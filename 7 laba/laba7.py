'''#1'''
with open('1.txt') as datfile:
    text = datfile.read()
print(sum(map(int, text.split(None, 2)[:2])))
'''#2'''
import mmap

with open('2.txt', 'rb', 0) as file, \
    mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
    if s.find(b's') != -1:
        print('YES')
    else:
        print('NO')
'''3'''
with open('3.txt') as t:
    print(*(sum(map(int, line.split())) for line in t.readlines()), sep='\n')
'''#4'''
# lines = 0
# words = 0
# letters = 0 

# for line in open('4.txt', 'r'):    
#     lines += 1     
#     letters += len(line)      
#     pos = 'out' 
    
#     for letter in line:        
#         if letter != ' ' and pos == 'out':            
#             words += 1            
#             pos = 'in'        
#         elif letter == ' ':            
#             pos = 'out'
# print("Lines:", lines)
# print("Words:", words)
# print("Letters:", letters)
'''#5'''
# file = '5.txt' 
# action = input("Введите от 'a' до 'e': ").lower() #a b c d e
 
# with open(file) as f:
#     data = f.readlines()
 
# if action == 'a':
#     print(*data[0], sep='')
# elif action == 'b':
#     print(*data[4], sep='')
# elif action == 'c':
#     print(*data[0:4], sep='')
# elif action == 'd':
#     s1, s2 = map(int, input('Введите s1 и s2 через пробел: ').split())
#     print(*data[s1-1 : s2-1], sep='')
# elif action == 'e':
#     print(*data, sep='')
'''#6'''
# large_line = ''
# with open('6.txt', 'r') as f:
#     for line in f.readlines():  
#         if len(line)>len(large_line):
#             large_line = line

# wordlist = [] 
# f = open('6.txt')
# for word in f.readlines():
#     wordlist.append(word.strip())
# f.close()
# number =0
# length =0
# for i in range(len(wordlist)): 
#     if len(wordlist[i]) > length: 
#         length = len(wordlist[i]) 
#         number = i
# print('Напечатать самую длинную строку:', large_line, end = '')
# print('длинна самой длинной строки', length)
# print('номер самой длинной строки', number + 1)
'''#7 a)'''
# with open('7.txt') as file:
#     lines = [line.rstrip()[::-1] + '\n' for line in file.readlines()]

# with open('71.txt', 'w') as file:
#     file.writelines(lines)
'''#7 b)'''
# with open('7.txt') as file:
#     lines = [line.rstrip()[::-1] + '\n' for line in file.readlines()]

# with open('71.txt', 'w') as file:
#     file.writelines(lines[::-1])
'''#8'''
# count = 0
# eq = True
# with open("8.txt", "r", encoding = "utf-8") as f1, open("81.txt", "r", encoding = "utf-8") as f2:
#     for a1, a2 in zip(f1, f2):
#         count += 1
#         if a1 != a2:
#             eq = False
#             break
# print(f"Нет отличий") if eq else print(f"Отличается строка {count}")
'''#10'''
# inFile = open('10.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
# k = inFile.readline()
# k = int(k)
# rez = []
# l = inFile.readlines()
# for i in l:
#     if len(i.split()) == 6:
#         n1, n2, n3, s1, s2, s3 = i.split()
#     if len(i.split()) == 5:
#         n1, n2, s1, s2, s3 = i.split()
 
#     if int(s1) >= 40 and int(s2) >= 40 and int(s3) >= 40:
#         sum = int(s1) + int(s2) + int(s3)
#     else:
#         sum = 0
#     rez.append(sum)
# rez.sort(reverse=True)
# if rez[k] == 0:
#     print(0)
# elif rez[0] == rez[k]:
#     print(1)
# elif rez[k] == rez[k - 1]:
#     print(rez[k - 2])
 
# else:
#     print(rez[k - 1])
# inFile.close()
# outFile.close()