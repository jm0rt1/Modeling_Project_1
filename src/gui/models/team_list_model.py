

from __future__ import annotations
from PySide6 import QtGui
from src.online.client import TeamNamesIntEnum


class TeamListModel(QtGui.QStandardItemModel):

    def __init__(self):
        """
        constructor, one time setup, no other methods
        """
        super().__init__(None)  # type:ignore
        names = TeamNamesIntEnum.list_names()
        for name in names:
            self.appendRow(QtGui.QStandardItem(name))  # type:ignore
