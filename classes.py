"""

Restaurant Management System

"""

from os import system as sys
sys("cls")

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
    def __inint__(self, name, username, password):
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


        