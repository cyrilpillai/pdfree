from flask import Flask, render_template, request, redirect, send_file
from werkzeug.utils import secure_filename
import os
import pikepdf

app = Flask(__name__)
app.config['STORAGE'] = 'storage'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    error_message = ''
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        # If the user does not select a file, the browser may
        # submit an empty part without a filename
        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['STORAGE'], filename))
            password = request.form['password']
            input_path = os.path.join(app.config['STORAGE'], filename)
            output_path = os.path.join(app.config['STORAGE'], 'pdfree_' + filename)

            success = remove_password(input_path, output_path, password)

            if success:
                result = send_file(output_path, as_attachment=True)
                remove_file(input_path)
                remove_file(output_path)
                return result
            else:
                error_message = 'Invalid password. Please try again.'

    return render_template('index.html', error_message=error_message)

def remove_password(input_path, output_path, password):
    try:
        with pikepdf.open(input_path, password=password) as pdf:
            pdf.save(output_path)
        return True
    except:
        return False


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been successfully removed.")
    except OSError as e:
        print(f"Error occurred while removing file '{file_path}': {e}")
