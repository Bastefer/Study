class LeapYear:
    def __init__(self, year):
        self.year = year
    
    def rodj(self):
        if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
            return f'год {self.year} високосный'
        else:
            return f'год {self.year} невисокосный'
        
fdf = LeapYear(1968)
print(fdf.rodj())
