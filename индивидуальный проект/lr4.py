import pickle

class Hospital():
    def __init__(self, patients, doctor):
        self.patients = patients
        self.doctor = doctor
    
    # Конструктор
    def chamber(self):
        x = b1.patients + b2.patients + b3.patients + b4.patients
        return( f"Лечющий врач {self.doctor} лечит {x} болных")
    
    def test(self):  # unittest
        x = b1.patients + b2.patients + b3.patients + b4.patients
        return x
    
    # Сериализация
    def serialize(self):
        with open('ster.pkl', 'wb') as f:
            pickle.dump(self.patients, f)
        f.closed
        
    # Десериализация
    def deserialize(self):
        with open ('ster.pkl', 'rb') as f:
            Hospital = pickle.load(f)
        f.close
        return Hospital
    
    #Деконструктор
    # def __del__(self):
    #     print(f'{self.patients} пациентов выписалось')

# Наследование    
class Patient(Hospital):
    def __init__(self, patients, doctor, name, disease):
        super().__init__(patients, doctor)
        self.name = name
        self.disease = disease
        
    def medical_card(self): 
        print('Пациент '+ self.name + " находится в больнице по подозрению в диагнозе " + self.disease + ' его лечущий врач '+ self.doctor )

    #Полиморфизм
    def chamber(self):
        print(f"Все в 3 группе у всех болезьнь {self.disease}.")
        
  
b1 = Hospital(8, 'Баранов Виктор')
b2 = Hospital(5, 'Ульянов Кирил')
b3 = Hospital(10, 'Булыгин Динис')
b4 = Hospital(7, 'Стирманов Сергей')
print(b2.chamber())
b3 = Patient(b3.patients, b3.doctor, "Антонов Александр", 'аппендицит')
b3.medical_card()
b3.chamber()
b1.serialize()
# print(b1.deserialize())
b4.serialize()
# print(b4.deserialize())

