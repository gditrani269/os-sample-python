from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "germy - 16-09-2020 - Hello World!"

if __name__ == "__main__":
    application.run()
