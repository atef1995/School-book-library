# unit testing
from main_app import Meny
from unittest import TestCase
from unittest.mock import patch


class test_app(TestCase):
    def test_print_menu(self):
        with patch("builtins.print") as mocked_print:
            Meny().__init__()
            expected = "1.Adding new borrower\n" +\
                "2.Add a new book\n" +\
                "3.Borrow or rent out a book to teacher or to student\n" +\
                "4.Return a book and print out the charges applied.\n" +\
                "5.Print out in the terminal all books\n" +\
                "6.Print out a library report\n"
            mocked_print.assert_called_with(expected)

    def test_print_book_dict(self):
        m = Meny()
        with patch("builtins.print") as mocked_print:
            m.menu('5')
            expected = {'Science': [{'name': 'test', 'ISBN': 123111, 'author': 'test_author', 'status week': 1}], 'Literature': [
                {'name': 'test2', 'ISBN': 123123, 'author': 'test_author', 'status week': 1}], 'Entertainment': [{'name': 'test2', 'ISBN': 131313, 'author': 'test_author', 'status week': 1}]}
            mocked_print.assert_called_with(expected)

    def test_library_report(self):
        m = Meny()
        with patch("builtins.print") as mocked_print:
            m.menu('6')
            expected = "borrowed books: 1 funds collected:$ 40 Total books:3"
            mocked_print.assert_called_with(expected)
