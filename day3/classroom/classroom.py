class Person():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    def printFullName(self):
        print(f"{self.name} {self.lastname}")

class Student(Person):
    def __init__(self, name, lastname, subject):
        Person.__init__(self, name, lastname)
        self.subject = subject
    def printNameSubject(self):
        print(f"{self.name} {self.lastname}, {self.subject}")

class Teacher(Person):
    def __init__(self, name, lastname, course):
        Person.__init__(self, name, lastname)
        self.course = course
    def printNameSubject(self):
        print(f"{self.name} {self.lastname}, {self.course}")

