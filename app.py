allDresses = [
    {
        "title":"Gween's Dress",
        "id": "first",
        "image": "IMG_2382.PNG",
        "description": [
                "Pencil mild",
                "collar detaiols",
                "Black zipper"
        ]
    },
        {
        "title":"jide's dress Dress",
        "id": "second",
        "description": [
                "black head",
                "red head",
                "Black zipper"
        ]
    }

]
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/owanbe")
def owanbe():
    return render_template("owanbe.html")

@app.route("/owanbe2")
def owanbe2():
    return render_template("owanbe2.html")

@app.route("/<dressid>")
def dress(dressid):
    for dress in allDresses:
        if dress['id'] == dressid:
            return render_template("each.html", dress=dress)
if __name__ == 'main':
    app.run(debug=True)
