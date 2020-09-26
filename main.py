import firebase_admin
from firebase_admin import credentials, auth

import functions
from flask import jsonify


cred = credentials.Certificate("./serviceAccount.json")
firebase_admin.initialize_app(cred)


def search_data(request):
    if "Authorization" not in request.headers:
        return ({'error': 'no authorization token'}, 500)

    decoded_token = auth.verify_id_token(
        request.headers["Authorization"])
    uid = decoded_token['uid']
    print(uid)

    response_body = functions.search_data(request)

    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows POST requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    response = jsonify(response_body)
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    return (response, 200, headers)