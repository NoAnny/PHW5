# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
temp = [0] * b
print(f'{a}^{b} = {pow(a,b)}')

def pow(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif temp[b] == 0 and b >0:
        q = pow(a,b-1)*a
        temp[b] = q
        return q
    else:
        q = 1/(pow(a,b-1)*a)
        temp[b] = q
        return q