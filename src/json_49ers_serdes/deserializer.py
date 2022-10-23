
from __future__ import annotations
from pathlib import Path

from src.data.game import Game
import json


class Deserializer:
    def __init__(self):
        pass

    def from_string(self, json_string: str) -> list[Game]:
        data = json.loads(json_string)
        Game(data[Game.Keys.NEUTRAL], data[Game.Keys.VIS_TEAM_NAME],
             data[Game.Keys.HOME_TEAM_NAME],
             data[Game.Keys.IS_FINAL],
             data[Game.Keys.DATE],
             data[Game.Keys.HOME_STATS],
             data[Game.Keys.VIS_STATS])

        pass

    def from_file(self, path: Path) -> list[Game]:
        json_str = ""
        with open(path, "r") as fp:
            json_str = fp.read()

        return self.from_string(json_str)
