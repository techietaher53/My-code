def sum(n):
    if (n==1):
        return 1
    return sum(n-1) + n

n = int(input('Enter a number: '))

print(f'The sum of this number is: {sum(n)}')
