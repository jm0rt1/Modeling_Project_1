
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
        VISTEAMNAME = "visTeamName"
        VISSTATS = "visStats"
        HOMESTATS = "homeStats"
        ISFINAL = "isFinal"
        DATE = "date"

    def print(self, ):
        pass
