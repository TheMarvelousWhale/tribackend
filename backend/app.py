from tracemalloc import start
from flask import Flask, flash, request, redirect, url_for,render_template
import shutil,os,uuid
from config import init_config
from pipeline import *


UPLOAD_FOLDER = './static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CONFIG = init_config()
IMG_RES = CONFIG['resolution']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
        if file and allowed_file(file.filename):
            filename = str(uuid.uuid1()) + file.filename[file.filename.rfind('.'):]
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('success',id=filename))
    return render_template('index.html')


@app.route('/<id>/success', methods=['GET'])
def success(id):
    shutil.copyfile(f"{UPLOAD_FOLDER}/{id}",f"./../pifuhd/sample_images/{id}")
    #Thread(target=start_processing_image,args=(id,)).start()
    start_processing_image(id) 
    return render_template('file_uploaded.html',img=id)

def start_processing_image(id):
    print(f"Start processing photo {id}")
    preprocessing_image(id)
    gen_model_from_image(res=IMG_RES)
    clean_up(id,res=IMG_RES)
    print(f"Done processing photo {id}")

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/'+filename), code=301)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)