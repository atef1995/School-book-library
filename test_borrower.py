from borrower import Borrower
from unittest import TestCase
from unittest.mock import Mock


class Test(TestCase):
    def test_repr(self):
        const = Borrower(name="Tester1", id=11223344,
                         is_student=True, is_teacher=False)
        m = Mock(side_effect=const)
        expected = f"Borrower Name: {const.b_name}\n" +\
            f"Borrower ID: {const.b_id}\n" +\
            "Borrower is Student"
        actual = str(m.side_effect)
        self.assertEqual(expected, actual)

    def test_teacher_repr(self):
        const_teacher = Borrower(name="Tester1", id=1122344,
                                 is_student=False, is_teacher=True)
        m_2 = Mock(side_effect=const_teacher)
        expected2 = f"Borrower Name: {const_teacher.b_name}\n" +\
            f"Borrower ID: {const_teacher.b_id}\n" +\
            "Borrower is Teacher"
        actual2 = str(m_2.side_effect)
        self.assertEqual(expected2, actual2)

    def test_constructor(self):
        const = Borrower(name="Tester", id=112233,
                         is_student=True, is_teacher=False)
        assert const.b_name == "Tester"
        assert const.b_id == 112233
        assert const.is_student == True
        assert const.is_teacher == False
