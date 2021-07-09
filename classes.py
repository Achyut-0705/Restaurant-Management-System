"""

Restaurant Management System
All classes Used in the project

"""
class RESTAURANT:
    def __init__(self, name, address, owner):
        self.name = name
        self.address = address
        self.owner = owner
        
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
        
    def changeUsername(self, newUsername):
        self.username = newUsername

    def changePassword(self, newPassword):
        self.password = newPassword


class EMPLOYEE:
    def __init__(self, ECode, Name, Username, Password):
        self.Name = Name
        self.ECode = ECode
        self.Username = Username
        self.Password = Password

    def changePass(self, newPass):
        self.Password = newPass

    def changeUsername(self, newUsername):
        self.Username = newUsername


class ITEM:
    def __init__(self, ICode, IName, Price):
        self.ICode = ICode
        self.IName = IName
        self.Price = Price
        
    def updatePrice(self, newPrice):
        self.Price = newPrice
