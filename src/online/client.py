from __future__ import annotations
import enum
import urllib.request
from src.json_49ers_serdes.deserializer import Deserializer
from src.data.game import Game
import re

ENCODING = "utf-8"


class StatsTypes(str, enum.Enum):
    TEAM_STATS = "teamStats"


class TeamNamesIntEnum(enum.IntEnum):
    """
    Ordered -- Order matches the numbers for the teams in the API
    """
    CARDINALS = 1
    FALCONS = 2
    RAVENS = 3
    BILLS = 4
    PANTHERS = 5
    BEARS = 6
    BROWNS = 7
    COWBOYS = 8
    BRONCOS = 9
    LIONS = 10
    PACKERS = 11
    GIANTS = 12
    COLTS = 13
    JAGUARS = 14
    CHIEFS = 15
    DOLPHINS = 16
    VIKINGS = 17
    PATRIOTS = 18
    SAINTS = 19
    JETS = 20
    RAIDERS = 21
    EAGLES = 22
    STEELERS = 23
    CHARGERS = 24
    SEAHAWKS = 25
    T_49ERS = 26
    RAMS = 27
    BUCCANEERS = 28
    TITANS = 29
    WASHINGTON = 30
    BENGALS = 31
    TEXANS = 32

    @staticmethod
    def get_str_name(team_number: int):
        """
        team number ranges from 1-32

        Args:
            team_number (int): number of the team to get the string for

        Returns:
            str: capitalized name
        """
        if not (1 <= team_number <= 32):
            raise RuntimeError(
                f"team number ranges from 1-32, team_number = {team_number}")

        index = team_number - 1
        teams_list = list(TeamNamesIntEnum)
        item = teams_list[index]
        item_str = str(item)
        dot_idx = item_str.find(".")
        name_all_caps = item_str[dot_idx+1:]
        name_lower = name_all_caps.lower()
        if name_lower[0].isalpha():
            name_capped = name_lower.capitalize()
            return name_capped

        return name_lower

    @staticmethod
    def get_team_number(team_name_str: str) -> TeamNamesIntEnum:
        for item in list(TeamNamesIntEnum):
            name = TeamNamesIntEnum.get_str_name(item.value)

            if team_name_str.lower() == name.lower():
                return item
        raise RuntimeError("Could not find a number for entered team name")


class URLs(str, enum.Enum):
    @staticmethod
    def NFL_SEARCH_HANDLER(stats_type: StatsTypes, season: int, teamName: TeamNamesIntEnum):
        value = f"https://sports.snoozle.net/search/nfl/searchHandler?fileType=inline&statType={stats_type}&season={season}&teamName={teamName}"
        return value


class Client():
    def __init__(self) -> None:
        pass
        contents = urllib.request.urlopen(
            URLs.NFL_SEARCH_HANDLER(StatsTypes.TEAM_STATS, 2020, TeamNamesIntEnum.BEARS)).read()
        contents = str(contents, ENCODING)

        Deserializer().from_string(contents)

    @staticmethod
    def get_team_stats_by_number(year: int, team_number: TeamNamesIntEnum) -> list[Game]:
        contents = urllib.request.urlopen(
            URLs.NFL_SEARCH_HANDLER(StatsTypes.TEAM_STATS, year, team_number)).read()
        contents = str(contents, ENCODING)
        return Deserializer().from_string(contents)

    @staticmethod
    def get_team_stats_by_name(year: int, team_name: str) -> list[Game]:
        team_number = TeamNamesIntEnum.get_team_number(team_name)
        return Client.get_team_stats_by_number(year, team_number)
