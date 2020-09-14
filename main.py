import functions
from flask import jsonify


def search_data(request):
    response_body = functions.search_data(request)

    response = jsonify(response_body)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
