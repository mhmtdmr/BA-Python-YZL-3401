from queue import Full
from Student import Student

# print("Burası Run.py",__name__)

if __name__=="__main__":

    # # # PARAMETRESİZ INIT METODU.
    # student = Student()   # Nesne boş olarak(varsayılan değerleri ile) tanımlandı.
    # student.Number = 20220101
    # student.FullName = "John Doe"
    # student.Email ="john@gmail.com"
    # student.PhoneNumber = "+905461112211"


    # # # PARAMETRELİ INIT METODU
    student1 = Student(1,"Jane Doe","05462923058","mail.mehmetdemir@gmail.com")
    # print(student1.Info)
    # student1.WriteInfo()

    student2 = Student(2)
    student2.Email = "s2@gmail.com"
    # print(student2.Info)
    # student2.WriteInfo()

    student3 = Student(3,fullName = "Ahmet GÜRCAN")
    # print(student3.Info)
    # student3.WriteInfo()

    # print(Student.db.keys())
    # print(Student.db.values())
    # studentItems = Student.db.items()

    # for item in studentItems:
    #     print(item)



# (1, {'number': 1, 'fullname': 'Jane Doe', 'phonenumber': '05462923058', 'email': 'mail.mehmetdemir@gmail.com'})
# (2, {'number': 2, 'fullname': '', 'phonenumber': '', 'email': ''})
# (3, {'number': 3, 'fullname': 'Ahmet GÜRCAN', 'phonenumber': '', 'email': ''})


    # SInıf özelliklerine örnekler.
    # print(Student.ClassCoder) 
    # print(Student.ClassDetail)

    # UPDATE
    student3.Email = "ahmet@gurcan.net"
    student3.PhoneNumber = "02161112233"
    # print()
    # print()

    print(Student.db)
    student3.Update()       # Nesne metotları  
    # print()
    # print()
    # print(Student.db)
    # print()
    # print()

    student2.FullName = "Merve Sena CÜCELİ"
    student2.Update()       # Nesne metotları  
    print()
    print()
    # print(Student.db)


    # # # # DELETE
    # student2.Delete()       # Nesne metotları  
    # print()
    # print()
    # print(Student.db)

    # # Sınıf metotları , @classmethod: Nesneye gerek kalmadan kullanılabilir.!!!
    # Student.DeleteByNumber(3)
    # print()
    # print(Student.db)

    # Student.Search(fullname="Ahmet")
    
    # ogrenci = Student()
    # print(ogrenci.topla(5,6))




    # Adı Jane Doe olanları bul!
    myStudents = Student.Search(fullname="Jane Doe",email="ahmet@gurcan.net")
    
    # print(Student.db)
    # print(myStudents)
    


    Student.PrintStudentsCount()





### Dictionary hatırlama
    # Personel1 =  dict()
    # Personel1["id"]=1
    # Personel1["adsoyad"]="Mehmet CEYLAN"
    # Personel1["maas"]=15000
    # print(Personel1)
    # print()
    # print()
    # Personel2 =  dict()
    # Personel2["id"]=2
    # Personel2["adsoyad"]="Mehmet TEKER"
    # Personel2["maas"]=9000
    # print(Personel2)

    # print()
    # print()
    # Personels = dict()
    # Personels[Personel1["id"]] = Personel1
    # Personels[Personel2["id"]] = Personel2
    # print()
    # print()

    # print(Personels)

