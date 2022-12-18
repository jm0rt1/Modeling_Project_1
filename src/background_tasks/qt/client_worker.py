from PySide6 import QtCore

from src.online.client import SnoozelSportsClient

# using QThread to develop the interface directly into the event loop of the PySide6 (Qt) based GUI


class ClientWorker(QtCore.QThread):
    send_data = QtCore.Signal(object)

    def __init__(self, condition: QtCore.QWaitCondition = QtCore.QWaitCondition(), mutex: QtCore.QMutex = QtCore.QMutex()) -> None:
        """
        Constructor

        Args:
            condition (QtCore.QWaitCondition, optional): optional condition variable. Defaults to QtCore.QWaitCondition().
            mutex (QtCore.QMutex, optional): optional mutex. Defaults to QtCore.QMutex().
        """
        super().__init__(None)
        self.condition = condition
        self.mutex = mutex
        self.year = 0
        self.name = ""

    def run(self):
        """
        called on self.start, very simple, not much error checking
        """
        while True:
            self.mutex.lock()
            self.condition.wait(self.mutex)
            self.mutex.unlock()
            games = SnoozelSportsClient.get_team_stats_by_name(
                self.year, self.name)
            self.send_data.emit(games)  # type:ignore
            pass

    def request_data(self, year: int, name: str):
        """
        Wake the thread to request data from the API

        Args:
            year (int): year of season
            name (str): name of team
        """
        self.year = year
        self.name = name
        self.condition.wakeAll()
