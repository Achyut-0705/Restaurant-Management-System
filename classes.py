"""

Restaurant Management System
All classes Used in the project

"""

class RESTAURANT:
    def __init__(self, name, address, owner):
        self.name = name
        self.address = address
        self.owner = owner
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    def getOwner(self):
        return self.owner
    def changeName(self, new_name):
        self.name = new_name
    def changeAddress(self, new_address):
        self.address = new_address
    def changeOwner(self, new_owner):
        self.owner = new_owner 
        
class ADMIN:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
    
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    def getName(self):
        return self.name
    def changeUsername(self, newUsername):
        self.username = newUsername
    def changePassword(self, newPassword):
        self.password = newPassword

class EMPLOYEE:
    def __init__(self, ECode, Name, Username, Password, Salary, DOA):
        self.Name = Name
        self.ECode = ECode
        self.Username = Username
        self.Password = Password
        self.Salary = Salary
        self.DOA = DOA
    
    def changePass(self, newPass):
        self.Password = newPass
    def changeUsername(self, newUsername):
        self.Username = newUsername
    def updateSalary(self, newSalary):
        self.Salary = newSalary
    def getName(self):
        return self.Name
    def getUsername(self):
        return self.Username
    def getPassword(self):
        return self.Password
    def getSalary(self):
        return self.Salary
    def getDOA(self):
        return self.DOA
    def getECode(self):
        return self.ECode

class ITEM:
    def __init__(self, ICode, IName, Price):
        self.ICode = ICode
        self.IName = IName
        self.Price = Price
    def getICode(self):
        return self.ICode
    def getIName(self):
        return self.IName
    def getPrice(self):
        return self.Price
    def updatePrice(self, newPrice):
        self.Price = newPrice
        