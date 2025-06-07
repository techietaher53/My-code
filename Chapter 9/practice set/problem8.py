with open('this.txt') as f:
    content = f.read()

with open('this1.txt', 'w') as f:
    f.write(content)
