with open('poems.txt') as f:
    content = f.read()
    if('twinkle' in content):
        print('the word twinkle is there')
    else:
        print('the word twinkle is not there')
