from turtle import pos
from Ders12_Teacher import Teacher
from Ders12_Student import Student
from datetime import date

# teacher = Teacher(1,"Selahattin USTABAŞI",date(day=2,month=2,year=1965))
# student = Student(1,"John Doe",date(day=10,month=5,year=2005),teacher)

# print("Student Information\n********************\n")
# print("Full name: ",student.FullName)
# print("Birthday : ",student.Birthday)
# print("Age      : ",student.GetAge())
# print("Teacher Name:", student.Teacher.FullName)


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
#     Props:ID:int,Detail:str,LikeCount:int,Comments:list,User:User


from Ders12_User import User
from Ders12_Post import Post

# Kullanıcı tanımladık
user1 = User(uid=1,fullName="Jane Doe",email="jane@jane.com",password="Jane123")

# Kullanıcı parolasını değiştirdik.
user1.ChangePassword("cvb123123123..")

# Post tanımladık.
post1 = Post(pid=1,detail="Bugün hava çok güzel.",likeCount=100,dislikeCount=5,comments=[],user=user1)

post1.Detail = "Lorem Ipsum, dizgi ve baskı endüstrisinde kullanılan mıgır metinlerdir. Lorem Ipsum, adı bilinmeyen bir matbaacının bir hurufat numune kitabı oluşturmak üzere bir yazı galerisini alarak karıştırdığı 1500'lerden beri endüstri standardı sahte metinler olarak kullanılmıştır."

post1.AddComment("Harika bir yazı olmuş. Ellerinize sağlık!")
post1.AddComment("Harika bir yazı olmuş. Bravo!")


# print(post1)

post1.Print()


















