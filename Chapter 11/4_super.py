class Employee:
    def __init__(self):
        print('Constructer of  Employee')
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print('Constructer of  Programmer')
    b = 2

class Manager(Programmer):
    
    def __init__(self):
        super().__init__()
        print('Constructer of  Manager')
    c = 3


e = Employee()
print(e.a)

e = Programmer()
print(e.a, e.b)


e = Manager()
print(e.a, e.b, e.c)