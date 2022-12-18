
from __future__ import annotations
from PySide6 import QtGui

from src.data.game import Game


class GamesListComboboxModel(QtGui.QStandardItemModel):

    def __init__(self):
        """
        Constructor
        """
        super().__init__(None)  # type:ignore

    def update_model(self, games_list: list[Game]):
        """
        Load a games list into the model (does not clear the model)

        Args:
            games_list (list[Game]): list of games to load
        """
        str_list = list_games(games_list)

        for game_str in str_list:
            self.appendRow(QtGui.QStandardItem(game_str))  # type:ignore

    def display_no_games_found(self):
        """
        When no games are found, run this method to display "No Games Found" (does not clear the model)
        """
        self.appendRow(QtGui.QStandardItem("No Games Found"))  # type:ignore


def list_games(games: list[Game]) -> list[str]:
    out_list: list[str] = []
    for i, game in enumerate(games):
        out_list.append(  # type:ignore
            f"{i+1} -  {game.visTeamName}  at {game.homeTeamName}")
    return out_list
