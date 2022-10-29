'''# 1'''
# a = int(input())
# for i in range(1, 21):
#     print('$',str(i),'текущий курс в рублях', str(i*a))
'''# 2'''
# a = int(input('введите число '))
# for i in range(1, 10):
#     print(str(a), '*', str(i), '=', str(i*a))
'''# 3'''
# a = int(input('введите а '))
# b = int(input('введите b '))
# s = 0
# i = a
# if b < a:
#     print('невернo')
# else:
#     while i <= b:
#         s+=i*i
#         i+=1
#     print(s)
'''# 4'''
# a = int(input())
# s = a
# for i in range(1, 6):
#     print(s%10, end='')
#     s//= 10
'''# 5'''
# n = int(input())
# s = 1
# c = 1
# for i in range(2, n + 1):
#     c *= i
#     s += c
# print(s)
'''# 6'''
# lst = [-1,-2,-3,-5,-6,-7,-7,9,7,-4,9]
# count = 0
# index = 0
# while (lst[index] < 0):
#     count += 1
#     index +=1
# print(count)
'''# 7'''
# fib1 = 1
# fib2 = 1
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n) - 2
# while n>0:
#     fib1, fib2 = fib2, fib1 + fib2
#     n -= 1
#  
# print("Значение этого элемента:", fib2)
'''#8'''
# n = int(input())
# s = 0
# while n != 0:
#     if n % 10 == 0:
#         s+=1
#     n //= 10
# print(s)
'''#9'''
# n, f, s = map(float, input('n, f, s = ').split())
# if s != 0:
#     if n == f:
#         print('Нет')
#     else:
#         if s<0:
#             f, n = n, f
#             s = abs(s)
#         while f<n:
#             f += s
#         print('Да' if n == f else 'Нет')
# else:
#     print('Да' if n == f else 'Нет')
'''#10'''
# cheslo = int(553244000)
# cheslo = str(cheslo)
# ok = []
# for i in cheslo:
#     ok.append(i)
# print(ok)
# print(ok.index(max(ok)))
# ok.reverse()
# print(ok.index(max(ok)))
'''#11'''
# from math import *
# f = int(input("Введите факториал числа n:"))
# for n in range(1,f+1):
#     if(n==f):
#         print("неверно")
#         break
#     if factorial(n) == f:
#         print(n)
#         break
'''#12'''
# n = int(input()) 
# money = [] 
# money_range = sorted([1, 2, 4, 8, 16, 32, 64], reverse=True) 

# for i in range(0, len(money_range)): 

#     if n // money_range[i] != 0:
#         num = n // money_range[i] 
# for j in range(0, num): 
#     money.append(money_range[i]) 
#     n -= money_range[i] 
# else:    
#     print(*money) 
'''#13'''
# for b in range (1, 100//10+1):
#     for k in range(1, 100//5+1):
#         for t in range(1, 101-b-k):
#             if b+k+t == 100 and b*10+k*5+t*0.5 == 100:
#                 print("быки:", b, "коровы:", k, "телята:", t)
'''#14'''
# e=int(input())
# i = 0
# for e in range(e):
#     e += 1
# i = i + e ** 2
# print (i)




