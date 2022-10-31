
from __future__ import annotations
from copy import deepcopy
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
            games_dicts_list.append(game_dict)  # type:ignore

        string = json.dumps(games_dicts_list, indent=4)
        return string

    def to_file(self, games: list[Game], path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        json_str = self.to_string(games)
        with open(path, "w") as fp:
            fp.write(json_str)
