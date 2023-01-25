from flask import Flask, request, render_template
from create_db import create_database_and_tables
import sqlite3

app = Flask(__name__)

create_database_and_tables()

@app.route("/")
def form():
    return render_template("form2.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    return "Name saved: " + name

if __name__ == "__main__":
    app.run(debug=True)
