from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def bookTicket(self, fro, to):
        print(f'Ticket is booked in train no:{self.trainNo} from {fro} to {to}')
    
    def getStatus(self):
        print(f'Train no: {self.trainNo} is running on time')

    def getFare(self, fro , to):
        print(f'Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(125, 2000)}')

t = Train(12568)
t.bookTicket('Kota', 'Indore')  
t.getStatus()     
t.getFare('Kota', 'Indore')

