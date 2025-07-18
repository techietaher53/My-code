l = [1, 2, 6, 7, 6]
# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simpliflied using enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")