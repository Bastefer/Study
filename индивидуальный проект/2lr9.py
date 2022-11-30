class Hospital(): #инкапсуляция 
    def __init__(self, patients, doctor, name, disease, sitter):
        if isinstance(patients, int):
            self.patients = patients
        else:
            raise Error()
        self.doctor = doctor
        self.name = name
        self.disease = disease
        self.sitter = sitter

    def subsequence(self): 
        self.__diseasse()
        self.__names()
        return ''
    
    def __diseasse(self): 
        print("Врач " + self.doctor + " лечит пациента " + self.name + " с больезнью " + self.disease)
        
    def __names(self): 
        print("В больнице лежит " + str(self.patients) + " пациента " + self.sitter + " присматривает за ними ")

       
class Error(Exception):
    def __str__(self):
        return "Строка должно состоять из целых цифр"

try:
    h = Hospital(22, 'Баранов Виктор', 'Ульянов Кирил', 'восполение лёгких', 'Стирманов Сергей')
    h.subsequence() 
except Error as e:
    print(e)


