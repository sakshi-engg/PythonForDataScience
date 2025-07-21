import unittest
from dao.payroll_service import PayrollService
from exception.payroll_generation_exception import PayrollGenerationException

class TestPayroll(unittest.TestCase):

    def setUp(self):
        self.service = PayrollService()

    def test_generate_and_get_payroll(self):
        payroll = self.service.generate_payroll(1, '2023-01-01', '2023-01-31')
        self.assertGreater(payroll.net_salary, 0)

    def test_get_payroll_invalid_id(self):
        result = self.service.get_payroll_by_id(-1)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
