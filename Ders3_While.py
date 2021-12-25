from time import sleep
from random import randint

# kosul = True
# # kosul = False
# while(kosul):
#   print("Koşul Çalıştı !!!")
#   print("Sonsuz döngü!")
#   sleep(1)

# print("Program sonlandı!!!")


# # Ekrana 10 defa merhaba yazdıran program.
# sayac = 1
# while(sayac<=10):
#   print("merhaba")
#   sayac+=1
#   sleep(0.5)

# # Ekrana 1-10 arasındaki sayıları yazdıran program.
# sayac = 1
# while(sayac<=10):
#   print(sayac)
#   sayac+=1
#   sleep(0.5)


# s=10
# kontrol = (s>5) and (s<15)
# kontrol = (s>5) or (s<15)
# while(s>5 and s<15):






# sayi = 9
# if(sayi%2==0):
#   print(sayi,"çifttir!")
# else:
#   print(sayi,"tektir!")

# # 1-100 arasındaki çift sayıları döngü ile yazdırın.
# s = 2
# while(s<=100):
#   print(s)
#   s+=2 # varolan değerine 2 ekledik.

# s = 1
# while(s<=100):
#   if(s%2==0):
#     print(s,end=" ")
#   s+=1 # varolan değerine 1 ekledik.

# # Kullanıcı T,C,X,B harflerinden başka değer girerse tekrar alalım.
# kontrol=True
# harf = ""
# while(kontrol):
#   harf = input("harf:")
#   h=harf.lower()
#   if(h=="t" or h=="c" or h=="x" or h=="b"):
#     kontrol = False
#   else:
#     print("Sadece T,C,B,X harflerinden 1 tanesini giriniz!")
  
# print("harf :",harf)

# # Yukarıdaki soru break ile.
# # Wifi: BA GUESS Parola: Kadikoy1bilge
# # kullanıcı 85 dışında bir değer girdiği sürece yeni değer alınsın ve ekrana yazdırılsın. 
# # 85 girerse program sonlansın.
# # 95 girerse ekrana yazılmasın ancak döngü devam etsin.
# while(True): # sonsuz döngü
#   sayi = int(input("sayı : "))
#   sleep(0.2)
#   if(sayi==85):
#     break # döngüden çıkmak için anahtar kelimemiz: break
#   elif(sayi==95):
#     continue # döngünün başına döndürür. satır: 74'e
#   print(sayi)

# print("program sonlandı!")



# Kullanıcı T,C,X,B harflerinden başka değer girerse tekrar alalım.
# while(True): # sonsuz döngü
#   harf = input("harf : ")
#   h=harf.lower()
#   if(h=="t" or h=="c" or h=="x" or h=="b"):
#     break # doğru harf girildi ise döngüden çık.
#   print("Sadece T,C,B,X harflerinden 1 tanesini giriniz!")
  
# print("harf :",harf)

# SORU: Kullanıcıdan alınan pozitif sayıların toplamını ekrana yazdıran programı yazınız.
# Negatif sayılar toplama dahil edilmeyecek
# Kullanıcı -1 girdiğinde toplam ekrana yazdırılıp
# program sonlanacak.

# pozToplam = 0
# while(True):
#   sayi = int(input("sayı:"))
#   if(sayi>0):
#     pozToplam += sayi
#   elif(sayi==-1):
#     break
# print("Toplam =",pozToplam)


# https://github.com/
# https://desktop.github.com/
# Github Test

# Kullanıcıdan sayı adedi isteyip o kadar sayı alınaarak.
# Sayıların karelerini toplayıp ekrana yazdırın.
# kareToplam = 0
# try:
#   adet = int(input("Kaç sayı girilsin: "))
# except:
#   print("Hatalı veri girişi !!!")

# i = 1
# while(i<=adet):
#   try:
#     sayi = int(input("s : "))
#     kareToplam += (sayi**2)
#     i += 1
#   except:
#     print("girilen sayı hatalı !!!")

# print("kareler toplamı : ",kareToplam)

  
# from random import randint
# rastGele = randint(0,100)
# print(rastGele)

# Rastgele üretilen sayıyı bulma oyunu. (0-100 aralığında)
# Kullanıcının başlangıçta 1000 puanı var.
# Her başarısız tahminde 50 puan azalacak.
# Eşitse puan ekrana yazdırılarak program sonlanacak.
# Opsiyonel: tahminden sonra yukarı aşağı yönlendirme yapılsın.


rastgele = randint(0,100)
puan = 1000
while(True):
  try:
    tahmin = int(input("tahmin : "))
  except:
    print("Hatalı veri girişi !!!")
    break

  if(tahmin==rastgele):
    print(f"Tebrikler buldunuz sayı {rastgele} idi.Puanınız: {puan}")
  else:
    puan -= 50
    if(tahmin>rastgele):
      print("Daha küçük !!!")
    else:
      print("Daha büyük !!!")
  


