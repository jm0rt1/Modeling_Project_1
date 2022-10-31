

import enum
import unittest
from src.json_49ers_serdes.deserializer import Deserializer
from src.json_49ers_serdes.serializer import Serializer
from tests.json_49ers_serdes.test_deserializer import ORIGNAL_PATH, SINGLE_ELEMENT_PATH


class TestSerializer(unittest.TestCase):
    def test_init(self):
        _ = Serializer()

    def test_string_reversal_single(self):
        data = Deserializer().from_file(SINGLE_ELEMENT_PATH)
        string = Serializer().to_string(data)
        rev_data = Deserializer().from_string(string)

        for i, item in enumerate(data):
            a = rev_data[i] == item
            self.assertTrue(a)

    def test_string_reversal_original(self):
        data = Deserializer().from_file(ORIGNAL_PATH)
        string = Serializer().to_string(data)
        rev_data = Deserializer().from_string(string)

        for i, item in enumerate(data):
            a = rev_data[i] == item
            self.assertTrue(a)
