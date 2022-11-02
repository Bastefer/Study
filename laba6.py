'''# 1'''
# print(len(set(input().split())))
'''# 2'''
# print(len(set(input().split()) & set(input().split())))
'''# 3'''
'''# 4'''
# s = int(input())
# mass=[]
# for i in range(s):
#     mass.append(set())
#     for j in range(int(input())):
#         mass[i].add(input())
# evr = set.intersection(*mass)
# all = set.union(*mass)
# print(len(evr), *sorted(evr), sep='\n')
# print(len(all), *sorted(all), sep='\n')
'''# 5'''
# a = set('123')
# b = set('456')
# print(a | b)
'''# 6'''
# slov = {} ### словарь для строк
# for i in range(int(input())):
#     str = input().split()   ### ввод строк
#     for j in str:           ### словам из строки задаём счётчик 
#         slov[j] = slov.get(j, 0) + 1 ### по поиску этого же слова в словаре
# for j in sorted(slov.items(), key = lambda x: (-x[1],x[0])): ### выводим слова
#     print(j[0]) ### используя словарь, и функцию для сортировки по убыванию
'''# 7'''

'''# 8'''
# d = {}
# for i in range(int(input('число строк '))):
#     for word in input('строки ').split():
#         d[word] = d.get(word, 0) + 1
# 
# for i in sorted(d.items(), key=lambda x: (x[0])): #(i[0]-->keys, i[1]-->values)    
#     if i[1] == max(d.values()):
#         print('самое частое слово -', i[0])
#         break
'''#9'''
# from collections import defaultdict
# from sys import stdin
# 
# clients = defaultdict(lambda: defaultdict(int))
# for line in stdin.readlines():
#     client, thing, value = line.split()
#     clients[client][thing] += int(value)
#         
# for client in sorted(clients):
#     print(client + ':')
#     for thing in sorted(clients[client]):
#         print(thing, clients[client][thing])
'''# 10'''
# n = int(input())
# cities = {}
# for _ in range(n):
#     line = input().split()
#     for city in line[1:]:
#         cities[city] = line[0]
# 
# for _ in range(int(input())):
#     print(cities[input()])


















