from flask import Flask

app = Flask(__name__)

# Name almacena el nombre del modulo "app.py" -> app

@app.route("/")
def index():
    return "Hello World my friends!"

if __name__ == '__main__':
    app.run(debug=True)