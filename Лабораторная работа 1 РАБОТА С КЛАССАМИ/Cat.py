class Cat:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
#         
#     def meow(self):
#         print('Мяу!')
#  
#     def eat(self):
#         print('Лакомлюсь рыбой')
#  
#     def sleep(self):
#         print('Я Сплю')
#  
    def __str__(self):
        return f'Я кот {self.name}, мне {self.age} лет'
 
cat = Cat('Барсик', 5)
print(cat)
cat.eat()
cat.meow()
cat.sleep()
