from flask import Flask

app = Flask (__name__)

@app.route("/")
def index():
    return'que pedo qleros '

@app.route("/hola")
def hola():
    return'Hola  perros'

if __name__=='__main__':
    app.run(debug=True)

