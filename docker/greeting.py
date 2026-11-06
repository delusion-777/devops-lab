
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Greetings from Jaswanth - Docker Version 2.0!</h1>"
