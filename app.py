#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Cookies and Sessions Demo</h1>'

# DELIVERABLES
    # 1. Create a GET '/cookies' custom route
    # 2. In route function:
        # a. set_trace and inspect request cookies
        # b. set a cookie for hello=world
        # c. set another for foo=bar
        # d set another for current_user=codetombomb
    # 3. Use session to create encrypted current user_id
        # a. inspect datat in browser
    # 4. Return a JSON object with a key of cookies and a value of an array of cookie key value pairs

if __name__ == '__main__':
    app.run(port=5555, debug=True)