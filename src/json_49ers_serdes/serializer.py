
from __future__ import annotations
from copy import copy, deepcopy
import json
from pathlib import Path
from src.data.game import Game


class Serializer:
    def __init__(self):
        pass

    def to_string(self, games: list[Game]):
        # make a copy, so as not to bugger the ref
        g = deepcopy(games)
        games_dicts_list = []

        for game in g:
            game_dict = game.to_dict()
            games_dicts_list.append(game_dict)

        string = json.dumps(games_dicts_list)

        return string

    def to_file(self, path: Path):
        pass
