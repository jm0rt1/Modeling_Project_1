
from __future__ import annotations
from pathlib import Path
from src.data.game import Game


class Serializer:
    def __init__(self):
        pass

    def to_string(self, games: list[Game]):
        pass

    def to_file(self, path: Path):
        pass
