# veritabanındaki person tablosuna karşılık gelen sınıfımız.
class Person:
    def __init__(self,pid:int=0,name:str="",surname:str="",age:int=0):
        self.ID = pid
        self.Name = name
        self.Surname = surname
        self.Age = age

    # obje doğrudan print edildiğinde objenin adresi yerine Ad SOyadını göster.
    def __str__(self) -> str:
        return self.Name+" "+self.Surname

if __name__=="__main__":
    test = Person(name="Jack",surname="Clark")
    print(test)
        
    
