import speech_recognition as sr
import moviepy.editor as mp
from pytube import YouTube

link = "https://www.youtube.com/watch?v=TbpW5wt5M2Y"

yt = YouTube(link)

ys = yt.streams.get_by_resolution("720p")
ys.download(output_path="./videos", filename="video.mp4")

video_path = "./videos/video.mp4"


video = mp.VideoFileClip(video_path)

audio = video.audio.to_soundarray()

r = sr.Recognizer()
audio_text = sr.recognize_sphinx(audio)

search_word = "Elon Musk"
if search_word in audio_text:
    start_time = audio_text.index(search_word) / audio.frame_rate
    print(f"A palavra '{search_word}'  mencionada em {start_time} segundos.")
else:
    print(f"A palavra '{search_word}' nao mencionada no video.")
