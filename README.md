# acc-flask-cookie-sessions-demo

Cookies and Sessions cheatsheet: [Link](https://furry-shrimp-4f0.notion.site/Cookies-and-Sessions-Cheatsheet-2e4cbcd1c8ee4d71b8b0da395ebb3fe4?pvs=4)

### Deliverables
1. Create a GET '/cookies' custom route
2. In route function:
    - set_trace and inspect request cookies
    - set a cookie for hello=world
    - set another for foo=bar
    - set another for current_user=codetombomb
    - on last cookie, set path, expiration date, max age, httpOnly    
3. In the client:
    - Use useEffect to send a GET request to '/cookies'
    - parse resp as json and console.log resp
    - console.log document.cookie
    - Note the cookies that are marked as HTTP only 

## Sesssions
Review sesssions: [Link to slides](https://docs.google.com/presentation/d/1n50KET2YQJJoXdJQUcGMIdeyEYcqbKda3SU_kZeWTLU/edit?usp=sharing)

4. Use session to create encrypted current user_id
    - generate app.secret_key -> Cheatsheet: https://furry-shrimp-4f0.notion.site/Cookies-and-Sessions-Cheatsheet-2e4cbcd1c8ee4d71b8b0da395ebb3fe4?pvs=4
    - create a session and store a user_id=1
    - inspect session cookie in the browser
    - delete cookie on the browser and check request.cookies on the server side