import functions
from flask import jsonify


def search_data(request):
    response_body = functions.search_data(request)

    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows POST requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    response = jsonify(response_body)
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    return (response, 200, headers)
