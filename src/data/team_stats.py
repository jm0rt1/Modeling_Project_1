
from __future__ import annotations


from dataclasses import dataclass
import datetime
import enum
from typing import Any


class TeamStats:
    def __init__(self) -> None:
        self.statIdCode: str
        self.gameCode: str
        self.teamCode: int
        self.gameDate: datetime.date
        self.rushYds: int
        self.rushAtt: int
        self.passYds: int
        self.passAtt: int
        self.passComp: int
        self.penalties: int
        self.penaltYds: int
        self.fumblesLost: int
        self.interceptionsThrown: int
        self.firstDowns: int
        self.thridDownAtt: int
        self.thirdDownConver: int
        self.fourthDownAtt: int
        self.fourthDownConver: int
        self.timePoss: int
        self.score: int

    class Keys(str, enum.Enum):
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

    @classmethod
    def from_dict(cls, a: dict[Any, Any]):
        team_stats = cls()
        team_stats.__dict__ = a
        return team_stats

    def to_dict(self):
        return self.__dict__
