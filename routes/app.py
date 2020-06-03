from flask import Flask

app = Flask(__name__)

# Name almacena el nombre del modulo "app.py" -> app

@app.route("/")
def index():
    return "Hello World my friends!"

@app.route("/hola")
def hola():
    return "Hola"

@app.route("/user/<string:user>")
def user(user):
    return "Hola " + user

@app.route("/numero/<int:n>")
def numero(n):
    return "Número: {}".format(n)
# string:name - int:name - float:name

@app.route("/default/")
@app.route("/default/<string:msg>")
def default( msg = "Default" ):
    return "Def: " + msg

if __name__ == '__main__':
    app.run(debug=True)