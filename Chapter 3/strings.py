a = 'Taher'     # Single quoted string    
b = "Aliasgar"   # Double quoted string
c = '''Shakir'''# Triple  quoted string


name ='TaherShakir'
namecut = name[0:5]
print(namecut)

# Negative slicing

name ='TaherShakir'

print(name[-7:-12])
print(name[0:5])

# Skip value

a = '123456789'
print(a[1:5:3])

# Str functions

name = 'taher'
print(len(name)) # len prints the length of string
print(name.endswith('er')) # endswith checks whether the string is ending with that character or not
print(name.startswith('tah')) # startswith checks whether the string is starting with that character or not
 
# escape sequence

# \n new line 
print('I am Taher shakir \nI live in Kota')
# \' character\' add single quotes
print('I am \'Taher\'')
