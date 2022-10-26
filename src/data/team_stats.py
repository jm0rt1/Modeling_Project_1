
from __future__ import annotations


from dataclasses import dataclass
import datetime
import enum


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

    class keys(str, enum.Enum):
        """
        Needs to be in the same order as the constructor
        """
        STAT_ID_CODE = "statIdCode"
        GAME_CODE = "gameCode"
        TEAM_CODE = "teamCode"
        GAME_DATE = "gameDate"
        RUSH_YDS = "rushYds"
        RUSH_ATT = "rushAtt"
        PASS_YDS = "passYds"
        PASS_ATT = "passAtt"
        PASS_COMP = "passComp"
        PENALTIES = "penalties"
        PENALTYDS = "penaltYds"
        FUMBLES_LOST = "fumblesLost"
        INTERCEPTIONS_THROWN = "interceptionsThrown"
        FIRST_DOWNS = "firstDowns"
        THRIDDOWN_ATT = "thridDownAtt"
        THIRDDOWN_CONVER = "thirdDownConver"
        FOURTH_DOWN_ATT = "fourthDownAtt"
        FOURTH_DOWN_CONVER = "fourthDownConver"
        TIME_POSS = "timePoss"
        SCORE = "score"
