class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f'the class attribute of "a" is {cls.a}')

e = Employee()
e.a = 45
print(e.a) 

e.show()