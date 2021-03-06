"""
1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""

a = 5
b = 6
res_and = a & b
res_or = a | b
res_xor = a ^ b
res_left = a << 2
res_right = a >> 2

print(f'Побитовая операция 5 AND 6: {res_and}')
print(f'Побитовая операция 5 OR 6: {res_or}')
print(f'Побитовая операция 5 XOR 6: {res_xor}')
print(f'Побитовое смещение 5 влево на 2 знака: {res_left}')
print(f'Побитовое смещение 5 вправо на 2 знака: {res_right}')
