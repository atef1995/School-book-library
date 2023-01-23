# Atef Moazzen
# Book library project

from book import Book
import datetime


class Meny:
    borrower_dict = {"borrowers": [
        {
            "name": "Test person",
            "id": 1,
            "teacher": True,
            "student": False,
            "borrowed books": [123111, 123123],
            "funds collected": 30
        },
        {
            "name": "Tester2",
            "id": 2,
            "teacher": False,
            "student": True,
            "borrowed books": [123111],
            "funds collected": 10
        }
    ]}
    book_dict = {
        "Science": [{
            "name": "test",
            "ISBN": 123111,
            "author": "test_author",
            "status week": 1
        }],
        "Literature": [{
            "name": "test2",
            "ISBN": 123123,
            "author": "test_author",
            "status week": 1
        }],
        "Entertainment": [{
            "name": "test2",
            "ISBN": 131313,
            "author": "test_author",
            "status week": 1
        }],
    }

    def __init__(self) -> None:
        menu_list = "1.Adding new borrower\n" +\
            "2.Add a new book\n" +\
            "3.Borrow or rent out a book to teacher or to student\n" +\
            "4.Return a book and print out the charges applied.\n" +\
            "5.Print out in the terminal all books\n" +\
            "6.Print out a library report\n"
        print(menu_list)

    def menu(self, val):
        self.val = val
        if self.val == "1":
            self.add_borrower()
        elif self.val == "2":
            self.add_new_book()
        elif self.val == "3":
            self.rent_book()
        elif self.val == "4":
            self.rent_book()
        elif self.val == "5":
            print(self.book_dict)
        elif self.val == "6":
            self.library_report()
        elif self.val == "7":
            quit()

    def add_borrower(self):
        name = input("Enter borrowers name:")
        i_d = int(input("Enter id number:"))
        teacher_or_student = input("Student or teacher:")
        if teacher_or_student == "t":
            is_teacher = True
            is_student = False
            self.create_borrower_dictionary(name, i_d, is_teacher, is_student)
        else:
            is_teacher = False
            is_student = True
            self.create_borrower_dictionary(name, i_d, is_teacher, is_student)

    def create_borrower_dictionary(self, name, i_d, is_teacher, is_student):
        borrower = {
            "name": name,
            "id": i_d,
            "teacher": is_teacher,
            "student": is_student,
            "borrowed books": [],
            "funds collected": 0,
        }

        self.borrower_dict["borrowers"].append(borrower)

    def add_new_book(self):
        category = input("Book category:")
        name = input("book name:")
        isbn = int(input("ISBN:"))
        author = input("Author:")
        new_book_dictionary = {
            "Name": name,
            "ISBN": isbn,
            "Author": author,
            "status week": datetime.date.today().isocalendar()[1]
        }
        self.book_dict[category].append(new_book_dictionary)

    def rent_book(self):
        category = input("Book category:").capitalize()
        isbn = int(input("Enter book ISBN:"))
        borrowers_id = int(input("Enter borrower id number:"))
        for i in range(len(self.book_dict[category])):
            if isbn == self.book_dict[category][i].get("ISBN"):
                if self.val == '3':
                    self.send_book_info_to_book_class(
                        category, i, borrowers_id)
                elif self.val == '4':
                    self.return_book(borrowers_id, isbn, category, i)

    def send_book_info_to_book_class(self, category, i, borrowers_id):
        status_week = self.book_dict[category][i].get("status week")
        name = self.book_dict[category][i].get("name")
        isbn = self.book_dict[category][i].get("ISBN")
        author = self.book_dict[category][i].get("author")
        b = Book(name, author, isbn, status_week, category)
        b.borrow_book(4)
        return_week = b.status_week
        self.book_dict[category][i]["status week"] = return_week
        print(f"the book should be returned in week:{return_week}")
        for x in range(len(self.borrower_dict["borrowers"])):
            if borrowers_id == self.borrower_dict["borrowers"][x].get("id"):
                self.borrower_dict["borrowers"][x]["borrowed books"].append(
                    isbn)

    def return_book(self, borrowers_id, isbn, category, i):
        for i in range(len(self.borrower_dict["borrowers"])):
            if borrowers_id == self.borrower_dict["borrowers"][i].get("id"):
                borrower = self.borrower_dict["borrowers"][i]
                self.borrower_dict["borrowers"][i]["borrowed books"].remove(
                    isbn)
                if borrower.get("teacher") == True:
                    if category == "Science":
                        self.charges_func(category, charges=15)
                    elif category == "Literature":
                        self.charges_func(category, charges=10)
                    else:
                        self.charges_func(category, charges=0)

                elif borrower["student"] == True:
                    if category == "Science":
                        self.charges_func(category, charges=5)
                    else:
                        self.charges_func(category, charges=0)

    def charges_func(self, category, charges, i=0):
        status_week = self.book_dict[category][0].get("status week")
        current_week = datetime.date.today().isocalendar()[1]
        total = int((status_week - current_week)*charges)
        print(f"Should pay {total}")

    def library_report(self):
        total_funds = []
        for i in range(len(self.borrower_dict["borrowers"])):
            borrowed_books = len(
                self.borrower_dict["borrowers"][i]["borrowed books"])
            funds_collected = self.borrower_dict["borrowers"][i]["funds collected"]
            total_funds.append(funds_collected)
            borrowed_books_print = f"borrowed books: {borrowed_books}"
            total_funds_print = f"funds collected:$ {sum(total_funds)}"
            total_books = self.book_dict["Science"].__len__(
            ) + self.book_dict["Literature"].__len__() + self.book_dict["Entertainment"].__len__()
            print(
                f"{borrowed_books_print} {total_funds_print} Total books:{total_books}")
