import unittest
from dao.financial_record_service import FinancialRecordService

class TestFinancialRecord(unittest.TestCase):

    def setUp(self):
        self.service = FinancialRecordService()

    def test_add_and_get_record(self):
        record = self.service.add_financial_record(
            1, "Bonus", 5000, "Income"
        )
        self.assertEqual(record.amount, 5000)

    def test_get_invalid_record(self):
        result = self.service.get_financial_record_by_id(-1)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
