from datetime import date

class Employee:
    def __init__(self, employee_id = None, first_name = None, last_name = None, dob = None, gender = None, email = None, phone_number = None, address = None, position = None, joining_date = None, termination_date = None):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.__gender = gender
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address
        self.__position = position 
        self.__joining_date = joining_date
        self.__termination_date = termination_date
        
#getters

def get_employee_id(self):
    return self.__employee_id

def get_first_name(self):
    return self.__first_name

def get_last_name(self):
    return self.__last_name

def get_dob(self):
    return self.__dob

def get_gender(self):
    return self.__gender

def get_email(self):
    return self.__email

def get_phone_number(self):
    return self.__phone_number

def get_address(self):
    return self.__address

def get_position(self):
    return self.__position

def get_joining_date(self):
    return self.__joining_date

def get_termination_date(self):
    return self.__termination_date

#setters
def set_employee_id(self, employee_id):
     self.__employee_id = employee_id

def set_first_name(self, first_name):
     self.__first_name = first_name

def set_last_name(self, last_name):
     self.__last_name = last_name

def set_dob(self, dob):
     self.__dob = dob

def set_gender(self, gender):
     self.__gender = gender

def set_email(self, email):
     self.__email = email

def set_phone_number(self, phone_number):
     self.__phone_number = phone_number

def set_address(self, address):
     self.__address = address

def set_position(self, position):
     self.__position = position

def set_joining_date(self, joining_date):
     self.__joining_date = joining_date

def set_termination_date(self, termination_date):
     self.__termination_date = termination_date

#Method to calculate age
def calculate_age(self):
    if self.__dob:
        today = date.today()
        return today.year - self.__dob.year - ((today.month, today.day) < (self.__dob.month, self.__dob.day))
