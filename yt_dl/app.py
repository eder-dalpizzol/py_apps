from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/download', methods=['POST'])
def download():
    link = request.form['link']
    yt = YouTube(link)
    filename = yt.title + ".mp4"
    filename = filename.replace("|", "-")
    ys = yt.streams.get_by_resolution("720p")
    ys.download(output_path="./videos", filename=filename)
    return send_file(os.path.join("./videos", filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
