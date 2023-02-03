from flask import Flask, render_template, request, redirect
import sqlite3, os
from db import create_db
from settings import path

app = Flask(__name__)

# create_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadprod', methods=['GET', 'POST'])
def cadprod():
    if request.method == 'POST':
        descricao = request.form['descricao']
        preco = request.form['preco']
        qtde = request.form['qtde']
        codebar = request.form['codebar']

        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute("INSERT INTO products (descricao, preco, qtde, codebar) VALUES (UPPER(?), ?, ?, ?)",
                  (descricao, preco, qtde, codebar))
        conn.commit()
        conn.close()

        return redirect("/")
    return render_template("cadprod.html")

@app.route("/listprod")
def listprod():
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    con.close()
    return render_template("listprod.html", products=products)

@app.route("/movprod", methods=["GET", "POST"])
def movprod():
    if request.method == "POST":
        product = request.form.get("product")
        mov_type = request.form.get("type")
        price = request.form.get("price")
        general_info = request.form.get("GeneralInfo")
        
        # Check if the price is not empty
        if price == "":
            price = 0
        else:
            price = float(price)

        # Add the data to the kardex table
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO kardex (product, mov_type, price, general_info) VALUES (?, ?, ?, ?)",
            (product, mov_type, price, general_info),
        )
        conn.commit()
        conn.close

        return redirect("/")
    
    # Get all products from the products table
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close
    
    return render_template("movprod.html", products=products)


@app.route('/report')
def report():
    return render_template('report.html')

if __name__ == '__main__':
    app.run()
