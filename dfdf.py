class TumbaYumba:
            
    def __init__(self, letter):
        self.letter = letter
        self.letters_num = 0
        self.amount()
        
    def myprint(self):
        print(self.letter)
        
    def amount(self):
        self.letters_num = len(self.letter)
    
    def printamount(self):
        print(self.letters_num)

    def example(self):
        print("Tumba Yumba Example:\nDeienaw v swnf uns efs")


fdf = TumbaYumba('QWERTYU')
fdf.example()
fdf.printamount()
fdf.myprint()