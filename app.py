from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
@app.route("/")
def homePage():
    return render_template('home.html', titolo="Home page")

app.run()
