# System Testing

from main_app import Meny
from unittest import TestCase
from unittest.mock import patch
import datetime


class test_app(TestCase):
    def test_add_borrower(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('a', 123, 't')
            Meny().menu('1')
            self.assertIn({"name": 'a',
                           "id": 123,
                           "teacher": True,
                           "student": False,
                           "borrowed books": [],
                           "funds collected": 0, }, Meny.borrower_dict["borrowers"]
                          )

    def test_add_new_book(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Science', 'Test1', 121212, 'Tester1')
            Meny().menu('2')
            self.assertIn({
                "Name": 'Test1',
                "ISBN": 121212,
                "Author": 'Tester1',
                "status week": datetime.date.today().isocalendar()[1]
            }, Meny.book_dict["Science"]
            )

    def test_return_book(self):
        m = Meny()
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Literature', 123123, 1)
            with patch("builtins.print") as mocked_print:
                m.menu('4')
                mocked_print.assert_called()
                expected = "Should pay 0"
                mocked_print.assert_called_with(expected)
