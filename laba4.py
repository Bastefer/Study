'''#1'''
# from random import randint
# lst=[]
# for i in range(12):
#     lst.append(randint(163, 190))
# print(lst)
'''2'''
# a = int(input("a = "))
# p = int(input("p = "))
# lst = [a]
# for i in range(1, 10):
#     lst.append(a+i*p)
# print(lst)
'''3'''
# s = list(input())
# for i in reversed(s):
#     print(i, end='')
'''4'''
# a = [int(x) for x in input().split()]
# print(sum(a[::2]) - sum(a[1::2]))
'''5'''
# k=[10,0,0,40,5,30,10,10,00,40,35,00,10,10,20,40,0,30,10,10,20,00,35,30,10,10,20,40,35,30,10,20,40,35,30,10,10,20,40,35,30,10]
# t=str(sum(k))
# if len(t)==4:
#     print(" есть четырехзначное число")
# else :
#     print(" не является четырехзначным числом")
'''6 a)'''
# s=input().split()
# for i in range(len(s)):
#     s[i] =int(s[i])
#     if s[i]%2==0:
#         print(s[i])
'''6 b)'''
# s=input().split()
# for i in range(len(s)):
#     s[i] =int(s[i])
#     if s[i]%10==0:
#         print(s[i])
'''7'''
# math = ['60', '50', '40', '13', '45', '12', '52', '78', '98', '53', '65']
# inf = ['60', '50', '40', '15', '58', '45', '65', '87', '97', '86', '45']
# rus = ['60', '50', '40', '20', '65', '89', '75', '56', '88', '46', '68']
# stud = ['Иванов', 'Петров', 'Сидоров', 'Антонов', 'Кустов', 'Лудинов', 'Стирманов', 'Комаров', 'Жуков', 'Шольц', 'Годунов']
# for x in range(len(stud)):
#     print(stud[x],rus[x],inf[x],math[x])
#     if not max(rus):
#         print('Не зачислен')
#     else:
#         print('Зачислен')
'''8'''
# lst=[int(i) for i in input().split()]
# print(len(set(lst)))
'''9'''
# a = [int(i) for i in input().split()]
# for i in range(1, len(a), 2):
#     a[i - 1], a[i] = a[i], a[i - 1]
# print(' '.join([str(i) for i in a]))
'''10'''
# import random
# l = []
# r = int(input())

# for i in range(r):  #создаем список
#     l.append(random.randint(-5,5))
# half = r//2  # для четного количества элементов списка
# shalf = r//2+r%2  # для нечетного кол-ва    _._._._._._._._._._
# print (l)
# if r%2 == 0: # проверка для четного кол-ва
#     print(l[half:] + l[0:half])  # меняем местами элементы
# else:
#     nl = l[half+1:]+ l[shalf-1:shalf] + l[0:half]  # если проверка не пройдена, то меняем местами, при этом оставляем средний
#     print(nl)                                      # элемент списка посередине
'''11'''
# a = [int(s) for s in input().split()]
# guests = 0
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] == a[j]:
#             guests += 1
# print(guests)
'''12'''
# mylist = ['45', '45', '46', '42', '45', '43', '45']
# myset = set(mylist)
# print(myset)
'''13'''
# from functools import reduce

# a = [17,18,19]
# b = [['Иванов', 'Петров', 'Сидоров'], ['Антонов', 'Кустов'], ['Лудинов', 'Стирманов', 'Комаров', 'Жуков']]
# c = list(reduce(lambda x,y: x+y, b))
# print(len(c))
# print(min(b, key=len))
# print(max(b, key=len))
# print(sorted(c))
'''14'''
# grades = [5, 4, 5, 3, 2, 5, 4, 3, 5, 5, 4, 2, 2, 3]
# print(f'Средний балл: {sum(grades) / len(grades)}')
# print(*grades, sep=';')
'''15'''
# print([i for i in range(1, 10001) if (not i%3 and not i%7) or not i%9])
'''16'''
# a = input ("Напишите, сколько строк вы хотите напечатать: ")
# a = int(a)
# lst = []
# for i in range(1, a+1):
#     line = str(i)
#     lst.append(line + str(i))
# print(lst)    
'''17'''
# a = [[i,10*i] for i in range(1,5)]
# print(a)
# b = sum(a,[])
# print(b)
'''18'''
print([i**2 if i%2 == 0 else i+2 for i in range(1,21)])
