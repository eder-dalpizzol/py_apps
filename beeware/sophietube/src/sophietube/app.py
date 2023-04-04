import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import os
from pytube import YouTube
from toga import timer

def download(link, progress_bar):
    dir_path = '/storage/emulated/0/Download'
    yt = YouTube(link)
    filename = "video.mp4"
    ys = yt.streams.get_by_resolution("720p")
    total_size = int(ys.filesize)

    # Iniciar o download
    with ys.stream_to_file(os.path.join(dir_path, filename)) as file:
        # Definir a função de callback de atualização da barra de progresso
        def update_progress():
            progress_bar.value = file.tell()
            if progress_bar.value < progress_bar.max:
                timer.schedule(update_progress, 0.1)

        # Iniciar o temporizador para atualizar a barra de progresso
        timer.schedule(update_progress, 0.1)


class Sophietube(toga.App):

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
    return Sophietube()
