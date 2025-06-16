from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
        
    def bookTicket(Taher, fro, to):
        print(f'Ticket is booked in train no:{Taher.trainNo} from {fro} to {to}')
    
    def getStatus(Shakir):
        print(f'Train no: {Shakir.trainNo} is running on time')

    def getFare(self, fro , to):
        print(f'Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(125, 2000)}')

t = Train(12568)
t.bookTicket('Kota', 'Indore')  
t.getStatus()     
t.getFare('Kota', 'Indore')

# The answer is: YES,we can change self to something else and stil, the program will run as usual.