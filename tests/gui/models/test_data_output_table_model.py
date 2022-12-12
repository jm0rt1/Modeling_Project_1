import unittest
from src.gui.models.game_display_table_model import GameDisplayTableModel
from src.nfl_json_serdes.deserializer import Deserializer
from tests.json_49ers_serdes.test_deserializer import ORIGNAL_PATH


class TestDataOutputTableModel(unittest.TestCase):
    def test_init(self):
        GameDisplayTableModel()

    def test_populate(self):
        gdtm = GameDisplayTableModel()
        games = Deserializer().from_file(ORIGNAL_PATH)

        gdtm.populate(games[1])
