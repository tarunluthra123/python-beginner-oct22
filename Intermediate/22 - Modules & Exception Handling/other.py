def hello():
    print("Hello world")


class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student object (name: %s)" % self.name

x = 10