from flask import Flask
import requests
app = Flask(__name__)
headers = {'user-agent' : 'controller'}
dogUrl = "http://dog-service:6060"
catUrl = "http://cat-service:7070"

@app.route('/')
def index_route():
    dogRes = requests.get(url = dogUrl, headers=headers)
    catRes = requests.get(url = catUrl, headers=headers)
    return "<p> cat says: " + catRes.text + "</p> <p> dog says: " + dogRes.text + "</p>"

# Status route, made for kuber
@app.route('/status')
def status_route():
    return ""

if __name__ == "__main__":
    app.run(debug=False)