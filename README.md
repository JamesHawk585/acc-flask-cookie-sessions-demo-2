# acc-flask-cookie-sessions-demo

### Deliverables
1. In the app.py file, create a GET '/cookies' custom route
2. In route function:
    - set_trace and inspect request cookies
    - set a cookie for hello=world
    - set another for foo=bar
    - set another for current_user=codetombomb
3. Use session to create encrypted current user_id
    - inspect data in browser
4. Return a JSON object with a key of cookies and a value of an array of cookie key value pairs