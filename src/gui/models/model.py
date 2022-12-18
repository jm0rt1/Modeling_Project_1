from __future__ import annotations
from typing import Optional
from PySide6 import QtCore
from src.data.game import Game
from src.gui.models.game_display_table_model import GameDisplayTableModel
from src.gui.models.games_list_combobox_model import GamesListComboboxModel
from src.gui.models.team_list_model import TeamListModel
# from src.online.client import SnoozelSportsClient
from src.background_tasks.qt.client_worker import ClientWorker


class Model(QtCore.QObject):
    def __init__(self, parent: Optional[QtCore.QObject] = None) -> None:
        super().__init__(parent)
        self.games_combobox_model = GamesListComboboxModel()
        self.displayed_game = GameDisplayTableModel()
        self.team_list_model = TeamListModel()
        self.client_worker = ClientWorker()
        self.client_worker.send_data.connect(  # type:ignore
            self.games_recieved)  # type:ignore
        self.client_worker.start()

    def load_data_from_snoozle_server(self, year: int, name: str):
        """
        make a request to the client worker

        Args:
            year (int): year of season
            name (str): Name of team
        """
        # self.games = SnoozelSportsClient.get_team_stats_by_name(
        #     year, name)
        self.client_worker.request_data(year, name)

    def games_recieved(self, games: list[Game]):
        """
        games sent from the ClientWorker are recieved here

        Args:
            games (list[Game]): Games downloaded by the ClientWorker
        """
        self.games = games
        self.games_combobox_model.clear()
        if len(self.games) > 0:
            self.games_combobox_model.update_model(self.games)
        elif len(self.games) == 0:
            self.games_combobox_model.display_no_games_found()
