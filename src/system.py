
# -*- coding: utf-8 -*-
from __future__ import annotations
import enum
from pathlib import Path
from typing import Optional

from src.data.game import Game
from src.nfl_json_serdes.deserializer import Deserializer
from src.nfl_json_serdes.serializer import Serializer
from src.online.client import SnoozelSportsClient, TeamNamesIntEnum


class TeamRoles(str, enum.Enum):
    HOME = "home"
    AWAY = "away"


class System:
    def __init__(self, games: Optional[list[Game]] = None):
        self.games: Optional[list[Game]] = games

    def load_data_from_file(self):
        path = choose_file_open()
        self.games = Deserializer().from_file(path)
        print(f"{len(self.games)} games loaded")

    def load_data_from_snoozle_server(self):
        year, number = self.__get_year_and_team()

        self.games = SnoozelSportsClient.get_team_stats_by_number(
            year, TeamNamesIntEnum(number))

    def __get_year_and_team(self) -> tuple[int, int]:
        ok = False
        year = None
        number = None
        while not ok:
            year_str = input("Enter desired season year: ")
            try:
                year = int(year_str)
                ok = True
            except:
                print("not a valid year, must be numeric/integer")
        print()
        print(TeamNamesIntEnum.print_all_names_numbered())

        ok = False
        while not ok:
            number_str = input("Enter number of desired team")

            try:
                number = int(number_str)
                ok = True
            except:
                print("not a valid year, must be numeric/integer")

        if year is None or number is None:
            raise RuntimeError("Something went wrong")
        return year, number

    def get_team_record(self):
        year, number = self.__get_year_and_team()
        games = SnoozelSportsClient.get_team_stats_by_number(
            year, TeamNamesIntEnum(number))
        name = TeamNamesIntEnum.get_str_name(number)
        wins = 0
        loss = 0

        # calculate wins and losses
        for game in games:
            if game.homeTeamName == name:
                this_team_stats = game.homeStats
                other_team_stats = game.visStats
            else:
                this_team_stats = game.visStats
                other_team_stats = game.homeStats

            if this_team_stats.score > other_team_stats.score:
                wins += 1
            else:
                loss += 1

        print(f"Team #{number}: {name} {year} W-L Record: {wins} - {loss}")
        pass

    def save_data(self):
        if self.games is None:
            print("No Games Loaded...")
            return

        path = choose_file_save()
        Serializer().to_file(self.games, path)
        print(f"{len(self.games)} have been saved to {path.as_posix()}")

    def add_game(self, game: Optional[Game] = None):
        """
        The default argument exists for the purpose of reducing the number of dependencies in run.py, also eliminates an if block

        Args:
            game (Game, optional): Add a Game instance to the self.games list. Defaults to Game.from_console_input().
        """
        if game is None:
            game = Game.from_console_input()
        # initialize
        if self.games is None:
            self.games = []
        self.games.append(game)

    def print_games(self):
        if self.games is None:
            print("No Games Loaded...")
            return
        print("Select which game you would like to print the data for: \n")

        for i, game in enumerate(self.games):
            print(f"{i+1} -  {game.visTeamName}  at {game.homeTeamName}")
        valid_selection = False
        selection_int = None
        while not valid_selection:
            selection = input("Enter Number of Game to Print: ")
            try:
                selection_int = int(selection)
            except:
                print("Not a number")
                valid_selection = False
                continue
            selection_int -= 1
            if not 0 <= selection_int < len(self.games):
                print("Not in range")
                valid_selection = False
                continue
            else:
                valid_selection = True

        if selection_int is None:
            print("selection was not initialized -- an unexpected error occurred")
        else:
            self.games[selection_int].print()

    def find(self):
        if self.games is None:
            print("No Games Loaded...")
            return
        name: str = input("Enter name of the team (not case-sensitive): ")

        home_away: str = input("Home or Away?: ")

        # loop over games, find the name of the home/away team, and then compare equality.
        found: list[Game] = []

        for game in self.games:
            if home_away == TeamRoles.HOME and game.homeTeamName.lower() == name:
                found.append(game)  # type:ignore
            if home_away == TeamRoles.AWAY and game.visTeamName.lower() == name:
                found.append(game)  # type:ignore
        if len(found) == 0:
            print("...not found")
            return
        for i, game in enumerate(found):
            print()
            print()
            print(f"found {i+1}:")
            game.print()
            print()
            print("-------------------------")


def choose_file_open():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    root.quit()
    root.destroy()
    root.mainloop()

    return Path(file_path)


def choose_file_save():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename()

    root.quit()
    root.destroy()
    root.mainloop()

    return Path(file_path)
