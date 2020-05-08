import sys
import webbrowser
import os
import pathlib
import requests
import json
import webbrowser

from flask import Flask, render_template, request, jsonify, url_for, redirect

app = Flask(__name__)

def joke():
    f = r"http://api.icndb.com/jokes/random"
    data = requests.get(f)
    tt = json.loads(data.text)
    result = tt["value"]["joke"]
    return result

joke()


@app.route('/')
def index():
    return render_template("index.html", data = joke())

if __name__ == "__main__":
    app.run(port='5000', host='0.0.0.0', debug = True)

