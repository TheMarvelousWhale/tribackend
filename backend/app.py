import subprocess
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import shutil,os,uuid
from threading import Thread

UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
@app.route('/<id>/success', methods=['GET'])
def success(id):
    shutil.move(f"./static/{id}",f"./../pifuhd/sample_images/{id}")
    Thread(target=start_processing_image).start()
       
    return '''
    <!doctype html>
    <h1>Your Image has been successfully uploaded</h1>
    <h1><a href='/'>Back to homepage</a></h1>
    '''
def start_processing_image():
    print("start processing...")
    subprocess.call("./../pifuhd/start.sh")