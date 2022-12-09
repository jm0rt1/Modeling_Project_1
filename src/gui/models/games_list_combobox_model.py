
from __future__ import annotations
from PySide6 import QtGui

from src.data.game import Game


class GamesListComboboxModel(QtGui.QStandardItemModel):

    def __init__(self):
        super().__init__(None)

    def update_model(self, games_list: list[Game]):
        str_list = list_games(games_list)

        for game_str in str_list:
            self.appendRow(QtGui.QStandardItem(game_str))


def list_games(games: list[Game]) -> list[str]:
    out_list = []
    for i, game in enumerate(games):
        out_list.append(
            f"{i+1} -  {game.visTeamName}  at {game.homeTeamName}")
    return out_list
