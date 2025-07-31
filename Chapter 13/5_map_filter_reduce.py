from functools import reduce
# Map example
l = [22, 26, 2006, 6, 3, 9, 7]

square = lambda x: x*x

sqList = map(square, l)
print(list(sqList))

# Filter example
def even(n):
    if(n%2 == 0):
        return True
    return False



onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Example
def sum(a, b):
    return a + b

mul = lambda x,y:x*y

print(reduce(sum, l))
print(reduce(mul, l))
