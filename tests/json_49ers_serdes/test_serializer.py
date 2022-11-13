

import enum
import os
from pathlib import Path
import unittest
from src.nfl_json_serdes.deserializer import Deserializer
from src.nfl_json_serdes.serializer import Serializer
from tests.json_49ers_serdes.test_deserializer import ORIGNAL_PATH, SINGLE_ELEMENT_PATH

TEST_OUT_PATH = Path("./tests/test_files/test_output.json")


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

    def test_saving_to_file(self):
        data = Deserializer().from_file(ORIGNAL_PATH)
        Serializer().to_file(data, TEST_OUT_PATH)
        with open(ORIGNAL_PATH, "r") as fp:
            og_data = fp.read()

        with open(TEST_OUT_PATH, "r") as fp:
            test_data = fp.read()
        os.remove(TEST_OUT_PATH)
        self.assertEqual(og_data, test_data)
