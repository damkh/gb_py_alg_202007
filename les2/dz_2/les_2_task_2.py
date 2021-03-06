"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
num = int(input("Введите число: "))
n_even = 0
n_odd = 0

while num > 0:
    n = num % 10
    if n % 2 == 0:
        n_even += 1
    else:
        n_odd += 1
    num //= 10

print(f"Количество четных: {n_even}")
print(f"Количество нечетных: {n_odd}")
