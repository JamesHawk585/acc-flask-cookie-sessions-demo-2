#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify, session
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '<h1>Cookies and Sessions Demo</h1>'

def expiration_date(delay):
    expire_date = datetime.datetime.now()
    expire_date = expire_date + datetime.timedelta(days=delay)
    return expire_date
    
@app.route("/cookies", methods=['GET'])
def cookies():
    # import ipdb; ipdb.set_trace()
    resp = make_response(jsonify({"cookies": [{key: value} for key, value in request.cookies.items()]}))
    resp.set_cookie("hello", "world", expires=expiration_date(90))
    resp.set_cookie("foo", "bar", httponly=True, path="/cookies", max_age=3)
    session["current_user"] = "codetombomb"
    session["more_protected_data"] = "username"
    
    return resp, 200
    

# DELIVERABLES
    # 1. Create a GET '/cookies' custom route
    # 2. In route function:
        # - set_trace and inspect request cookies
        # - set a cookie for hello=world
        # - set another for foo=bar
        # - set another for current_user=codetombomb
        # - on last cookie, set path, expiration date, max age, httpOnly    
    # 3. Use session to create encrypted current user_id
        # - generate app.secret_key -> Cheatsheet: https://furry-shrimp-4f0.notion.site/Cookies-and-Sessions-Cheatsheet-2e4cbcd1c8ee4d71b8b0da395ebb3fe4?pvs=4
        # - create a session and store a user_id=1
        # - inspect session cookie in the browser
        # - delete cookie on the browser and check request.cookies on the server side

if __name__ == '__main__':
    app.run(port=5555, debug=True)