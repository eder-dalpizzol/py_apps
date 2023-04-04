from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_page', methods=['POST'])
def load_page():
    url = request.form['url']
    return render_template('load_page.html', url=url)

if __name__ == '__main__':
    app.run()
