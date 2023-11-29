from flask import Flask

model = None

app = Flask(__name__)

@app.route("/")
def hello():
    return "Bonjour bienvenue dans flask"

def run(load_model):
    global model
    model = load_model
    app.run(debug=True)