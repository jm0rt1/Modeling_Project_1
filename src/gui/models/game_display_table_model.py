from __future__ import annotations
from PySide6 import QtGui


class GameDisplayTableModel(QtGui.QStandardItemModel):
    def __init__(self):
        super().__init__(None)  # type:ignore

    def clear(self):
        self.clear()
