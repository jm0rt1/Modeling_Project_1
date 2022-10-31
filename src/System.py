
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

    def print_games(self, ):
        if self.games is None:
            print("No Games Loaded...")
            return
        print("Select which game you would like to print the data for: \n")

        for i, game in enumerate(self.games):
            print(f"{i+1} -  {game.visTeamName}  at {game.homeTeamName}")
        valid_selection = False
        while not valid_selection:
            selection = input("Enter Number of Game to Print: ")

            try:
                sel_int = int(selection)
            except:
                print("Not a number")
                valid_selection = False
            sel_int -= 1
            if not 0 <= sel_int < len(self.games):
                print("Not in range")
                valid_selection = False
            else:
                valid_selection = True

        self.games[sel_int].print()


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
