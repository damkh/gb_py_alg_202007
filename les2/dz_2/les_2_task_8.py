"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def num_search(x, y):
    s = 0
    while x > 0:
        n = x % 10
        if n == y:
            s += 1
        x //= 10
    return s


quantity = int(input("Введите количество чисел (>0): "))
k = int(input("Введите искомую цифру: "))
s_all = 0

while quantity != 0:
    num = int(input("Введите число: "))
    s_all += num_search(num, k)
    quantity -= 1

print(f"Результат: {s_all}")
