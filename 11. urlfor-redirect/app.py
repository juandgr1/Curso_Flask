from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/start")
def start():
    return url_for("start", next="login")

@app.route("/google")
def go_to_google():
    return redirect("https://www.google.com")

@app.route("/post/<int:id>")
def post(id):
    return "Showing post: {}".format(id)

@app.route("/today")
def today():
    #url_for redirige a una funcion dentro de una ruta, en este caso a la función post.
    return redirect(url_for("post", id=15, next="edit"))

if __name__ == "__main__":
    app.run(debug=True)