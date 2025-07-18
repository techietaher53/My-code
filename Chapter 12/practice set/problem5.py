table = int(input("Enter a number to print its table: "))

TablePrint = [table*i for i in range(1, 11)]
with open("tables.txt", "a") as f:
    f.write(f"Table of {table} :{str(TablePrint)} \n")