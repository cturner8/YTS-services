from flask import Flask, render_template, session, redirect, url_for, jsonify, request
from flask_cors import CORS
from flask_minify import minify

import functions
import secret

app = Flask(__name__)
app.secret_key = secret.secret_key
app.config['JSON_SORT_KEYS'] = False
CORS(app)

minify(app=app, html=True, js=True, cssless=True)


@app.route('/search', methods=["GET", "POST"])
def search_data():
    filter = {
        "title": "",
        "dateTo": "",
        "dateFrom": ""
    }

    if request.method == "POST":
        body = request.get_json()

        filter["title"] = body.get("title")
        filter["dateTo"] = body.get("dateTo")
        filter["dateFrom"] = body.get("dateFrom")

    response_body = {
        "filter": filter,
        "items": functions.get_data(filter)
    }

    response = jsonify(response_body)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/')
def view():
    data = search_data()
    filter = data["filter"]
    has_filters = functions.has_filters(filter)

    return render_template("view.html", data=data["items"], filter=filter, has_filters=has_filters)


@app.route('/upload')
def upload():
    return render_template("upload.html")


@app.route('/py_test')
def py_test():
    session["name"] = "cameron"

    response = {
        "data": "test"
    }

    redirect(url_for('upload'))

    return response


@app.route('/testing', methods=['GET'])
def testing():
    response = {
        "data": "hello"
    }

    return jsonify(response)
