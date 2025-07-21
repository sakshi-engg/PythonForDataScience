from dao.iemployee_service import IEmployeeService
from util.db_conn_util import DBConnUtil
from entity.employee import Employee
from exception.employee_not_found_exception import EmployeeNotFoundException

class EmployeeService(IEmployeeService):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    def get_employee_by_id(self, employee_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Employee WHERE EmployeeID = ?", (employee_id,))
            row = cursor.fetchone()
            if row:
                return Employee(*row)
            else:
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def get_all_employees(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Employee")
            rows = cursor.fetchall()
            return [Employee(*row) for row in rows]
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def add_employee(self, employee_data):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                employee_data.get_first_name(), employee_data.get_last_name(), employee_data.get_dob(),
                employee_data.get_gender(), employee_data.get_email(), employee_data.get_phone_number(),
                employee_data.get_address(), employee_data.get_position(), employee_data.get_joining_date(),
                employee_data.get_termination_date()
            ))
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def update_employee(self, employee_data):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE Employee SET FirstName=?, LastName=?, DateOfBirth=?, Gender=?, Email=?, PhoneNumber=?, 
                Address=?, Position=?, JoiningDate=?, TerminationDate=? WHERE EmployeeID=?
            """, (
                employee_data.get_first_name(), employee_data.get_last_name(), employee_data.get_dob(),
                employee_data.get_gender(), employee_data.get_email(), employee_data.get_phone_number(),
                employee_data.get_address(), employee_data.get_position(), employee_data.get_joining_date(),
                employee_data.get_termination_date(), employee_data.get_employee_id()
            ))
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def remove_employee(self, employee_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Employee WHERE EmployeeID = ?", (employee_id,))
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
