class Number:
    def __init__(self, n):
        self.n = n

    def __sub__(self, num):
        return self.n - num.n
    
n = Number(17)
m = Number(10)

print(n - m)