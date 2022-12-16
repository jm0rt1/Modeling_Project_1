from PySide6 import QtCore

from src.online.client import SnoozelSportsClient

# using QThread to develop the interface directly into the event loop of the PySide6 (Qt) based GUI


class ClientWorker(QtCore.QThread):

    def __init__(self, condition: QtCore.QWaitCondition = QtCore.QWaitCondition(), mutex: QtCore.QMutex = QtCore.QMutex()) -> None:
        self.condition = condition
        self.mutex = mutex

    def run(self):
        while True:
            self.mutex.lock()
            self.condition.wait(self.mutex)
            games = SnoozelSportsClient.get_team_stats_by_name(
                year, name)
            self.get_data()

    def get_data(self):
        pass
