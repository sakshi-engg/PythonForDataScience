from dao.ipayroll_service import IPayrollService
from util.db_conn_util import DBConnUtil

class PayrollService(IPayrollService):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    def generate_payroll(self, employee_id, start_date, end_date):
        pass

    def get_payroll_by_id(self, payroll_id):
        pass

    def get_payrolls_for_employee(self, employee_id):
        pass

    def get_payrolls_for_period(self, start_date, end_date):
        pass
