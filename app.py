from flask import Flask, render_template
from flask_minify import minify
from flask_bootstrap import Bootstrap
import functions

app = Flask(__name__)
Bootstrap(app)

minify(app=app, html=True, js=True, cssless=True)


def get_info():
    filter = {}
    filter["title"] = ""
    filter["dateTo"] = ""
    filter["dateFrom"] = ""

    return functions.get_data(filter)


@app.route('/')
def home():

    return render_template("home.html", data=get_info())
