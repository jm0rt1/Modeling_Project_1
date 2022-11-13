import enum
from src.online.client import Client, TeamNamesIntEnum

import unittest


class NameStrs(str, enum.Enum):
    CARDINALS = "Cardinals"
    FALCONS = "Falcons"
    RAVENS = "Ravens"
    BILLS = "Bills"
    PANTHERS = "Panthers"
    BEARS = "Bears"
    BROWNS = "Browns"
    COWBOYS = "Cowboys"
    BRONCOS = "Broncos"
    LIONS = "Lions"
    PACKERS = "Packers"
    GIANTS = "Giants"
    COLTS = "Colts"
    JAGUARS = "Jaguars"
    CHIEFS = "Chiefs"
    DOLPHINS = "Dolphins"
    VIKINGS = "Vikings"
    PATRIOTS = "Patriots"
    SAINTS = "Saints"
    JETS = "Jets"
    RAIDERS = "Raiders"
    EAGLES = "Eagles"
    STEELERS = "Steelers"
    CHARGERS = "Chargers"
    SEAHAWKS = "Seahawks"
    T_49ERS = "T_49ers"
    RAMS = "Rams"
    BUCCANEERS = "Buccaneers"
    TITANS = "Titans"
    WASHINGTON = "Washington"
    BENGALS = "Bengals"
    TEXANS = "Texans"


class TestClient(unittest.TestCase):
    def test_init(self):
        _ = Client()

    def test_get_games_by_number(self):

        for number in TeamNamesIntEnum:
            data = Client.get_team_stats_by_number(2020, number)
            self.assertGreaterEqual(len(data), 15)
            pass

    def test_get_games_by_name(self):

        for _, item in enumerate(NameStrs):
            data = Client.get_team_stats_by_name(2020, item.value)
            self.assertGreaterEqual(len(data), 15)


class TestTeamNamesIntEnum(unittest.TestCase):
    def test_str_names(self):
        for i in range(1, 33):
            name = TeamNamesIntEnum.get_str_name(i)
            self.assertEqual(list(NameStrs)[i-1].value,  name)

    def test_get_team_number(self):
        for i, item in enumerate(NameStrs):
            name = item.value
            result = TeamNamesIntEnum.get_team_number(name)
            self.assertEqual(result, i+1)
