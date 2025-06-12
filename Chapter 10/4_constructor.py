class musaid:
    salary = '5000'
    time = '90 minutes' # class attribute
    def __init__(self):# dunder method which is automatically called when you create an object
        print(' Now who the fuck made an object?') 
    
    
     
    def getInfo(self): 
        print(f'The salary is {self.salary} and Time is {self.time}')

taher = musaid()
taher.salary ='5500'  # instance attribute
taher.name = 'Taher '

# print(taher.name,taher.salary, taher.time)
 