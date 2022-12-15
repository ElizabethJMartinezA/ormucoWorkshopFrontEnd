from flask import Flask, render_template
import requests

#create a Flask Instance
app=Flask(__name__)

#create a route decorator
@app.route('/')
def index():
    
    url = "http://127.0.0.1:5000/listImages"
    images = requests.get(url=url).json()
    
    url2 = "http://127.0.0.1:5000/flavoursList"
    flavours = requests.get(url=url2).json()
    
    url3 = "http://127.0.0.1:5000/keypairsList"
    keyPairs = requests.get(url=url3).json()
    
    url4 = "http://127.0.0.1:5000/securityGroups"
    sGropus = requests.get(url=url4).json()
    
    url5 = "http://127.0.0.1:5000/networksList"
    networks = requests.get(url=url5).json()
    
    #url6 = "http://127.0.0.1:5000/getJson"
        
    return render_template("index.html", images=images,flavours=flavours, keyPairs=keyPairs, sGropus=sGropus,networks=networks)
# virtualenv web
#source bin/activate
#flask --app hello.py --debug run

if __name__ == '__main__':
    app.run(debug=True, port=8002)
    
    #export FLASK_APP=hello.py
    #export FLASK_ENV=development
    #flask run
