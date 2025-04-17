import unittest
from ch11_testcode import city_country,Employee
"""
class TestCase(unittest.TestCase):
    def test_city(self):
        a = city_country("santiago", "chile")
        self.assertEqual(a, "Santiago,Chile")
        a = city_country("santiago", "chile",6000)
        self.assertEqual(a, "Santiago,Chile -population 6000 ")

if __name__ == '__main__':
    unittest.main()
    
"""

"""
class TestCaseEmployee(unittest.TestCase):
    def setUp(self) :
        self.employee = Employee("Liang", "Huo",  27)

    def test_assert(self):
        self.assertEqual(self.employee.first_name, "Liang")
        self.assertEqual(self.employee.last_name, "Huo")
        self.assertEqual(self.employee.salary, 27)
        self.assertEqual(self.employee.give_raise(), 77)

    def test_assertA(self):
        self.assertEqual(self.employee.first_name, "Liang")
        self.assertEqual(self.employee.last_name, "Huo")
        self.assertEqual(self.employee.salary, 27)
        self.assertEqual(self.employee.give_raise(23), 50)



if __name__ == '__main__':
    unittest.main()
"""