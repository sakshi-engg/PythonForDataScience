class PayrollGenerationException(Exception):
    def __init__(self, message="Error occurred during payroll generation."):
        super().__init__(message)
