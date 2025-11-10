from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "secret-key-facemesh"

pairs = [
    ("real1.jpg", "ai1.jpg"),
    ("real2.jpg", "ai2.jpg"),
    ("real3.jpg", "ai3.jpg"),
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/politica")
def politica():
    return render_template("politica.html")

@app.route("/game1")
def game1():
    img_real, img_ai = random.choice(pairs)
    options = [("Real", img_real), ("IA", img_ai)]
    random.shuffle(options)
    return render_template("game1.html", options=options)

@app.route("/game2")
def game2():
    img_real, img_ai = random.choice(pairs)
    options = [("Real", img_real), ("IA", img_ai)]
    random.shuffle(options)
    return render_template("game2.html", options=options)

@app.route("/final")
def final():
    return render_template("final.html", score=random.randint(0,10))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

