from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "germy - 16-09-2020 - Hello World!"

@application.route("/mi")
def mi():
    return "soy el metodo mi"

@application.route("/mi2")
def mi2():
    return "soy otro metodo mi, anda"

if __name__ == "__main__":
    application.run()
