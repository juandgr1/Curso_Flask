from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/Flask/Curso_Flask/7.database/database_test.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))


@app.route("/")
def index():
    titulo = "Home!"
    lista = ["footer", "header", "info"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/insert/default")
def insert_default():
    new_post = Posts(title="Default Title")
    db.session.add(new_post)
    db.session.commit()
    return "The default Post was created"

@app.route("/select/default")
def select_default():
    post = Posts.query.filter_by(id=1).first()
    print(post.title)
    return "Query done."

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


# comandos para probar la base de datos
#     desde el directorio de trabajo 
#         sqlite3 database.db

#     una vez adentro de la base de datos
#         .schema 
#             este comando muestra las tablas 
        # .tables 
        #     muestra las tablas 
        # select * from posts;
            



