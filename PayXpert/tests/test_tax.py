import unittest
from dao.tax_service import TaxService
from exception.tax_calculation_exception import TaxCalculationException

class TestTax(unittest.TestCase):

    def setUp(self):
        self.service = TaxService()

    def test_calculate_tax(self):
        tax = self.service.calculate_tax(1, 2023)
        self.assertGreaterEqual(tax.tax_amount, 0)

    def test_get_tax_by_invalid_id(self):
        result = self.service.get_tax_by_id(-1)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
