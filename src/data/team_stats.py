
from __future__ import annotations


import enum
from typing import Any


class TeamStats:
    """
    Yes, "thridDownAtt" is a typo in the JSON file so I kept the typo consistent.
    Will not be writing getters/setters for this class to reduce clutter. Utilize dot operator instead
    """

    def __init__(self) -> None:
        self.statIdCode: str
        self.gameCode: str
        self.teamCode: int
        self.gameDate: str
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
        JSON Keys
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
        """
        Generate a TeamStats from a dictionary using the payload method

        Args:
            a (dict[Any, Any]): dictionary input

        Returns:
            TeamStats: generated from dict
        """
        team_stats = cls()
        team_stats.__dict__ = a
        return team_stats

    def to_dict(self):
        """
        Convert this TeamStats into a dictionary

        Returns:
            dict: dictionary output
        """
        return self.__dict__

    @classmethod
    def from_raw_data(cls, statIdCode: str, gameCode: str,
                      teamCode: int, gameDate: str, rushYds: int,
                      rushAtt: int, passYds: int, passAtt: int,
                      passComp: int, penalties: int, penaltYds: int,
                      fumblesLost: int, interceptionsThrown: int, firstDowns: int,
                      thridDownAtt: int, thirdDownConver: int, fourthDownAtt: int,
                      fourthDownConver: int, timePoss: int, score: int):
        """
        Alternative constructor

        Args:
            statIdCode (str): statIdCode input value
            gameCode (str): gameCode input value
            teamCode (int): teamCode input value
            gameDate (str): gameDate input value
            rushYds (int): rushYds input value
            rushAtt (int): rushAtt input value
            passYds (int): passYds input value
            passAtt (int): passAtt input value
            passComp (int): passComp input value
            penalties (int): penalties input value
            penaltYds (int): penaltYds input value
            fumblesLost (int): fumblesLost input value
            interceptionsThrown (int): interceptionsThrown input value
            firstDowns (int): firstDowns input value
            thridDownAtt (int): thridDownAtt input value
            thirdDownConver (int): thirdDownConver input value
            fourthDownAtt (int): fourthDownAtt input value
            fourthDownConver (int): fourthDownConver input value
            timePoss (int): timePoss input value
            score (int): score input value

        Returns:
            TeamStats: from raw data
        """

        ts = cls()
        ts.statIdCode = statIdCode
        ts.gameCode = gameCode
        ts.teamCode = teamCode
        ts.gameDate = gameDate
        ts.rushYds = rushYds
        ts.rushAtt = rushAtt
        ts.passYds = passYds
        ts.passAtt = passAtt
        ts.passComp = passComp
        ts.penalties = penalties
        ts.penaltYds = penaltYds
        ts.fumblesLost = fumblesLost
        ts.interceptionsThrown = interceptionsThrown
        ts.firstDowns = firstDowns
        ts.thridDownAtt = thridDownAtt
        ts.thirdDownConver = thirdDownConver
        ts.fourthDownAtt = fourthDownAtt
        ts.fourthDownConver = fourthDownConver
        ts.timePoss = timePoss
        ts.score = score
        return ts

    @classmethod
    def from_console_input(cls) -> TeamStats:
        """
        Ask the user for the input data from the console, very rudimentary/no error checking

        Returns:
            TeamStats: generated from user input
        """
        statIdCode = input("(str) statIdCode =")
        gameCode = input("(str) gameCode =")
        teamCode = int(input("(int) teamCode ="))
        gameDate = input("(str) gameDate =")
        rushYds = int(input("(int) rushYds ="))
        rushAtt = int(input("(int) rushAtt ="))
        passYds = int(input("(int) passYds ="))
        passAtt = int(input("(int) passAtt ="))
        passComp = int(input("(int) passComp ="))
        penalties = int(input("(int) penalties ="))
        penaltYds = int(input("(int) penaltYds ="))
        fumblesLost = int(input("(int) fumblesLost ="))
        interceptionsThrown = int(input("(int) interceptionsThrown ="))
        firstDowns = int(input("(int) firstDowns ="))
        thridDownAtt = int(input("(int) thridDownAtt ="))
        thirdDownConver = int(input("(int) thirdDownConver ="))
        fourthDownAtt = int(input("(int) fourthDownAtt ="))
        fourthDownConver = int(input("(int) fourthDownConver ="))
        timePoss = int(input("(int) timePoss ="))
        score = int(input("(int) score ="))
        return cls.from_raw_data(statIdCode,
                                 gameCode,
                                 teamCode,
                                 gameDate,
                                 rushYds,
                                 rushAtt,
                                 passYds,
                                 passAtt,
                                 passComp,
                                 penalties,
                                 penaltYds,
                                 fumblesLost,
                                 interceptionsThrown,
                                 firstDowns,
                                 thridDownAtt,
                                 thirdDownConver,
                                 fourthDownAtt,
                                 fourthDownConver,
                                 timePoss,
                                 score)
