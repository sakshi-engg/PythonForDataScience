import unittest
from dao.employee_service import EmployeeService
from entity.employee import Employee
from exception.employee_not_found_exception import EmployeeNotFoundException

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.service = EmployeeService()

    def test_add_and_get_employee(self):
        emp = Employee(None, "Test", "User", "1990-01-01", "Male", "testuser@example.com",
                       "9999999999", "Test Address", "Engineer", "2023-01-01", None)
        self.service.add_employee(emp)
        fetched_emp = self.service.get_employee_by_id(emp.employee_id)
        self.assertEqual(fetched_emp.first_name, "Test")

    def test_employee_not_found(self):
        with self.assertRaises(EmployeeNotFoundException):
            self.service.get_employee_by_id(99999)  # Assuming this ID doesn't exist

if __name__ == '__main__':
    unittest.main()
