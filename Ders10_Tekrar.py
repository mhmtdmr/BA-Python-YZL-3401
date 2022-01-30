# Veri tipleri

str
float
int
bool
complex

# a = "Yüz" #str
# print(type(a))
# a = 100 # int
# print(type(a))
# a = 100.0 # float
# print(type(a))
# a = True # bool
# print(type(a))
"""
<class 'str'>
<class 'int'>  
<class 'float'>
<class 'bool'> 
"""

# floatSayi = 34.3
# intSayi = int(floatSayi) # int'e dönüşüm
# floatSayi = float(intSayi) # float'a dönüşüm.
# strSayi = str(floatSayi) # str ye dönşüm.
# boolSayi = bool(strSayi) # bool'a dönüştür.
# print(boolSayi,strSayi)

"""
The following values are considered false in Python:

None
False
Zero of any numeric type. For example, 0, 0.0, 0j
Empty sequence. For example, (), [], ''.
Empty mapping. For example, {}
objects of Classes which has __bool__() or __len()__ 
method which returns 0 or False
"""

# kontrol = 45<34 # 45 34'ten küçükse True değilse False
# print(kontrol)


### string interpolasyon.

# isim = "Nurcan"
# yas = 30
# telefon = "02122221133"
# bilgiler = isim +" "+ str(yas)+" "+ telefon
# print(bilgiler)
# bilgiler = f"{isim} {yas} {telefon}"
# print(bilgiler)
# bilgiler = "{0} {1} {2}".format(isim,yas,telefon)
# print(bilgiler)

# bicimliYazi = """
# *****************
# **** Kadıköy **** 
# **** Bilge   **** 
# **** Adam    ****
# *****************
# """
# print(bicimliYazi)


# Hata Yönetimi

# try:
#     print("Merhaba,hatasız merhaba")
# except Exception as hataDetayı:
#     print("Merhaba hata oluştu!.")
#     print(hataDetayı)
# finally:
#     print("Burası her koşulda çalışır.")



# try:
#     sonuc = 100/0
# except:
#     print("Bir hata oluştu!")
# finally:
#     print("try except sonlandı!")

# print("Hatası ile program devam ediyor.")



#ValueError: veri tipi uymadığında.
#Import error: içeri aktarılmaya çalışılan modül aktarılırken bir hata oluşursa.
#ModuleNotFoundError: içeri aktarılmaya çalışan modül yerinde yoksa bu hata üretilir.
#MemoryError: Bellek programa yetmediği zaman üretilir.
#ZeroDivisionError: 0'a bölünme hatası.
#OverflowError: bir değişkene kapasitesinden fazla değer atamak istediğimizde üretilen hatadır.
#IndexError: 4 elemanlı bir listenin 5. elemanına ulaşmaya çalıştığımızda bu hata ile karşılaşırız.
#NameError: name 'x' is not defined : Tanımsız bir değişken veya eleman çağırıldığında.
#TypeError: farklı tiplerde veriler birlikte işleme sokulduğunda.
#SyntaxError: yazım hatası

# from Ders9_LOGGER import LogWriter
# try:
#     # print("Benim adım:",isim)
#     print("Burada çeşitli işlemler olacak.")
#     sonuc = 9/0
# except ZeroDivisionError as hata:
#     hataDetay = "HATA : Sıfıra bölme hatası!"
#     LogWriter(hataDetay)
#     print("Sıfıra bölme yapmayalım lütfen!!!")
#     print(hata)
# except MemoryError as hata:
#     hataDetay = "HATA : Yetersiz bellek!"
#     LogWriter(hataDetay)
#     print("Bilgisayar belleği yetersiz. Lütfen gereksiz uygulamaları kapatı tekrar deneyin!")
#     print(hata)
# except NameError as hata:
#     hataDetay = "HATA : Tanımlanmamış bir değişken kullanılmaya çalıştı!"
#     LogWriter(hataDetay)
#     print("Kullanmaya çalıştığınız bir değişken ya da metot ismi henüz tanımlanmamış gibi gözüküyor!!!")
#     print(hata)
# except Exception as hata:
#     print("Burası tüm hataları yakalayabilir. Yukarıdaki exception'lar dışındakileri ben yakalarım!!!")
#     print(hata)


