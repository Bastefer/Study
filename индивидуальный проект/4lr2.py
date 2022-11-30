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

    def __add__(self, pandemia):
        self.patients += pandemia
        
        
    def __call__(self, pandemia):
        self.pandemia = pandemia

    def Workload(self):
        print(f"Количество больных новым вирусом {self.patients}")

class Error(Exception):
    def __str__(self):
        return "Строка должно состоять из целых цифр"
    

h1 = Hospital(22, 'Баранов Виктор', 'Ульянов Кирил', 'восполение лёгких', 'Стирманов Сергей')
h1.Workload()
h1+75
h1.Workload()
h1 + 170
h1.Workload()
