from pathlib import Path
import unittest
import src.json_49ers_serdes.deserializer as des
from src.data.game import Game
import os
from stat import S_IREAD, S_IRGRP, S_IROTH
from tests.json_49ers_serdes.strings import GAMES_STRING

ORIGNAL_PATH = Path("./tests/test_files/ORIGINAL.json")


os.chmod(ORIGNAL_PATH, S_IREAD | S_IRGRP | S_IROTH)


class TestDeserializer(unittest.TestCase):
    def test_init(self):
        _ = des.Deserializer()

    def test_file_load(self):
        deser = des.Deserializer()
        games = deser.from_file(ORIGNAL_PATH)

        actual_games_length = len(games)
        expected_games_length = 16
        self.assertEqual(actual_games_length, expected_games_length)

        actual_str = str(games)
        self.assertEqual(GAMES_STRING, actual_str)
        pass
