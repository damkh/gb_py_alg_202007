"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
"""
n = 32
while 32 <= n <= 127:
    s = chr(n)
    print(f'{n}:"{s}"', end='    ')
    if (n - 1) % 10 == 0:
        print()
    n += 1
