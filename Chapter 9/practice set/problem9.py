with open('this.txt') as f:
    content = f.read()

with open('this1.txt') as f:
    content1 = f.read()

if(content == content1):
    print('Its the same')
else:
    print('Its not the same as you are')