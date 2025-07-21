from dao.itax_service import ITaxService
from util.db_conn_util import DBConnUtil

class TaxService(ITaxService):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    def calculate_tax(self, employee_id, tax_year):
        pass

    def get_tax_by_id(self, tax_id):
        pass

    def get_taxes_for_employee(self, employee_id):
        pass

    def get_taxes_for_year(self, tax_year):
        pass
