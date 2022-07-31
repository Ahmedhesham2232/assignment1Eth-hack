class Employee:
    def _init_(self,id,FirstName,LastName,Salary):
        self.id=id
        self.FirstName=FirstName
        self.LastName=LastName
        self.Salary=Salary

    
    
    def setid(self,id):
        self.id=id
    
    def getid(self):
        return self.id
    
    def setFirstName(self,FirstName):
         self.FirstName=FirstName

    def getFirstName(self):
        return self.FirstName

    def setLastName(self,LastName):
        self.LastName= LastName

    def getLastName(self):
        return self.LastName

    def getFullName(self):
        return (self.getFirstName() + " " +self.getLastName())
    
    def setSalary(self,Salary ):        
        self.Salary = Salary

    def getSalary(self):        
        return self.Salary

    def getAnnualSalary(self):        
       return (self.getSalary() *12)
    def raiseSalary(self, percent):    
     self.Salary+=(self.Salary*(percent/100))    
     return self.Salary
    def Info(self):
        print(f" ID= {self.id} \n FullName= {self.getFullName()} \n Salary= {self.Salary}") 

employ =Employee()
employ.setid(1548)
employ.setFirstName('ahmed')
employ.setLastName('hesham')
employ.setSalary(6000)
employ.Info()
print(f"the AnnualSalary is = {employ.getAnnualSalary()}")
