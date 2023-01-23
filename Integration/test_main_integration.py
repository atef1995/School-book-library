# integration testing
from main_app import Meny
from unittest import TestCase
from unittest.mock import patch
import datetime


class test_app(TestCase):
    def test_rent_book(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Science', 123111, 1)
            m = Meny()
            with patch("builtins.print") as mocked_print:
                m.menu('3')
                expected = "the book should be returned in week:5"
                mocked_print.assert_called_with(expected)
