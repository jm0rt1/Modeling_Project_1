from src.online.client import Client

import unittest


class TestClient(unittest.TestCase):
    def test_init(self):
        _ = Client()
