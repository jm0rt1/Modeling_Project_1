from PySide6 import QtCore

from src.online.client import SnoozelSportsClient

# using QThread to develop the interface directly into the event loop of the PySide6 (Qt) based GUI

import pydevd


class ClientWorker(QtCore.QThread):
    send_data = QtCore.Signal(object)

    def __init__(self, condition: QtCore.QWaitCondition = QtCore.QWaitCondition(), mutex: QtCore.QMutex = QtCore.QMutex()) -> None:
        super().__init__(None)
        self.condition = condition
        self.mutex = mutex
        self.year = 0
        self.name = ""

    def run(self):
        pydevd.settrace(suspend=False)
        while True:
            self.mutex.lock()
            self.condition.wait(self.mutex)
            self.mutex.unlock()
            games = SnoozelSportsClient.get_team_stats_by_name(
                self.year, self.name)
            self.send_data.emit(games)
            pass

    def request_data(self, year: int, name: str):
        self.year = year
        self.name = name
        self.condition.wakeAll()
