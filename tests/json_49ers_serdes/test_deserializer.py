from pathlib import Path
import unittest
import src.nfl_json_serdes.deserializer as des
import os
from stat import S_IREAD, S_IRGRP, S_IROTH
from src.nfl_json_serdes.serializer import Serializer
from tests.json_49ers_serdes.strings import ORIGINAL_GAMES_STRING

ORIGNAL_PATH = Path("./tests/test_files/ORIGINAL.json")
SINGLE_ELEMENT_PATH = Path("./tests/test_files/single_element.json")

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

    def test_reverse_string_output(self):
        deser = des.Deserializer()
        games = deser.from_file(ORIGNAL_PATH)
        actual_str = Serializer().to_string(games)
        self.assertEqual(ORIGINAL_GAMES_STRING, actual_str)
        pass

    def test_single_element(self):
        games = des.Deserializer().from_file(SINGLE_ELEMENT_PATH)
        self.assertEqual(len(games), 1)
        self.assertEqual(games[0].date, '2020-09-13')
