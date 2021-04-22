"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/21/21
"""
# coding: utf-8
import random


class License:
    is_expired = False

    def __init__(self):
        self.license_id = int(random.random() * 100)

    def get_id(self):
        return self.license_id

    def check_expired(self):
        if self.is_expired:
            print('License is expired!')
        else:
            print('License is fine')


    def make_all_expired(self):
        License.is_expired = True


la = License()
print(la.get_id(), la.check_expired())

lb = License()
print(lb.get_id(), lb.check_expired())

la.make_all_expired()
# License.is_expired = True
print(lb.get_id(), lb.check_expired())

la.author = 'jet'

print(dir(la))
