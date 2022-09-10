from distutils.command.upload import upload
from tracemalloc import start
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
import shutil,os,uuid
from util import *
from pathlib import Path
import importlib.util,os,subprocess,shutil,requests


"""Global var"""
UPLOAD_FOLDER_NAME: str =  'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
CONFIG_YAML_FILENAME = '../config.yaml'


"""Set up internal variable"""
dirname = os.path.dirname(__file__)
upload_dir = os.path.join(dirname, UPLOAD_FOLDER_NAME)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = upload_dir
app.secret_key = str(uuid.uuid1()) 
config = load_config_from_yaml(CONFIG_YAML_FILENAME)
img_res = config['resolution']
preprocessor_host= config["preprocessor_host"]
preprocessor_port= config["preprocessor_port"]
pifu_host = config["pifu_host"]
pifu_port = config["pifu_port"]
pix2surf_host = config["pix2surf_host"]
pix2surf_port = config["pix2surf_port"]
pifu_input_dir:str = config["pifu_input_dir"]
pifu_result_dir:str = config["pifu_result_dir"]
pix2surf_input_dir:str = config["pix2surf_input_dir"]
result_dir:str = config["result_dir"]

"""Front end"""
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and is_file_allowed(file.filename,ALLOWED_EXTENSIONS):
            filename = str(uuid.uuid1()) + file.filename[file.filename.rfind('.'):]
            file.save(os.path.join(upload_dir, filename))
            return redirect(url_for('success',fileid=filename))
    return render_template('index.html')


@app.route('/<fileid>/success', methods=['GET'])
def success(fileid):
    start_processing_image(fileid) 
    return render_template('file_uploaded.html',img=fileid)

@app.route('/display/<name>')
def display_image(name):
    fullpath = os.path.join(UPLOAD_FOLDER_NAME.replace('static/',''),name)
    return redirect(url_for('static', filename=fullpath), code=301)

# API endpoint
@app.route('/api/picture', methods=['POST'])
def api_upload_file():
    # return "upload file"
    # check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({
            "success": False,
            "message":"'No file part"
        })
    file = request.files['file']
    # # If the user does not select a file, the browser submits an
    # # empty file without a filename.
    if file.filename == '':
        return jsonify({
            "success": False,
            "message":"No selected file"
        })
    if file and is_file_allowed(file.filename):
        filename = str(uuid.uuid1()) + file.filename[file.filename.rfind('.'):]
        file.save(os.path.join(upload_dir, filename))
        return jsonify({
            "success": True,
            "message":"File upload success",
            "filename": filename
        })


"""Back end"""
def check_setup() -> bool:
    dirname, not_exists = check_dir_not_exist() 
    if not_exists:
        print(f"{dirname} missing")
        return False
    return True  

def check_dir_not_exist():
    for _dir in [pifu_input_dir,pifu_result_dir,upload_dir]:
        if not Path.exists(_dir):
            return _dir, True
    return "",False


def start_processing_image(fileid):
    print(f"===== Start processing photo {fileid} =====")
    preprocessing_image(fileid, preprocessor_host,preprocessor_port)
    gen_model_from_image(fileid,pifu_host,pifu_port)
    filename = clean_up(fileid,img_res)
    gen_pix2surf(filename)
    print(f"==== Done processing photo {fileid} ====")

def preprocessing_image(fileid:str,preprocessor_host:str,preprocessor_port:str):
    shutil.copyfile(f"{upload_dir}/{fileid}",f"{pifu_input_dir}/{fileid}")
    requests.get(f'http://{preprocessor_host}:{preprocessor_port}/{fileid}')

def gen_model_from_image(fileid:str,pifu_host:str,pifu_port:str):
    requests.get(f'http://{pifu_host}:{pifu_port}/{fileid}')

def gen_pix2surf(filename:str):
    filename_wo_extension = filename.replace(".obj","")
    os.remove(f"{pix2surf_input_dir}/body_0.obj")
    shutil.copyfile(f"{result_dir}/{filename}",f"{pix2surf_input_dir}/body_0.obj")
    requests.get(f'http://{pix2surf_host}:{pix2surf_port}/{filename_wo_extension}')
    shutil.copyfile(f"../pix2surf/{filename_wo_extension}.mp4",f"{upload_dir}/{filename_wo_extension}.mp4")

def clean_up(fileid,res) -> str:
    try:
        file_prefix = now()
        
        obj = fileid[:fileid.rfind('.')]+f"_{res}.obj"
        shutil.move(f"{pifu_result_dir}result_{obj}",f"{result_dir}/{file_prefix}_{obj}")
        png = obj.replace('.obj','.png')
        shutil.move(f"{pifu_result_dir}result_{png}",f"{result_dir}/{file_prefix}_{png}")

    except Exception as e:
        print(e)
    else:
        os.remove(f"{pifu_input_dir}{fileid}")
        os.remove(f"{pifu_input_dir}{fileid[:fileid.rfind('.')]}_rect.txt")
    finally:
        return f"{file_prefix}_{obj}"

if __name__ == '__main__':
    if check_setup == False:
        exit("setup failed") 
    app.run(host='0.0.0.0', port=5000)