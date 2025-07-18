a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("ARE YOU IN NURSERY OR WHAAAT???" \
    "YOU CANT DIVIDE WITH ZERO")
else:
    print(f"The division of a/b is {a/b}")