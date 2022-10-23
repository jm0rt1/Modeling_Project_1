import io
from src.main import main

import unittest
import unittest.mock


class TestMain(unittest.TestCase):
    def test_no_errors(self):
        main()

    def test_main_output(self):
        @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
        def assert_stdout(expected_output: str, mock_stdout: io.StringIO):
            main()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
        assert_stdout('hello world\n')
