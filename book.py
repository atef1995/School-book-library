import datetime


class Book():
    categories = {'Literature', 'Science', 'Entertainment'}

    def __init__(self, title, Auther_name, ISBN, status_week, category) -> None:
        self.title = title
        self.auther_name = Auther_name
        self.isbn = ISBN
        self.status_week = datetime.date.today().isocalendar()[1]
        # Check category
        if category in self.categories:
            self.category = category
        else:
            raise ValueError("Bad input Book Category")

    @classmethod
    def literature_book(cls, title, Auther_name, ISBN, status_week):
        return cls(title, Auther_name, ISBN,
                   datetime.date.today().isocalendar()[1], 'Literature')

    @classmethod
    def Science_book(cls, title, Auther_name, ISBN, status_week):
        return cls(title, Auther_name, ISBN,
                   datetime.date.today().isocalendar()[1], 'Science')

    @classmethod
    def Entertainment_book(cls, title, Auther_name, ISBN, status_week):
        return cls(title, Auther_name, ISBN,
                   datetime.date.today().isocalendar()[1], 'Entertainment')

    def __repr__(self) -> str:
        out_put = f"Book Title {self.title}\n" +\
                  f"Book Auther name = {self.auther_name}\n" +\
                  f"Book ISBN = {self.isbn}\n" +\
                  f"Book Category = {self.category}\n"
        current_week = datetime.date.today().isocalendar()[1]
        if self.status_week > current_week:
            out_put += f"Book is borrowed till week # {self.status_week}"
        else:
            out_put += f"Book is available fr.o.m week# {self.status_week}"
        return out_put

    def is_available(self):
        current_week = datetime.date.today().isocalendar()[1]
        if self.status_week > current_week:
            return False
        else:
            return True

    def borrow_book(self, weeks):
        current_week = datetime.date.today().isocalendar()[1]
        if self.is_available() and weeks > 0:
            if current_week + weeks < 53:
                self.status_week = current_week + weeks
                return True
            else:
                self.status_week = current_week + weeks - 52
                return True
        else:
            raise Exception("Bad value weeks")

    def return_book(self):
        current_week = datetime.date.today().isocalendar()[1]
        self.status_week = current_week
