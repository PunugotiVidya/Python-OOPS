
import datetime


class Employee():
    num_of_emplyoees = 0
    raise_amt = 1.04  # these are class based variables and can be accessed using Employee class name like Employee.raise_salary

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.num_of_emplyoees += 1

    @classmethod
    def from_string(cls, emp_str):
        name, age, salary = emp_str.split("-")
        return cls(name, age, salary)

    def fullname(self):
        return '{} age is {}'.format(self.name, self.age)

    @classmethod  # It needs cls as argument and it deals with class variables unlike normal class function which deals with instance variables.
    def set_raiseAmount(cls, amount):
        cls.raise_amt = amount

    @staticmethod  # staticmethod no need class or self as argument.
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


Employee.set_raiseAmount(1.02)

print(Employee.__dict__)
empstr_1 = "vidya-24-52000"
empstr_2 = "sagar-24-53000"
emp_1 = Employee.from_string(empstr_1)
emp_2 = Employee.from_string(empstr_2)

print(Employee.is_workday(datetime.date(2017, 8, 1)))
print(emp_1.__dict__)
print(emp_1.fullname())
