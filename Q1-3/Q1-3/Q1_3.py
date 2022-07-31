
class Rectangle:
    def _init_(self , length , width):
      self.length = length
      self.width = width
    def getLenght(self):
        return self.length 
    def setlength(self, length):
        self.length=length     
    def getwidth(self):
        return self.width
    def setwidth(self,width):
        self.width=width
    def Area(self):
        return self.length * self.width    
    def Perimeter(self):
        return (self.length + self.width) * 2 
    def Info(self):
        print(f"Area = {self.Area()} \n Perimeter = {self.Perimeter()}")
    

rect = Rectangle()
L=float(input("enter lenght of rectangle"))
W=float(input("enter width of rectangle"))

rect.setlength(L)
rect.setwidth(W)
rect.Info()
