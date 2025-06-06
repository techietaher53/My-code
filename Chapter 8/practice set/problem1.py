def gr_num(n1,n2,n3):
    if (n1>n2 and n1>n3):
        return n1
    elif(n2>n3 and n2>n1):
        return n2
    elif(n3>n1 and n3>n2):
        return n3
    
n1 = int(input('Enter a number: '))
n2 = int(input('Enter a number: '))
n3 = int(input('Enter a number: '))

print(f'the gretest number is:{gr_num(n1,n2,n3)}')