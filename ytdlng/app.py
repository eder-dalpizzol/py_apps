from nicegui import ui
from pytube import YouTube
import pathlib

APP_NAME = 'Sophitube Downloader'
DOWNLOAD_DIR = pathlib.Path.home() / "Downloads"

def download():
  link = result.text
  yt = YouTube(
        link,
        use_oauth=False,
        allow_oauth_cache=True
    )
  filename = yt.title + ".mp4"
  filename = filename.replace("|", "-")
  ys = yt.streams.get_by_resolution("720p")
  ys.download(output_path=DOWNLOAD_DIR, filename=filename)

with ui.card():
  ui.label(APP_NAME).style('font-size: 200%')
  ui.input(label='Link', placeholder='Video link',
            on_change=lambda e: result.set_text(e.value))
  result = ui.label()
  ui.button('Download!', on_click=download)

ui.run(dark=True, title=APP_NAME)
