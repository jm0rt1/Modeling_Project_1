

import unittest
from src.json_49ers_serdes.deserializer import Deserializer
from src.json_49ers_serdes.serializer import Serializer
from tests.json_49ers_serdes.test_deserializer import ORIGNAL_PATH
from src.json_49ers_serdes.deserializer import Deserializer


class TestSerializer(unittest.TestCase):
    def test_init(self):
        _ = Serializer()

    def test_example(self):
        data = Deserializer().from_file(ORIGNAL_PATH)
        string = Serializer().to_string(data)
