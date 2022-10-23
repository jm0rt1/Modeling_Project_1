
# -*- coding: utf-8 -*-

from dataclasses import dataclass
import datetime
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

    def print(self, ):
        pass
