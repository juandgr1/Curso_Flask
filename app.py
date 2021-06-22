from flask import Flask, jsonify

app = Flask(__name__)

isc_videos = [
    {
        "id": 1,
        "title": "1 - Hellow World - Curso Flask"
    },
    {
        "id": 2,
        "title": "2 - Metodo run - Curso Flask"
    }
]
cns_videos = [
    {
        "id": 1,
        "title": "1 - Hellow World - Curso Flask"
    },
    {
        "id": 2,
        "title": "2 - Metodo run - Curso Flask"
    }
]
@app.route("/")
def index():
#    print(__name__)
    return "Hello World!"

@app.route("/api/v1/videos/")
def get_all_videos():
    return jsonify({"videos": {"cns": cns_videos, "isc": isc_videos}})

if __name__ == "__main__":
    app.run(debug=True)

