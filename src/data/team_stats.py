
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
        STATIDCODE = "statIdCode"
        GAMECODE = "gameCode"
        TEAMCODE = "teamCode"
        GAMEDATE = "gameDate"
        RUSHYDS = "rushYds"
        RUSHATT = "rushAtt"
        PASSYDS = "passYds"
        PASSATT = "passAtt"
        PASSCOMP = "passComp"
        PENALTIES = "penalties"
        PENALTYDS = "penaltYds"
        FUMBLESLOST = "fumblesLost"
        INTERCEPTIONSTHROWN = "interceptionsThrown"
        FIRSTDOWNS = "firstDowns"
        THRIDDOWNATT = "thridDownAtt"
        THIRDDOWNCONVER = "thirdDownConver"
        FOURTHDOWNATT = "fourthDownAtt"
        FOURTHDOWNCONVER = "fourthDownConver"
        TIMEPOSS = "timePoss"
        SCORE = "score"
