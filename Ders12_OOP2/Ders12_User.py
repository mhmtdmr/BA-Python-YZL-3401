class User:
    def __init__(self,uid=0,fullName="",email="",password="") -> None:
        self.ID = uid
        self.FullName = fullName
        self.Email = email
        self.Password = password
    
    def ChangePassword(self,newPassword:str):
        if(len(newPassword)<8):
            print("Password's length must have minimum 8 characters!!! ")
            print("FALSE")
            return False
        if(newPassword.isnumeric()):
            print("FALSE")
            return False
        if(newPassword.isalpha()):
            print("FALSE")
            return False
        return True

