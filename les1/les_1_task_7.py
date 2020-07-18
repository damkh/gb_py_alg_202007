"""
7. Определить, является ли год, который ввел пользователь, високосным или не високосным.
"""
try:
    year = int(input("Введите год (н.э.): "))
    if year > 0:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print("Год високосный")
        else:
            print("Год не високосный")
    else:
        print("Ведено отрицательное число")

except ValueError:
    print("Введено не целое число")
