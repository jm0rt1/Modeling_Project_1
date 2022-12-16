from __future__ import annotations
import enum
import urllib.request
from src.nfl_json_serdes.deserializer import Deserializer
from src.data.game import Game

ENCODING = "utf-8"


class StatsTypes(str, enum.Enum):
    """
    strings that may be used to populate the "statType" field in
    the URLs.NFL_SEARCH_HANDLER's GET request to sports.snoozle.net
    """
    TEAM_STATS = "teamStats"


class TeamNamesIntEnum(enum.IntEnum):
    """
    Ordered -- Order matches the numbers for the
    teams in thesports.snoozle.net API for the field teamName.
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
        if name_lower.startswith("t_"):
            name_lower = name_lower.replace("t_", "")
        if name_lower[0].isalpha():
            name_capped = name_lower.capitalize()
            return name_capped

        return name_lower

    @staticmethod
    def get_team_number(team_name_str: str) -> TeamNamesIntEnum:
        """
        Convert string name to number

        Args:
            team_name_str (str): string name that should be converted to its number

        Raises:
            RuntimeError: Could not find a number for entered team name

        Returns:
            TeamNamesIntEnum: integer enum element representing the string team name
        """
        for item in list(TeamNamesIntEnum):
            name = TeamNamesIntEnum.get_str_name(item.value)

            if team_name_str.lower() == name.lower():
                return item
        raise RuntimeError("Could not find a number for entered team name")

    @staticmethod
    def print_all_names_numbered() -> str:
        """
        print all of the names numbered out in the format "{number}: {name}\n..."

        Returns:
            str: "{number}: {name}\n..." 
        """
        return_str = ""
        for item in list(TeamNamesIntEnum):
            return_str += f"{item.value}: {TeamNamesIntEnum.get_str_name(item.value)}\n"

        return return_str

    @staticmethod
    def list_names() -> list[str]:
        names: list[str] = []
        for item in list(TeamNamesIntEnum):
            names.append(TeamNamesIntEnum.get_str_name(item.value))
        return names


class URLs(str, enum.Enum):
    """
    Builds URLs dynamically, and enumerates static URLs
    """
    @staticmethod
    def NFL_SEARCH_HANDLER(stats_type: StatsTypes, season: int, teamName: TeamNamesIntEnum):
        """
        based on example URL https://sports.snoozle.net/search/nfl/searchHandler?fileType=inline&statType=teamStats&season=2020&teamName=26

        Args:
            stats_type (StatsTypes): type of stat to get
            season (int): season year
            teamName (TeamNamesIntEnum): team name parameter (an integer to the API)

        Returns:
            _type_: _description_
        """
        value = f"https://sports.snoozle.net/search/nfl/searchHandler?fileType=inline&statType={stats_type}&season={season}&teamName={teamName}"
        return value


class SnoozelSportsClient():
    """
    sports.snoozle.net API client
    """
    @staticmethod
    def get_team_stats_by_number(year: int, team_number: TeamNamesIntEnum) -> list[Game]:
        """
        get a list of Game objects using the year and team number

        Args:
            year (int): season year
            team_number (TeamNamesIntEnum): team number in API

        Returns:
            list[Game]: list of Game objects retrieved
        """
        contents = urllib.request.urlopen(
            URLs.NFL_SEARCH_HANDLER(StatsTypes.TEAM_STATS, year, team_number)).read()
        contents = str(contents, ENCODING)
        return Deserializer().from_string(contents)

    @staticmethod
    def get_team_stats_by_name(year: int, team_name: str) -> list[Game]:
        """
        get a list of Game objects using the year and team name

        Args:
            year (int): season year
            team_name (TeamNamesIntEnum): string team name

        Returns:
            list[Game]: list of Game objects retrieved
        """
        team_number = TeamNamesIntEnum.get_team_number(team_name)
        return SnoozelSportsClient.get_team_stats_by_number(year, team_number)
