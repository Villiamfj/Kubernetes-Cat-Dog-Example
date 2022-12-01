from flask import Flask
app = Flask(__name__)

@app.route('/')
def index_route():
    return "meow"
    
# Status route, made for kuber
@app.route('/status')
def status_route():
    return ""

if __name__ == "__main__":
    app.run(debug=False)