class ReportGenerator:

    @staticmethod
    def generate_payroll_report(payroll):
        report = f"""
        Payroll Report:
        ----------------
        Payroll ID: {payroll.payroll_id}
        Employee ID: {payroll.employee_id}
        Period: {payroll.pay_period_start_date} to {payroll.pay_period_end_date}
        Basic Salary: {payroll.basic_salary}
        Overtime Pay: {payroll.overtime_pay}
        Deductions: {payroll.deductions}
        Net Salary: {payroll.net_salary}
        """
        return report.strip()

    @staticmethod
    def generate_tax_report(tax):
        report = f"""
        Tax Report:
        ------------
        Tax ID: {tax.tax_id}
        Employee ID: {tax.employee_id}
        Tax Year: {tax.tax_year}
        Taxable Income: {tax.taxable_income}
        Tax Amount: {tax.tax_amount}
        """
        return report.strip()

    @staticmethod
    def generate_financial_report(record):
        report = f"""
        Financial Record:
        ------------------
        Record ID: {record.record_id}
        Employee ID: {record.employee_id}
        Date: {record.record_date}
        Description: {record.description}
        Amount: {record.amount}
        Type: {record.record_type}
        """
        return report.strip()
