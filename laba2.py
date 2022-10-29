'''##1'''
# x = int(input())
# y = int(input())
# if x>4:
#     print ('II')
# else:
#     print('I')
'''##2'''
# x = int(input())
# y = int(input())
# if y<3:
#     print ('II')
# else:
#     print('I')
'''##3,a'''
# x = int(input())
# if x >= 2 :
#     print(2)
# else:
#     print(x)
'''##3,b'''
# x = int(input())
# if x >= 3 :
#     print(-3)
# else:
#     print(-x)
'''##4'''
# x = int(input())
# y = int(input())
# print(max(x, y))
# print(min(x, y))
'''##5'''
# x = int(input())
# y = int(input())
# if x > y:
#     print('1е максимальное, 2е минимальное')
# else:
#     print('2е максимальное, а 1е минимальное')
'''##6'''
# years = int(input('Введите год рождения: '))
# month = int(input('Введите месяц рождения: '))
# years_now = int(input('Введите сейчашний год: '))
# month_now = int(input('Введите сейчашний месяц: '))
# ols = years_now - years
# mos = month_now + month
# if mos >= 12:
#     ols += 1
# print(ols)
'''##7'''
# from math import sin
# x = int(input())
# if x > 0:
#     y = sin(x)*sin(x)
# else:
#     y = 1-2*sin(x**2)
# print(y)
'''##8'''
# from math import sin
# x = int(input())
# if x > 0:
#     y = sin(x**2)
# else:
#     y = 1+2*sin(x)*sin(x)
# print(y)
'''##9'''
# a = int(input())
# b = int(input())
# if b % a == 0:
#     print ("да")
# else:
#     print ("нет")
'''##10'''
# a = int(input())
# if a %2 == 0:
#     print('чётноё')
# else:
#     print('не чётноё')
# while a > 10:
#     a %= 10
# if a == 7:
#     print('оканчивается на 7')
# else:
#     print('не оканчивается на 7')
'''##11'''
# a = int(input())
# b = a
# if b % 10 == b // 10:
#     print('цифры одинаковы')
# elif b % 10 > b // 10:
#     print('вторая больше')
# else:
#     print('первое больше')
'''##12'''
# a = (input())
# b = a[::-1]
# if int(a) / int(b) == 1:
#     print('полиндром')
# else:
#     print('не полиндром')
'''##13'''
# a = int(input())
# s = a // 100
# d = a % 100// 10
# f = a %10
# if s == d and s==f and f==d:
#     print('все цифры одинаковые')
# elif s == d or s==f or f==d:
#     print('в числе есть одинаковые цифры')
# else:
#     print('в числе нет одинаковых цифр')
'''##14'''
# a = int(input())
# s = a % 10
# if s // 2 ==0 and s != 0:
#     print('оно заканчивается четной цифрой')
# elif s // 2 !=0:
#     print('оно заканчивается нечетной цифрой')
# else:
#     print('оно заканчивается нулём')
'''##15'''
# n = int(input())
# if 0 <= n % 5 <= 3:
#     print('green')
# else:
#     print('red')
'''##16'''
# a = int(input())
# print(a // 1000, 'число полных тонн')
'''##17'''
# a = 130
# b = 543
# c = 130
# print(b // c, 'квадратов со стороной 130 мм можно отрезать от него')
'''##18'''
# m = int(input('m='))
# a = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
# print(a[m % 12])
'''##19'''
# a = input()
# print(a[::-1])
'''##20'''
# a = int(input())
# b = a // 100
# c = a % 100
# print(c,b,sep='')
'''##21'''
# a = int(input())
# b = a // 10
# c = a % 10
# print(c,b,sep='')
'''##22'''
# a = int(input())
# b = a // 100
# c = a // 10 % 10
# d = a % 10
# print(c,b,d,sep='')
'''##23'''
# a = int(input())
# b = a // 100
# c = a // 10 % 10
# d = a % 10
# print(b,d,c,sep='')
'''##24'''
# n = int(input())
# a = n // 100
# b = n // 10 % 10
# c = n % 10
# print(a, b, c,sep='')
# print(a, c, b,sep='')
# print(b, a, c,sep='')
# print(b, c, a,sep='')
# print(c, a, b,sep='')
# print(c, b, a,sep='')
'''##25'''
# n = int(input())
# e = n % 10
# d = n // 10
# print(e, ' единиц ', d, ' десятков')
'''##26'''
# n=int(237)
# c=n//100 
# x=(n%100)*10+c 
# print (x, 'исходное число Х')
'''##27'''
# n=int(input())
# c=n//100 
# n=(n%100)*10+c
# print (n, 'исходное число Х')
'''##28'''
# n = int(input())
# print((n % 10)*100+(n // 10))
'''#29'''
# n = int(input())
# x = n % 10 + n // 100 * 10 + n % 100 // 10 * 100
# print(x)
'''#33'''
# a = int(input())
# b = int(input())
# c = int(input())
'''# #а'''
# print((a>100) and (b>100))
'''# #б'''
# print (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0)
'''# #в'''
# print(a>0) or (b>0)
'''# #г'''
# print((a%3==0 and b%3==0 and c%3==0))
'''# #д'''
# if a % 2 == 0 and b % 2 == 0 and  c % 2 == 0:
#     print("NO")
#     exit()
# if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
#     print('YES')
# else:
#     print('NO')
'''# #е'''
# print((a<0) or (b<0) or (c<0))
'''#34'''
# x1, y1, x2, y2 = [input() for _ in range(4)]
# print('YES' if (x1 == x2) is not (y1 == y2) else 'NO')












#  