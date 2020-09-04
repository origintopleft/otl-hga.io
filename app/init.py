#!/usr/bin/env python3

from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/favicon.ico")
def favicon():
    return redirect("https://cdn.otl-hga.net/index/favicon.png", code=301)

@app.route('/', defaults={"path": ""})
@app.route("/<path:path>") 
def index_page(path):
    return render_template("index")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
