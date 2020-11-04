from flask import Flask
application = Flask(__name__)

#--------------------------------------
def m ():
    return ("hola")
#--------------------------------------
@application.route("/")
def hello():
    return "germy - 16-09-2020 - Hello World!"

@application.route("/mi")
def mi():
    return "soy el metodo mi"

@application.route("/mi2")
def mi2():
    return "soy otro metodo mi, anda"

@application.route("/fun")
def fun():
    return m()

if __name__ == "__main__":
    application.run()
