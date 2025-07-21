from dao.employee_service import EmployeeService
from dao.payroll_service import PayrollService
from dao.tax_service import TaxService
from dao.financial_record_service import FinancialRecordService
from util.db_property_util import DBPropertyUtil
from util.db_conn_util import DBConnUtil
from exception.invalid_input_exception import InvalidInputException
from util.validation_service import ValidationService
from util.report_generator import ReportGenerator

import datetime


def display_menu():
    print("\n==== PayXpert Payroll Management System ====")
    print("1. Add New Employee")
    print("2. View All Employees")
    print("3. Generate Payroll")
    print("4. Calculate Tax")
    print("5. Add Financial Record")
    print("6. View Financial Records for Employee")
    print("7. Exit")
    print("============================================")


def main():
    try:
        conn_str = DBPropertyUtil.get_connection_string("config.properties")
        connection = DBConnUtil.get_connection(conn_str)

        employee_service = EmployeeService(connection)
        payroll_service = PayrollService(connection)
        tax_service = TaxService(connection)
        financial_record_service = FinancialRecordService(connection)

        while True:
            display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                print("\nEnter Employee Details:")
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                dob = input("Date of Birth (YYYY-MM-DD): ")
                gender = input("Gender: ")
                email = input("Email: ")
                phone = input("Phone Number: ")
                address = input("Address: ")
                position = input("Position: ")
                joining_date = input("Joining Date (YYYY-MM-DD): ")

                try:
                    ValidationService.validate_email(email)
                    ValidationService.validate_phone(phone)
                    ValidationService.validate_non_empty_string(first_name, "First Name")

                    employee_service.add_employee(first_name, last_name, dob, gender, email,
                                                  phone, address, position, joining_date, None)
                    print("Employee added successfully.")
                except InvalidInputException as e:
                    print(f"Validation Error: {e}")

            elif choice == '2':
                employees = employee_service.get_all_employees()
                for emp in employees:
                    print(vars(emp))

            elif choice == '3':
                emp_id = int(input("Enter Employee ID: "))
                start = input("Pay Period Start Date (YYYY-MM-DD): ")
                end = input("Pay Period End Date (YYYY-MM-DD): ")
                payroll = payroll_service.generate_payroll(emp_id, start, end)
                print(ReportGenerator.generate_payroll_report(payroll))

            elif choice == '4':
                emp_id = int(input("Enter Employee ID: "))
                year = int(input("Enter Tax Year: "))
                tax = tax_service.calculate_tax(emp_id, year)
                print(ReportGenerator.generate_tax_report(tax))

            elif choice == '5':
                emp_id = int(input("Enter Employee ID: "))
                date = input("Record Date (YYYY-MM-DD): ")
                desc = input("Description: ")
                amount = float(input("Amount: "))
                record_type = input("Record Type (income/expense/tax): ")
                financial_record_service.add_financial_record(emp_id, date, desc, amount, record_type)
                print("Financial record added.")

            elif choice == '6':
                emp_id = int(input("Enter Employee ID: "))
                records = financial_record_service.get_records_for_employee(emp_id)
                for rec in records:
                    print(ReportGenerator.generate_financial_report(rec))

            elif choice == '7':
                print("Thank you for using PayXpert!")
                break
            else:
                print("Invalid choice. Try again.")

    except Exception as e:
        print(f"Application error: {e}")


if __name__ == '__main__':
    main()
