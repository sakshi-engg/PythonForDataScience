from dao.ifinancial_record_service import IFinancialRecordService
from util.db_conn_util import DBConnUtil

class FinancialRecordService(IFinancialRecordService):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    def add_financial_record(self, employee_id, description, amount, record_type):
        pass

    def get_financial_record_by_id(self, record_id):
        pass

    def get_financial_records_for_employee(self, employee_id):
        pass

    def get_financial_records_for_date(self, record_date):
        pass
