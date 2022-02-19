class A:
    def __init__(self,name:str="") -> None:
        self.Name = name 

    def GetName(self):
        return self.Name

class B:
    def __init__(self,surname:str="") -> None:
        self.Surname = surname
    
    def GetSurname(self):
        return self.Surname


class C(A,B):
    def __init__(self,name:str="",surname:str="") -> None:
        A.__init__(self,name)
        B.__init__(self,surname)
    
if __name__ == "__main__":
    nesne = C("Ömer Ali","Kılıç")
    
    print(nesne.GetName())
    print(nesne.GetSurname())
