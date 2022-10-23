
from __future__ import annotations


from dataclasses import dataclass
import datetime


@dataclass
class TeamStats:
    stat_id_code: str
    game_code: str
    team_code: int
    game_date: datetime.date
    rush_yds: int
    rush_att: int
    pass_yds: int
    pass_att: int
    pass_comp: int
    penalties: int
    penalt_yds: int
    fumbles_lost: int
    interceptions_thrown: int
    first_downs: int
    thrid_down_att: int
    third_down_conver: int
    fourth_down_att: int
    fourth_down_conver: int
    time_poss: int
    score: int
