# Testing the book.py

import pytest
from book import Book
import datetime
from unittest.mock import Mock
from unittest import TestCase


@pytest.fixture
def c():
    c = Book("book", "atef", 12345, any, 'Science')
    return c


def test_constructor(c):
    assert c.title == "book"
    assert c.auther_name == "atef"
    assert c.isbn == 12345
    assert c.status_week == datetime.date.today().isocalendar()[1]
    assert c.category == "Science"


def test_is_available(c):
    x = c.is_available()
    assert x == True


def test_borrow_book(c):
    x = c.borrow_book(1)
    assert c.status_week == datetime.date.today().isocalendar()[1] + 1
    assert x == True
    # test Exception with 0 weeks
    with pytest.raises(Exception, match="Bad value weeks"):
        c.borrow_book(0)


def test_return_book(c):
    c.return_book()
    current_week = datetime.date.today().isocalendar()[1]
    assert c.status_week == current_week


class unit_test(TestCase):

    def test_repr(self):
        constr = Book("book", "atef", 1234567891, any, 'Science')
        x = Mock(side_effect=constr)
        expected = "Book Title book\n" +\
            "Book Auther name = atef\n" +\
            "Book ISBN = 1234567891\n" +\
            "Book Category = Science\n" +\
            f"Book is available fr.o.m week# {datetime.date.today().isocalendar()[1]}"
        actual = str(x.side_effect)
        self.assertEqual(expected, actual)
