from pathlib import Path
import unittest
import src.json_49ers_serdes.deserializer as des


class TestDeserializer(unittest.TestCase):
    def test_init(self):
        _ = des.Deserializer()

    def test_file_load(self):
        deser = des.Deserializer()
        deser.from_file(Path("./tests/test_files/ORIGINAL.json"))
