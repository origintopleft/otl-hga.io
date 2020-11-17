#!/usr/bin/env python3

import random

from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/favicon.ico")
def favicon():
    return redirect("https://cdn.otl-hga.net/index/favicon.png", code=301)


@app.route('/', defaults={"path": ""})
@app.route("/<path:path>") 
def index_page(path):
    context = {"title": "otl-hga.net", "styles": [], "scripts": []}
    context["styles"].append("https://cdn.otl-hga.net/index/css/index.css")
    context["scripts"].append("https://cdn.otl-hga.net/gradius/gradius.js")
    return render_template("index_new", **context)

@app.after_request
def clacks_overhead(resp):
    names_to_honor = [
            "Breonna Taylor",
            "George Floyd",
            "Trayvon Martin",
            "Terry Pratchett"
        ]

    resp.headers["X-Clacks-Overhead"] = "GNU {0}".format(random.choice(names_to_honor))
    return resp

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
