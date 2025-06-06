p = int(input('enter a number:'))

for i in range(2, p):
    if(p%i) == 0:
        print('number is not prime')
        break
else:
    print('Number is prime')