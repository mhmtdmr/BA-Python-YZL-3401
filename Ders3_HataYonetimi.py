"""
ValueError: veri tipi uymadığında.
#Import error: içeri aktarılmaya çalışılan modül aktarılırken bir hata oluşursa.
#ModuleNotFoundError: içeri aktarılmaya çalışan modül yerinde yoksa bu hata üretilir.
#MemoryError: Bellek programa yetmediği zaman üretilir.
#ZeroDivisionError: 0'a bölünme hatası.
#OverflowError: bir değişkene kapasitesinden fazla değer atamak istediğimizde üretilen hatadır.
#IndexError: 4 elemanlı bir listenin 5. elemanına ulaşmaya çalıştığımızda bu hata ile karşılaşırız.
#NameError: name 'x' is not defined : Tanımsız bir değişken veya eleman çağırıldığında.
TypeError: farklı tiplerde veriler birlikte işleme sokulduğunda.
SyntaxError: yazım hatası
"""

# # Veri tipi uyuşmazlığından TypeError verir.
# s1 = "15"
# s2 = 20

# try:
#   toplam = s1 + s2
#   print(toplam)
# except:
#   print("Bir hata oluştu!")

# # Hata detaylarını ekrana yazdırmak istersek.
# try:
#   toplam = s1 + s2
#   print(toplam)
# except Exception as hata:
#   print("Bir hata oluştu! Detay:",hata)

# finally: Hata oluşsa da oluşmasa da çalışacak kod bloğu

# try:
#   toplam = s1 + s2
#   print(toplam)
# except:
#   print("Hata oluştu !")
# finally:
#   print("Try except bloğu sonlandı.")

# HATA DETAYINA GÖRE EXCEPTION

# bolunen = 20
# bolen = 2
# try:
#   bolum = bolunen//bolen
#   print(bolum)
# except ZeroDivisionError as hata:
#   print("Bolen sayı 0 olamaz !(bolen 1 oalrak değiştirilmiştir.)")
#   bolum=bolunen/1
#   print(f"Bolum: {bolum}")
# except TypeError as hata:
#   print("Bolunen ve bolen sayı olmalıdır !!!",hata)
# except SyntaxError:
#   print("Yazım hatası var !!!")
# except:
#   print("Bir hata oluştu !")
# https://codeshare.io/BA303
# SORU: Kullanıcıdan 2 tane sayı 1 de harf alacağız.
# Sayılar: harf T ise toplama,C ise cıkarma,B ise bölme,X ise çarpma işlemine sokulacak.

# # ZeroDivisionError yakalanıp 0 yerine tekrar sayı istenecek.
# # İşlem 1 kez daha denecek.
# # Bunun dışındaki hataları yakalamak için de bir except yazılacak.
# try:
#   s1 = int(input("s1:"))
# except ValueError:
#   print("rakamlardan oluşan veri girmediniz !!!")
# try:
#   s2 = int(input("s2:"))
# except ValueError:
#   print("rakamlardan oluşan veri girmediniz !!!")

# harf = input("Toplama : T\nÇıkarma : C\nÇarpma : X,\nBölme : B  =>")
# if(harf.lower()=="t"):
#   print("Toplam = ",(s1+s2))
# elif(harf.upper()=="C"):
#   print("Fark = ",(s1-s2))
# elif(harf.lower()=="x"):
#   print("Çarpım = ",(s1*s2))
# elif(harf.lower()=="b"):
#   try:
#     bolum = s1/s2
#     print(bolum)
#   except ZeroDivisionError:
#     print("Bolen 0 olmamalıydı !!!")
#   except:
#     print("Beklenmeyen  bir hata oluştu.")


##############################################
########    MANUEL HATA FIRLATMA     #########
##############################################

# try:
#   dersNot = int(input("Not = "))
# except ValueError:
#   print("Hatalı değer !!!")

# if(dersNot<0 or dersNot>100):
#   # raise Exception("HATALI NOT ARALIĞI !!!")
#   raise OverflowError("HATALI NOT ARALIĞI !!!")


# ASSERT
eposta = input("Doğru-posta adresini giriniz:") # bilge@adam.com girilmezse AssertionError üretir.
assert eposta == "bilge@adam.com"
print("Eposta doğru girildi")

