from __future__ import annotations
from typing import Optional
from PySide6 import QtCore
from src.gui.models.game_display_table_model import GameDisplayTableModel
from src.online.client import SnoozelSportsClient


class Model(QtCore.QObject):
    def __init__(self, parent: Optional[QtCore.QObject] = None) -> None:
        super().__init__(parent)
        self.displayed_game = GameDisplayTableModel()

    def load_data_from_snoozle_server(self, year: int, name: str):
        self.games = SnoozelSportsClient.get_team_stats_by_name(
            year, name)

    def update_games_list(self):
        pass
