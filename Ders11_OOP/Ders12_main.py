from Ders12_Teacher import Teacher
from Ders12_Student import Student
from datetime import date

# teacher = Teacher(1,"Selahattin USTABAŞI",date(day=2,month=2,year=1965))
# student = Student(1,"John Doe",date(day=10,month=5,year=2005),teacher)

# print("Student Information\n********************\n")
# print("Full name: ",student.FullName)
# print("Birthday : ",student.Birthday)
# print("Age      : ",student.GetAge())
# print("Teacher Name:", student.Teacher.FullName


# static method kullanımı

# tax = Teacher.GetSalaryTax(5000)
# print(tax)

# ### SINIFLAR
# User: 
#     Props: ID,FullName,Email,Password
#     Methods: ChangePassword(self,newPassword=str) 
                # len(newPassword)>=8
#         # Parola kuralları: en az 8 karakter
#         #                   numara ve harf içersin
#         # parola uygunsa değiştir,ekrana değiştirildi yaz. True dönder.
#         # parola uygun değil ise hata yazdır. False dönder.


# Post:
    # Props:ID:int,Detail:str,LikeCount:int,Comments:list,User:User


from Ders12_User import User
user = User()
user.ChangePassword("cvb123123123..")



