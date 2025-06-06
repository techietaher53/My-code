a = int(input('enter number 1:'))
b = int(input('enter number 2:'))
c = int(input('enter number 3:'))
d = int(input('enter number 4:'))

if(a>b and a>c and a>d):
    print('a is the greatest number:', a)

elif(b>a and b>c and b>d):
    print('b is the greatest number:', b)
elif(c>a and c>b and c>d):
    print('c is the greatest number:', c)
elif(d>a and d>b and b>c):
    print('d is the greatest number:', d)