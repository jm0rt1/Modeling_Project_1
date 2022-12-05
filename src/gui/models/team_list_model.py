

from __future__ import annotations
from PySide6 import QtGui
from src.online.client import TeamNamesIntEnum


class TeamListModel(QtGui.QStandardItemModel):

    def __init__(self):
        super().__init__(None)
        names = TeamNamesIntEnum.list_names()
        for name in names:
            self.appendRow(QtGui.QStandardItem(name))
