from flask import Flask, render_template, session, redirect, url_for, jsonify, request
from flask_cors import CORS
from flask_minify import minify
from dotenv import load_dotenv

import functions
import secret

load_dotenv()

app = Flask(__name__)
app.secret_key = secret.secret_key
CORS(app)

minify(app=app, html=True, js=True, cssless=True)


@app.route('/search', methods=["GET", "POST"])
def search_data():
    response_body = functions.search_data(request)

    response = jsonify(response_body)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
