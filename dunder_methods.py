class Employee():
    num_of_emplyoees = 0
    raise_amt = 1.04  # these are class based variables and can be accessed using Employee class name like Employee.raise_salary

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.num_of_emplyoees += 1

    def __str__(self): # str dunder method
        return '{}'.format(self.name)

    def __repr__(self): # repr dunder method
        return '{}'.format(self.salary)


emp_1 = Employee("vidya", 23, 54000)

print(repr(emp_1))
