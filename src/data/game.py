
from __future__ import annotations


import enum
from typing import Any
from src.data.team_stats import TeamStats


class Game:
    def __init__(self) -> None:

        self.neutral: bool
        self.visTeamName: str
        self.visStats: TeamStats
        self.homeStats: TeamStats
        self.isFinal: bool
        self.date: str
        self.homeTeamName: str

    class Keys(str, enum.Enum):
        NEUTRAL = "neutral"
        VIS_TEAM_NAME = "visTeamName"
        VIS_STATS = "visStats"
        HOME_STATS = "homeStats"
        IS_FINAL = "isFinal"
        DATE = "date"
        HOME_TEAM_NAME = "homeTeamName"

    @classmethod
    def from_raw_data(cls, neutral: bool,
                      visTeamName: str,
                      visStats: TeamStats,
                      homeStats: TeamStats,
                      isFinal: bool,
                      date: str,
                      homeTeamName: str):

        g = cls()
        g.neutral = neutral
        g.visTeamName = visTeamName
        g.visStats = visStats
        g.homeStats = homeStats
        g.isFinal = isFinal
        g.date = date
        g.homeTeamName = homeTeamName
        return g

    @classmethod
    def from_dict(cls, a: dict[Any, Any]):
        """ 
        Uses the 'payload method' to quickly load all of the data from the JSON dict into this object.

        Keys from the JSON are intended to match the attribute names in this object,
        and will not follow Python's snake case convention.
        """
        a[Game.Keys.HOME_STATS] = TeamStats.from_dict(a[Game.Keys.HOME_STATS])
        a[Game.Keys.VIS_STATS] = TeamStats.from_dict(a[Game.Keys.VIS_STATS])
        game = cls()
        game.__dict__ = a
        return game

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Game):
            raise RuntimeError("Cannot compare a unknown object to type Game")
        for key in __o.__dict__.keys():
            if isinstance(__o.__dict__[key], TeamStats):
                for ts_key in __o.__dict__[key].__dict__.keys():
                    try:
                        a = self.__dict__[
                            key].__dict__[ts_key] == __o.__dict__[key].__dict__[ts_key]
                        if not a:
                            return False
                    except KeyError:
                        return False
            else:
                a = self.__dict__[
                    key] == __o.__dict__[key]
                if not a:
                    return False
        return True

    def to_dict(self) -> dict[Any, Any]:
        data = self.__dict__
        data[Game.Keys.HOME_STATS] = data[Game.Keys.HOME_STATS].to_dict()
        data[Game.Keys.VIS_STATS] = data[Game.Keys.VIS_STATS].to_dict()
        return data

    def print(self, ):
        friendly_string = f"{self.visTeamName}\tAt\t{self.homeTeamName}  on {self.date}\n\n"
        friendly_string += f"Stats by team (away - home):\n\n"
        friendly_string += f"Score:\t\t\t  {self.visStats.score} - {self.homeStats.score}\n"
        friendly_string += f"Possession Time:\t  {self.visStats.timePoss} - {self.homeStats.timePoss}\n"
        friendly_string += f"First Downs:\t\t  {self.visStats.firstDowns} - {self.homeStats.firstDowns}\n"

        friendly_string += f"Fourth Down Att:\t  {self.visStats.fourthDownAtt} - {self.homeStats.fourthDownAtt}\n"
        friendly_string += f"Fourth Down conversion:\t  {self.visStats.fourthDownConver} - {self.homeStats.fourthDownConver}\n"
        friendly_string += f"Third Down Att:\t\t  {self.visStats.thridDownAtt} - {self.homeStats.thridDownAtt}\n"
        friendly_string += f"Third Down conversion:\t  {self.visStats.thirdDownConver} - {self.homeStats.thirdDownConver}\n"

        friendly_string += f"Fumbles Lost:\t\t  {self.visStats.fumblesLost} - {self.homeStats.fumblesLost}\n"

        friendly_string += f"Rushing Yds:\t\t  {self.visStats.rushYds} - {self.homeStats.rushYds}\n"
        friendly_string += f"Passing Yds:\t\t  {self.visStats.passYds} - {self.homeStats.passYds}\n"

        friendly_string += f"Pass Att:\t\t  {self.visStats.passAtt} - {self.homeStats.passAtt}\n"
        friendly_string += f"Rushing Att:\t\t  {self.visStats.rushAtt} - {self.homeStats.rushAtt}\n"

        friendly_string += f"Passes Complete:\t  {self.visStats.passComp} - {self.homeStats.passComp}\n"
        friendly_string += f"Interceptions Thrown:\t  {self.visStats.interceptionsThrown} - {self.homeStats.interceptionsThrown}\n"

        friendly_string += f"Penalties:\t\t  {self.visStats.penalties} - {self.homeStats.penalties}\n"
        friendly_string += f"Penalty Yards:\t\t  {self.visStats.penaltYds} - {self.homeStats.fourthDownConver}\n\n"
        friendly_string += f" -------------------------------\n\n"
        friendly_string += f"Neutral:\t {self.neutral}\n"
        friendly_string += f"Is Final:\t {self.isFinal}\n"

        print(friendly_string)
