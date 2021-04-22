"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/22/21
"""


# coding: utf-8
class Employee:
    raise_amt = 2

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 4


emp1 = Employee('Corey', 'Schafer', 500)
emp1.apply_raise()
print(emp1.pay)

dev1 = Developer('Jet', 'C', 1000)
print(dev1.raise_amt)
print(emp1.raise_amt)
