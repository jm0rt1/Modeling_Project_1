from __future__ import annotations
from PySide6 import QtGui

from src.data.game import Game
from src.data.team_stats import TeamStats

KEY_BLACKLIST = [TeamStats.Keys.STAT_ID_CODE,
                 TeamStats.Keys.GAME_CODE, TeamStats.Keys.GAME_DATE, TeamStats.Keys.TEAM_CODE]


class GameDisplayTableModel(QtGui.QStandardItemModel):
    def __init__(self):
        """
        constructor
        """
        super().__init__(None)  # type:ignore

    def populate(self, game: Game):
        """
        Populate the table with information from the selected game

        Args:
            game (Game): Game to display
        """
        self.appendRow([QtGui.QStandardItem(""), QtGui.QStandardItem(  # type:ignore
            game.visTeamName), QtGui.QStandardItem("at"), QtGui.QStandardItem(game.homeTeamName)])

        for key in game.visStats.__dict__.keys():
            vis_stats = game.visStats.__dict__
            home_stats = game.homeStats.__dict__
            if key in KEY_BLACKLIST:
                continue
            self.appendRow([QtGui.QStandardItem(key), QtGui.QStandardItem(  # type:ignore
                str(vis_stats[key])), QtGui.QStandardItem("-"), QtGui.QStandardItem(str(home_stats[key]))])
