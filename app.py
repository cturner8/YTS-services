from flask import Flask, render_template
import functions

app = Flask(__name__)


def get_info():
    filter = {}
    filter["title"] = ""
    filter["dateTo"] = ""
    filter["dateFrom"] = ""

    return functions.get_data(filter)


@app.route('/')
def home():

    return render_template("home.html", data=get_info())
