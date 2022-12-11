from __future__ import annotations
from typing import Optional
from PySide6 import QtCore
from src.gui.models.game_display_table_model import GameDisplayTableModel
from src.gui.models.games_list_combobox_model import GamesListComboboxModel
from src.gui.models.team_list_model import TeamListModel
from src.online.client import SnoozelSportsClient


class Model(QtCore.QObject):
    def __init__(self, parent: Optional[QtCore.QObject] = None) -> None:
        super().__init__(parent)
        self.games_combobox_model = GamesListComboboxModel()
        self.displayed_game = GameDisplayTableModel()
        self.team_list_model = TeamListModel()

    def load_data_from_snoozle_server(self, year: int, name: str):
        self.games = SnoozelSportsClient.get_team_stats_by_name(
            year, name)
        self.games_combobox_model.update_model(self.games)
