from datetime import datetime,date
from Ders12_Teacher import Teacher


class Student:
    db = dict()
    def __init__(self,sid=0,fullname="",birthday=date(2000,1,1),teacher:Teacher=None) -> None:
        self.ID = sid
        self.FullName = fullname
        self.Birthday = birthday
        self.Teacher = teacher # öğrencinin öğretmeni

        Student.db[self.ID] = {"sid":self.ID,"fullname":self.FullName,"birthday":self.Birthday,"teacher":self.Teacher}
    
    # instance method
    def GetAge(self):
        year = datetime.now().year
        age = year - self.Birthday.year
        return age


    