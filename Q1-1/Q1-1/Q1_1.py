from cmath import pi


class Circle:

    def _init_(self , raduis):
        self.raduis = raduis

    def getRaduis(self):
        return self.raduis
    
    def setRaduis(self , raduis):
        self.raduis = raduis
    
    def Area(self):
        return pow(self.raduis , 2) * pi

    def Circumfernce(self):
        return 2 * pi * self.raduis

    def Info(self):
        print(f"Raduis = {self.raduis} \n Area = {self.Area()} \n Circumfernce = {self.Circumfernce()}")

cir = Circle()
redis=float(input("enter Raduis (float number)"))
cir.setRaduis(redis)
cir.Info()
