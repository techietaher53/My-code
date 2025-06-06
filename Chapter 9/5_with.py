# f = open('file.txt')
# print(f.read())
# f.close

with open('file.txt') as f:
    print(f.read())

# with this statement , you dont have to close the file