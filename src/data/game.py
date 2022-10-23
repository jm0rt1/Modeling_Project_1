
from __future__ import annotations


from dataclasses import dataclass
import datetime
import enum
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

    def print(self, ):
        pass
