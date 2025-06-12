class Python:
    a = 'Taher'

learning = Python()
print(learning.a) # prints the class attribute because instance attribute is not present
learning.a = 0 # instance attribute is set
print(learning.a) # prints the instance attribute because instance attribute is present

print(Python.a) # prints the class attribute


