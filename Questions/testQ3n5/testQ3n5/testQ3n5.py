
from cmath import pi



class Circle:
    def _init_(self,radius,color):
        self.radius=radius
        self.color=color
    def getRadius(self):
        return self.radius
    def setRadius(self,radius):
        self.radius=radius     
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color=color
    def AreaCircle(self):
        return pi*self.radius*self.radius
    def toString(self):
        print(f"the radius is =  {self.radius} \n the color is =  {self.color}")



class Cylinder(Circle):  
    def _init_(self, radius, color,height):
        super()._init_(radius, color)  
        self.height=height
    def getHeight(self):
        return self.height
    def setHeight(self,height):
        self.height=height
    def getVolume(self):
        return self.AreaCircle()*self.height    


cyl=Cylinder(1.0,"red",1.0)
print(" Volume = ",cyl.getVolume())