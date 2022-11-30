#идёт работа
class Hospital(): #перегрузка
    def __init__(self, patients):
        self.patients = patients
        
    def Workload(self):
        print(f"Количество больных новым вирусом в больнице {self.patients}")
    
    def ede(self):
        return self.__patients
    
    def __add__(self, other):
        new = Hospital(self.patients)
        new.patients += other.patients
        return new

a = Hospital(12)
b = Hospital(25)
c = a+b
c.Workload()

