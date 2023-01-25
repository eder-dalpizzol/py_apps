from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM users WHERE name="{name}"')
        user = cursor.fetchone()
        cursor.execute(f'SELECT * FROM users')
        users = cursor.fetchall()
        if user:
            return render_template("user_found.html", user=user, users=users)
        else:
            return render_template("user_not_found.html")
    else:
        return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)
