"""
Python OOPs: Class, Object, Inheritance and Constructor with Example

"""


class Student():

    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def get(self):
        return self
