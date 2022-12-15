from flask import Flask, render_template

#create a Flask Instance
app=Flask(__name__)

#create a route decorator
@app.route('/')
def index():
    return render_template("index.html")
# virtualenv web
#source bin/activate
#flask --app hello.py --debug run