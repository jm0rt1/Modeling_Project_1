
from __future__ import annotations


from dataclasses import dataclass
import datetime
import enum
from typing import Any
from src.data.team_stats import TeamStats


@dataclass
class Game:
    neutral: bool
    vis_team_name: str
    home_team_name: str
    is_final: bool
    date: datetime.date
    home_stats: TeamStats
    vis_stats: TeamStats

    class Keys(str, enum.Enum):
        NEUTRAL = "neutral"
        VIS_TEAM_NAME = "visTeamName"
        VIS_STATS = "visStats"
        HOME_STATS = "homeStats"
        IS_FINAL = "isFinal"
        DATE = "date"
        HOME_TEAM_NAME = "homeTeamName"

    @classmethod
    def from_dict(cls, a: dict[Any, Any]):
        home_stats = TeamStats.from_dict(a[Game.Keys.HOME_STATS])
        vis_stats = TeamStats.from_dict(a[Game.Keys.VIS_STATS])

        game = cls(a[Game.Keys.NEUTRAL], a[Game.Keys.VIS_TEAM_NAME],
                   a[Game.Keys.HOME_TEAM_NAME],
                   a[Game.Keys.IS_FINAL],
                   a[Game.Keys.DATE],
                   home_stats,
                   vis_stats)
        return game

    def print(self, ):
        pass
