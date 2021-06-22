from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

import os

UPLOAD_FOLDER = os.path.abspath("./Flask/Curso_Flask/19.upload-files/uploads/")
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpge", "gif", "pdf"])


def allowed_file(filename):

    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def index():

    return "Hello World"

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if "ourfile" not in request.files:
            return "The form has no file part."
        f = request.files["ourfile"]
        if f.filename == "":
            return "No file selected"
        if f and allowed_file(f.filename):
    #       filename = f.filename      #opcion original de guardado de nombre, se activa con secure filename una opcion de seguridad
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("get_file", filename=filename))
        return "File not allowed"

    return """
        <form method="POST" enctype="multipart/form-data">
        <input type="file" name="ourfile">
        <input type="submit" value="UPLOAD">
        </form>
        """

@app.route("/uploads/<filename>")
def get_file(filename):

    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)


