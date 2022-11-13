
from __future__ import annotations
from pathlib import Path

from src.data.game import Game
import json


class Deserializer:
    def __init__(self):
        pass

    def from_string(self, json_string: str) -> list[Game]:
        """
        Convert from a json string to a list of Game objects

        Args:
            json_string (str): json string representing list[Game]

        Returns:
            list[Game]: list of Game objects represented by inputted string
        """
        data = json.loads(json_string)
        games: list[Game] = []
        if isinstance(data, dict) and "matchUpStats" in data.keys():
            data = data["matchUpStats"]  # type:ignore
        if not (isinstance(data, list)):
            RuntimeError("Data did not reduce to a list[dict[Any,Any]]")
        for item in data:  # type:ignore
            game = Game.from_dict(item)  # type:ignore
            games.append(game)
        return games

    def from_file(self, path: Path) -> list[Game]:
        """
        take file input path and convert to a list of Games

        Args:
            path (Path): path to file with JSON String

        Returns:
            list[Game]: list of Games represented by string at path
        """
        json_str = ""
        with open(path, "r") as fp:
            json_str = fp.read()

        return self.from_string(json_str)
