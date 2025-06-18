class Animals:
    favorite_animal = 'Horse'

class Pets(Animals):
    p = 'Horse is a good pet'

class Dog(Pets):
    d = " I dont like dogs"
    @staticmethod
    def bark():
        print('Bhow Bhow')

d = Dog()
print(d.favorite_animal)

