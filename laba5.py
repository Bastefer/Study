'''#2 вар8'''
# import math
#  
#  
# def f(x: float) -> float:
#     return 3 ** (-x) - (x**2)+1
#  
#  
# print(f"y = {f(float(input('x = ')))}")
'''#3 вар8'''
#from math import sin, cos
 
 
#def f(x):
#    print(cos(y+0.5)+x-0.8)
#    print(-2*y+sin(x)-1.6)
#    return ''
#x = float(input('x = '))
#y = float(input('y = '))

#print(f(x))

'''#4 вар8'''
# n = int(input("Введите число:"))
# a = int(input("Введите число:"))
# def f(n, a):
#     count = 0
#     count2 = 0
#     while n > 0:
#         count = count + 1
#     n = n // 10
#     while a > 0:
#         count2 = count2 + 1
#     a = a // 10
#     if count2>count:
#         return "больше цифр в a"
#     else:
#         return "больше цифр в n"
# print(f(n, a))

'''#5 вар 1'''
# num = [int(x) for x in input().split()]

# def f(num):
#     print('минимальное = ', min(num))
#     print('максимальное = ', max(num))
#     return ''



# print(f(num)) 
'''#5  вар 8'''
# num = [int(x) for x in input().split()]
# def f(num):
#     print('сумма абсолютных значений  = ', sum(map(abs, num)))
#     if min(num)<0:
#         print('максимальное отрицательное значение = ', min(num))
#         return
#     else:
#         return
# print(f(num))    
'''#6'''
# N=int(input())
# base =int(input())
# def deston(N, base, result = None):
#     if not hasattr(deston, 'table'):        
#         deston.table = '0123456789ABCDEF'       
#     x, y = divmod(N, base)        
#     return deston(x, base) + deston.table[y] if x else deston.table[y]
# print(deston(N, base, result = None)) 
'''#7'''
# def prime(n):
#     counter = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             counter += 1
#     return 'Простое число' if counter == 2 else 'Составное число'
# n = int(input())
# print(prime(n))
'''#8'''
# l = [1, 6, 69, 21, 89, 9, 63, 52, 36, 13, 92, 45, 75, 24, 11, 856, 325, 917, 367, 924]
# print(list(map(lambda l: l%7, l)))
'''9'''
# s = ['катя', 'маша', 'таня', 'саша']
# print(list(map(lambda x: x.title(), s)))
'''#10'''
# lst = ['Маша', 'Петя', 'Вася']
# secret_Имяs = list(map(lambda x: hash(x), lst))
# print(secret_Имяs)
'''11'''
# from functools import reduce
 
# s = ['научиться плести рыболовные сети',
# 'обучать нейронные сети',
# 'паук ловит в сети мух']
# print(reduce(lambda x, y: x + y, map(lambda x: 'сети' in x.lower(), s), 0))
'''12'''
# my_list = [1, 6, 69, 21, 89, 9, 63, 52, 36, 13, 92, 45, 75, 24, 11, 856, 325, 917, 367, 924]
# print(list(filter(lambda x: (x%7 ==0), my_list)))
'''13'''
# vse =[]
# names = ['Георгий', "Александр", "Кирил", "Михаил"]
# math = [98, 54, 36, 68]
# rus = [89, 67, 25, 78]
# inf = [93, 65, 47, 73]
# res = list(zip(names, math, rus, inf))
# print (res)
