try:
    a : int = 5
    b : int = 0
    print(a/b)

except ZeroDivisionError:
    print("infinite")