

class Employee():
    num_of_emplyoees = 0
    raise_salary = 1.04  # these are class based variables and can be accessed using Employee class name like Employee.raise_salary

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.num_of_emplyoees += 1

    def fullname(self):
        return '{} age is {}'.format(self.name, self.age)


Employee.raise_salary = 1.02

print(Employee.__dict__)
emp_1 = Employee("vidya", 24, 52000)
emp_2 = Employee("sagar", 24, 56000)
print(emp_1.__dict__)
print(emp_1.fullname())
