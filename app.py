from flask import Flask, render_template, session
from flask_minify import minify
# from flask_bootstrap import Bootstrap
import functions
import secret

app = Flask(__name__)
# Bootstrap(app)
app.secret_key = secret.secret_key

minify(app=app, html=True, js=True, cssless=True)


def get_info():
    filter = {
        "title": "",
        "dateTo": "",
        "dateFrom": ""
    }

    data = {
        "items": functions.get_data(filter),
        "filter": filter
    }

    return data


@app.route('/')
def home():
    data = get_info()
    filter = data["filter"]
    has_filters = functions.has_filters(filter)

    return render_template("home.html", data=data["items"], filter=filter, has_filters=has_filters)


@app.route('/py_test')
def py_test():
    session["name"] = "cameron"

    response = {
        "data": "test"
    }
    return response
