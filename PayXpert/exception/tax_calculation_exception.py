class TaxCalculationException(Exception):
    def __init__(self, message="Tax calculation failed."):
        super().__init__(message)
