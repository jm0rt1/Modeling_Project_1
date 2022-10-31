
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Optional

from src.data.game import Game
from src.json_49ers_serdes.deserializer import Deserializer
from src.json_49ers_serdes.serializer import Serializer


class System:
    def __init__(self):
        self.games: Optional[list[Game]] = None

    def load_data(self, ):
        path = choose_file_open()
        self.games = Deserializer().from_file(path)
        print(f"{len(self.games)} games loaded")

    def save_data(self, ):
        if self.games is None:
            print("No Games Loaded...")
            return

        path = choose_file_save()
        Serializer().to_file(self.games, path)
        print(f"{len(self.games)} have been saved to {path.as_posix()}")

    def add_game(self, game: Game):
        pass

    def Operation1(self, ):
        pass


def choose_file_open():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    root.quit()
    return Path(file_path)


def choose_file_save():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.asksaveasfilename()
    root.quit()
    return Path(file_path)
