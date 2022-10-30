
from __future__ import annotations


import datetime
import enum
from typing import Any
from src.data.team_stats import TeamStats


class Games():
    def __init__(self):
        pass


class Game:
    def __init__(self) -> None:

        self.neutral: bool
        self.visTeamName: str
        self.visStats: str
        self.homeStats: bool
        self.isFinal: datetime.date
        self.date: TeamStats
        self.homeTeamName: TeamStats

    class Keys(str, enum.Enum):
        NEUTRAL = "neutral"
        VIS_TEAM_NAME = "visTeamName"
        VIS_STATS = "visStats"
        HOME_STATS = "homeStats"
        IS_FINAL = "isFinal"
        DATE = "date"
        HOME_TEAM_NAME = "homeTeamName"

    def __str__(self):
        return str(self.__dict__)

    @classmethod
    def from_dict(cls, a: dict[Any, Any]):
        a[Game.Keys.HOME_STATS] = TeamStats.from_dict(a[Game.Keys.HOME_STATS])
        a[Game.Keys.VIS_STATS] = TeamStats.from_dict(a[Game.Keys.VIS_STATS])
        game = cls()
        game.__dict__ = a
        return game

    def to_dict(self) -> dict[Any, Any]:
        data = self.__dict__
        data[Game.Keys.HOME_STATS] = data[Game.Keys.HOME_STATS].to_dict()
        data[Game.Keys.VIS_STATS] = data[Game.Keys.VIS_STATS].to_dict()
        return data

    def print(self, ):
        pass
