"""
Programımızda belirli bir işi yapan kod bloklarının tekrar kullanılması durumunda tekrar yazılmadan çağırılmasını sağlayan modüllerdir.
Yani bir modülü 1 defa tanımlayıp istediğimiz kadar kullanabilmemizi sağlar.
Fonksiyonlar yazdığımız programın modüler olmasını sağlar, ayrıca okunabilirliği artırır.
"""

# Metod/Fonksiyon tanımlama

# def metodIsmi():
    # fonksiyon çağırıldığında çalışacak kodlar
    # fonksiyon çağırıldığında çalışacak kodlar
    # fonksiyon çağırıldığında çalışacak kodlar


# metodu tanımladık.
# def Merhaba():
#     print("Merhaba")

# # metodu çağırdık.
# Merhaba()
# Merhaba()
# print("Dünya")
# Merhaba()


# metoddan değer döndürmek
# kullanıcıdan int tipinde sayı alma işlemini bir metod olarak yazınız.ismi: inputInt

from traceback import print_tb


def inputInt() -> int:
    number = int(input("number:"))
    return number # kullanıcıdan alınan sayıyı döndür.

def inputInt2() -> int:
    number1 = int(input("number1:"))
    number2 = int(input("number2:"))
    return number1,number2 # kullanıcıdan alınan 2 sayıyı sıralı olarak döndürdük.

def inputLogin() -> str:
    email = input("Email:")
    passw = input("Password:")
    return email,passw

def inputPerson() -> dict:
    person = dict()
    person["name"] = input("name:")
    person["surname"] = input("surname:")
    person["birthyear"] = input("birthyear:")
    person["salary"] = input("salary:")

    return person 

# sayi = inputInt() # metoddan döndürülen sayıyı değişkene ata.
# print(sayi)

# s1,s2 = inputInt2() #metottdan döndürülen sayıları sıralı olarak değişkenlere atadık.
# print("s1",s1)
# print("s2",s2)

# # kullanıcıdan eposta ve parola bilgisini alıp döndüren metodu yazınız. inputLogin()
# email,password = inputLogin()
# print(f"email:{email}")
# print(f"password:{password}")

#kullanıcıdan ad,soyad,dogumyili,cinsiyet,maas bilgilerini isteyip bunları bir dictionary döndüren metodu yazınız. inputPerson

# person = inputPerson()
# for item in person.values():
#     print(item)


########################
# PARAMETRELİ METOTLAR #
########################


def topla(sayi1,sayi2):
    toplam = sayi1+sayi2 # parametre olarak alınan sayıları topla
    return toplam # toplamı döndür.

toplam = topla(19,35)
print("toplam:",toplam)
print("toplam:",topla(2,35))


# SORU: parametre olarak alınan 2 sayıyı yine parametre olarak alınan işlem bilgisine göre işleme sokup
# sonucu döndüren metodu yazınız.
# Örnek: islemYap(4,5,"carp") => 20,islemYap(4,5,"topla") => 9

def islemYap(s1,s2,islem):
    if(islem=="carp"):
        return s1*s2
    elif(islem=="topla"):
        return topla(s1,s2) # içiçe fonksiyon kullanımı
    elif(islem=="cikar"):
        return s1-s2
    elif(islem=="bol"):
        # if(s2!=0):
        #     return s1/s2
        # else:
        #     return "bölmede bölen 0 olamaz!"
        try:
            return s1/s2
        except ZeroDivisionError:
            return "bölmede bölen 0 olamaz!"

print(islemYap(9,0,"bol"))
print(islemYap(5,9,"topla"))











