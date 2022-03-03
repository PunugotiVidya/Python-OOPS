class Employee():
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print("Object deleted")


emp_1 = Employee("vidya", "sagar")
# since we used property as decorator we can use fullname as attribute instead of function.
# since we used setter we can set the values instead of calling functions.
emp_1.fullname = "vidya punugoti"
print(emp_1.fullname)
print(emp_1.email)
del emp_1.fullname
