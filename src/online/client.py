import enum
import urllib.request
from src.json_49ers_serdes.deserializer import Deserializer


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


class URLs(str, enum.Enum):
    @staticmethod
    def NFL_SEARCH_HANDLER(stats_type: StatsTypes, season: int, teamName: TeamNames):
        value = f"https://sports.snoozle.net/search/nfl/searchHandler?fileType=inline&statType={stats_type}&season={season}&teamName={teamName}"
        return value


class Client():
    def __init__(self) -> None:
        pass
        contents = urllib.request.urlopen(
            URLs.NFL_SEARCH_HANDLER(StatsTypes.TEAM_STATS, 2020, TeamNames.BEARS)).read()
        contents = str(contents, "utf-8")

        Deserializer().from_string(contents)
