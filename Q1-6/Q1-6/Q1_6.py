class Account:
    balance=0
    def _init_(self,id,name,balance):
        self.id=id
        self.name=name
        self.balance=balance
    

    def setID(self,id):
         self.id = id
    def getID(self):
        return self.id

    def setName(self,name):
         self.name = name
    def getName(self):
        return self.name

    def setBalance(self,balance):
         self.balance= balance
    def getBalance(self):
        return self.balance
    def Credit(self,amount):
        self.balance += amount
        return self.balance
    def debit(self,amount):
        if(amount <= self.balance):
            self.balance -= amount
            return self.balance
        else:
            print("Amount exceed balance \n")
            return self.balance
    def TransferTo(self,amount,Account):
        if(amount <= self.balance):
            amount=Account
        else:
            print("Amount exxceed balance \n")
            return self.balance
    def Info(self):
        print(f" ID = {self.id} \n Name is = {self.name} \n Balance is {self.balance} ")
 
accon=Account()
accon.setID(1548)
accon.setName("ahmed hesham")
accon.setBalance(6000)
accon.Info()
