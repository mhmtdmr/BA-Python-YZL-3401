#Sınıfı tanımladık.

# class Student():
class Student:
    # Sınıf değişkeni tanımladık.
    db = dict()
    ClassCoder = "Mehmet Demir"
    ClassDetail = "Bu sınıf öğrenci bilgi sistemindeki öğrencileri tanımlamak için yazılmıştır."


    # # PARAMETRESİZ INIT METODU
    # def __init__(self): 
    #     # Oluşturulacak nesne özelliklerini tanımlamamızı ve bu alanlar için bellekte yer açılmasını sağlar.
    #     # Metoda gyazılan ilk parametre nesneyi temsil eder. Genellikle self kullanılır.
    #     self.Number = int()   # 0
    #     self.FullName = str() # ''
    #     self.PhoneNumber  = str()
    #     self.Email = str()

    # # PARAMETRELİ INIT METODU, Nesne Özellikleri
    def __init__(self,number=0,fullName='',phoneNumber='',email=''): 
        """
        Parameters:
        number: School number
        fullName: Student full name
        phonenUmber: Student phone number
        email: Student email address
        """
        self.Number = number
        self.FullName = fullName
        self.PhoneNumber  = phoneNumber
        self.Email = email

        self.Info = {"number":self.Number,"fullname":self.FullName,"phonenumber":self.PhoneNumber,"email":self.Email}


        Student.db[self.Number] = self.Info  
        # sınıf dictionary'sine ekleme yaptık.

        # Student.db[1] = 
        #   1 : {"number":1,"fullname":"Ahmet ÇELEBİ","phonenumber":"05461112233","email":"ahmet@gmail.com"}



    # Nesne metotları    
    def WriteInfo(self):
        """
        This method writes student info.
        """
        print(f"""
*****************************************
    Number :\t\t\t{self.Number}
    FullName :\t\t\t{self.FullName}
    PhoneNumber :\t\t{self.PhoneNumber}
    Email :\t\t\t{self.Email}
*****************************************

""")

    # Nesne metotları: Instance Methods
    def Update(self):
        Student.db[self.Number]["phonenumber"] = self.PhoneNumber
        Student.db[self.Number]["email"] = self.Email
        Student.db[self.Number]["fullname"] = self.FullName
        print(f"Student {self.FullName} is updated!")

    # Nesne metotları: Instance Methods
    def Delete(self):
        print(f"Student {self.FullName} is deleted! :(")
        del Student.db[self.Number]


    @classmethod    # Bu method sınıf metodudur!!!!!
    def DeleteByNumber(cls,number):
        if(number in cls.db.keys()):
            print(f" Student { cls.db[number]['fullname'] } is deleted! ")
            del cls.db[number]
        else:
            print("There is no student on db with this number !!!")

    @classmethod
    def Search(cls) -> Student:
        print("bla bla")
        # Öğrenci numarası,adı,emaili,telefon numarasına göre aranabilecek. Bulunursa nesne döndürülecek.
        #ÖDEV







    






# print("Burası Student.py",__name__)


if __name__=="__main__":  # Dosya doğrudan çalıştırıldıysa __name__ => __main__ olur.
    studentObject1 = Student() # Nesne tanımladık.
    studentObject1.Number = 220001
    studentObject1.FullName = "John Doe"
    studentObject1.Email = "john@doe.com"
    studentObject1.PhoneNumber = "02123441020"

    studentObject2 = Student()
    studentObject2.Number = 220002
    studentObject2.FullName = "Jane Doe"
    studentObject2.Email = "jane@gmail.coms"
    studentObject2.PhoneNumber = "+4567112244"



    studentObject2.FullName = studentObject1.FullName
    studentObject2.Number = studentObject1.Number
    studentObject2.Email = studentObject1.Email
    studentObject2.PhoneNumber = studentObject1.PhoneNumber

    print(id(studentObject1))
    print(id(studentObject2))

    studentObject1.WriteInfo()
    studentObject2.WriteInfo()



