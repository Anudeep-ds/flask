from flask import Flask
### WSGI application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Flask first project"

@app.route('/project')
def project():
    return " Welcome to my first project"



if __name__=="__main__":
    app.run(debug=True)