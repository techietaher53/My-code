class musaid:
    salary = '5000'
    time = '90 minutes' # class attribute
    def getInfo(self):
        print(f'The salary is {self.salary} and Time is {self.time}')

taher = musaid()
taher.salary ='5500'  # instance attribute
taher.getInfo()
# musaid.getInfo(taher)