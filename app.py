from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/eleccion")
def eleccion():
    return render_template("eleccion.html")

@app.route("/razones")
def razones():
    return render_template("razones.html")

@app.route("/final")
def final():
    return render_template("final.html")

if __name__ == "__main__":
    app.run()