# # Manuel olarak hata fırlatma!!

# # raise Exception("HATA")
# # raise MemoryError("Bellek Yetersiz!!!")


# # # # DÖNGÜLER  # # # #

# kosul = True
# sayac = 1
# while(kosul):
#     print("kosul True olduğu sürece çalışırım!!!")
#     sayac += 1
#     if(sayac == 10):
#         kosul = False # break


# range(3) # 0,1,2 değerlerini barındıran aralık.

# range(1,3) # 1,2 

# range(1,10,2) # 1,3,5,7,9

# for i in range(1,9,2):
#     print(i,end=" ")


# List,Tuple,Dictionary

# # List
# #Tanımlama
# myList = []
# myList = list()
# myList = [1,25,6,"Kadıköy",True,3.15]
# #Okuma
# print(myList)
# print(myList[0])
# print(myList[1])
# print(myList[-1])

# sonEleman = myList.pop() # son elemanı getir ve listeden sil.
# sonEleman = myList.pop(4) # listedeki 3 indisli elemanı getir ve sil.

# #Arama
# indisKadikoy = myList.index("Kadıköy")
# print(indisKadikoy)

# #Ekleme
# myList.append("sonEleman")
# myList.append(34)
# myList.insert(0,1988) #listenin başına ekleme yaptık.

# #Silme
# if("Kadıköy" in myList):
#     myList.remove("Kadıköy")

# del myList[1] # listenin 4. indisinin sil.
    
# print(myList)

# #List metotları
# print(len(myList))
# adet34 = myList.count(34)
# print(f"34 sayısı listede {adet34} defa tekrar ediyor.\nListenin eleman sayısı: {len(myList)}")
# myList = list()
# myList = [13,25,76,1,2,43,5,7]
# myList.sort() # küçükten büyüğe veya a dan z ye sıralama.
# print(myList)
# myList.reverse() # liste elemanlarını tersten sıralar.
# print(myList)


# tuple = listenin sadece okunabilir halidir.
# readOnlyList = tuple()
# readOnlyList = ()
# readOnlyList = (23,34,45)

# # dictionary

# personel1 = {"id":1,"ad":"John Doe","yas":"18","maas":5000.0}

# print(personel1["ad"])
# print(personel1["yas"])
# print(personel1["maas"])

# personel2 = {"id":2,"ad":"Jane Doe","yas":"28","maas":7000.0}


# personel3 = dict()
# personel3["id"] = 3
# personel3["ad"] = "Jenny Doe"
# personel3["yas"] = 25
# personel3["maas"] = 15000.0
# personel3["maas"] = 25000.0 # varolan veriyi değiştirdik.

# personeller = dict()
# personeller[personel1["id"]] = personel1
# personeller[personel2["id"]] = personel2
# personeller[personel3["id"]] = personel3

# print(personeller)
# print(personeller[1])

# print()
# print()

# print(personeller.keys()) # anahtarları listeler.
# print()
# print()
# print(personeller.values()) # değerleri listeler.
# print()
# print()
# print(personeller.items()) # anahtar ve değerleri listeler.
# print()
# print()

# print(personeller.get(4)) # key yoksa hata vermez: None üretir
# personeller[4] # key yoksa hata verir

# del personeller[1]




##################
#### Metotlar ####
##################

#1
# def Merhaba():
#     print("Merhaba Dünya")

# #2
# def Merhaba(isim:str="Ömer"):
#     print(f"Merhaba {isim}")
#3
# def Merhaba(*isimler):
#     # print(isimler,type(isimler))
#     for isim in isimler:
#         print(f"isim : {isim}")

#4
def Merhaba(isim,sayi=1):
    for i in range(sayi):
        print(isim)

#5
def ListSize(listItem:list) -> int:
    length = len(listItem)
    return length

#1
# Merhaba()

# #2
# Merhaba("Meliha")
# Merhaba()

# #3
# Merhaba("İbrahim","Gürdal","Yıldız")
# Merhaba("Ahmet","Mehmet")


# #4 
# Merhaba("Mehmet",3)
# Merhaba("Ahmet")

listem = [12,13,14]
lsize = ListSize(listem)
print(lsize)








