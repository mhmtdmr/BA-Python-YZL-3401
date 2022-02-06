from datetime import date, datetime


class Teacher:
    db = dict()
    def __init__(self,tid=0,fullname="",birthday=date(1970,1,1)):
        """ This is Teacher class. """
        self.ID  = tid
        self.FullName = fullname
        self.Birthday = birthday
        
        # Öğretmeni veritabanına(db dictionary) kaydettik.
        Teacher.db[self.ID] = {"id":self.ID,"fullname":self.FullName,"birthday":self.Birthday}

    # instance method
    def GetAge(self):
        year = datetime.now().date()
        age = year - self.Birthday.year
        return age
    
    @classmethod
    def ListTeacherNames(cls):
        for teacher in cls.db.values():
            print(teacher["fullname"])
    
    @staticmethod # sınıf veya nesne ile ilgili herhangi bir işi olmayan metotlar
    def GetSalaryTax(salary):
        return salary*0.18


        

    
    
