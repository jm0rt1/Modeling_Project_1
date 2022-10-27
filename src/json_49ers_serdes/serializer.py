
from __future__ import annotations
import json
from pathlib import Path
from src.data.game import Game


class Serializer:
    def __init__(self):
        pass

    def to_string(self, games: list[Game]):
        games_dicts_list = []
        for game in games:
            game_dict = game.to_dict()
            games_dicts_list.append(game_dict)

        string = json.dumps(games)

        return string

    def to_file(self, path: Path):
        pass
