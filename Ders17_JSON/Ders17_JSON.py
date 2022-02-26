import json
from json import encoder

class Person:
    def __init__(self) -> None:
        self.Pid = 0
        self.Name = ""
        self.Surname = ""
        self.Age = 18
        self.IsActive = True
        self.Size = 0.0
        self.CurrentTeam = None
    
    def PrintInfo(self):
        print(f"""
        User Information
        ----------------
        Name: {self.Name}
        Surname: {self.Surname}
        Age: {self.Age}
        IsActive: {self.IsActive}
        Size: {self.Size}
        Current Team: {self.CurrentTeam}
        """)

if __name__=="__main__":
    # filePath = "C:\\Users\\Bilge Adam\\Desktop\\BA-Python-YZL-3401\\Ders17_JSON\\person.json"
    # personInFile = open(filePath,"r",encoding="utf-8")

    # personDictionary = json.load(personInFile)

    # print(personDictionary)
    # print(type(personDictionary))
    # # {'Pid': 15, 'Name': 'Michael', 'Surname': 'Çordan', 'Age': 29, 'IsActive': False, 'Size': 2.15, 'CurrentTeam': None}
    # # <class 'dict'>

    # personObject = Person()
    # personObject.Pid = personDictionary["Pid"]
    # personObject.Name = personDictionary["Name"]
    # personObject.Surname = personDictionary["Surname"]
    # personObject.IsActive = personDictionary["IsActive"]
    # personObject.Size = personDictionary["Size"]
    # personObject.CurrentTeam = personDictionary["CurrentTeam"]

    #     # # User Information  
    #     # # ----------------  
    #     # # Name: Michael     
    #     # # Surname: Çordan   
    #     # # Age: 18
    #     # # IsActive: False   
    #     # # Size: 2.15        
    #     # # Current Team: None
    # personObject.PrintInfo()

