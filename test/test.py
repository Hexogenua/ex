from flask import Flask,url_for,redirect,request
app = Flask(__name__)

@app.route('/success/<name>')
def succes(name):
    return 'welcome:{name}'.format(name)

@app.route("/login", classmethod)
