import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import os
from pytube import YouTube


def download(link):
    dir_path = '/storage/emulated/0/Download'
    # if not os.path.exists(dir_path):
      # os.makedirs(dir_path)
    yt = YouTube(link)
    filename = ("video.mp4")
    ys = yt.streams.get_by_resolution("720p")
    ys.download(output_path=dir_path, filename=filename)

class HelloWorld(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            "Link: ",
            style=Pack(padding=(0, 5))
        )
        self.link_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.link_input)

        button = toga.Button(
            "Download!",
            on_press=self.on_click,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def on_click(self, widget):
        download(self.link_input.value)


def main():
    return HelloWorld()
