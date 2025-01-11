from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = '138.41.20.102'
app.config['MYSQL_PORT'] = 53306
app.config['MYSQL_USER'] = 'ospite'
app.config['MYSQL_PASSWORD'] = 'ospite'
app.config['MYSQL_DB'] = 'w3schools'

mysql = MySQL(app)

#prodotti = (('p1', 'p1', 'p1', 'p1', 'p1', 'p1'),('p2', 'p2', 'p2', 'p2', 'p2', 'p2'), ('p3', 'p3', 'p3', 'p3', 'p3', 'p3'))

@app.route("/")
def homePage():
    return render_template('home.html', titolo="Home page")

@app.route("/products")
def products():

    #Interrogazione al DB
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    prodotti = cursor.fetchall()
    return render_template('products.html', titolo="Products", prodotti=prodotti)

@app.route("/category/<id>")
def category(id):
    #interrogazione al DB
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM categories WHERE CategoryID="+ id
    cursor.execute(query)
    dati = cursor.fetchall()
    return render_template('category.html', dati = dati)

app.run(debug=True)
