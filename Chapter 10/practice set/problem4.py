class Calculator:
    def __init__(self, n):
        self.n = n
        

    def square(self):
        print(f'The square is {self.n*self.n}')
    def cube(self):
        print(f'The cube is {self.n*self.n*self.n}')
    def squareroot(self):
        print(f'The squareroot is {self.n**1/2}')

    @staticmethod
    def hello():
        print('Hello , Welcome to my Calculator')
    

a = Calculator(int(input('Enter the number: ')))
a.hello()
a.square()
a.cube()
a.squareroot()
