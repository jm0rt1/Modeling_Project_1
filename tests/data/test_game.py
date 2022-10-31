

import unittest

from src.data.game import Game
from src.json_49ers_serdes.deserializer import Deserializer
from tests.json_49ers_serdes.test_deserializer import SINGLE_ELEMENT_PATH


class TestGame(unittest.TestCase):
    def test_init(self):
        _ = Game()

    def test_user_friendly_print(self):
        "Not a functional test, just for viewing -- always passes if no error"
        games = Deserializer().from_file(SINGLE_ELEMENT_PATH)
        games[0].print()
