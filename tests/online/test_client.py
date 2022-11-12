import enum
from src.online.client import Client, TeamNamesIntEnum

import unittest


class TestClient(unittest.TestCase):
    def test_init(self):
        _ = Client()


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


class TestTeamNamesIntEnum(unittest.TestCase):
    def test_str_names(self):
        for i in range(1, 33):
            name = TeamNamesIntEnum.get_str_name(i)
            self.assertEqual(list(NameStrs)[i-1].value,  name)
