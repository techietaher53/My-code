class musaid:
    salary = '5000'
    time = '90 minutes' # class attribute

taher = musaid()
taher.name ='Taher'  # instance attribute
taher.salary = '5300'
print(taher.name, taher.salary, musaid.time)

shabbir = musaid()
shabbir.name = 'Shabbir'
shabbir.time = '45 minutes'
print(shabbir.name, shabbir.salary, shabbir.time)

# here name is instance attribute and salary and time is class 
# attributes as they directly belong to the class.