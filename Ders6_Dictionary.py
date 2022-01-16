#############################################
############  Dictionary:dict  ##############
#############################################

# dict tanımlama


# sozluk = dict()
# sozluk = {"anahtar":"değer","anahtar2":"değer2","key3":"value3",4:"Dört","Beş":5,"notlar":[12,45,75,90]}


# dict elemanlarına erişim

# print(sozluk)
# print(sozluk["anahtar"])     # anahtar değer yoksa hata verir.
# print(sozluk.get("anahtar")) # anahtar değer yoksa hata vermez.
# notlar = sozluk.get("notlar")
# print(notlar,type(notlar))

# print(sozluk.items()) # sözlüğün anahtar değer ikililerini döndürür.
# print(sozluk.keys())  # sadece anahtarları listeler.
# print(sozluk.values())  # sadece değerleri listeler.

# for key in sozluk.keys():
#     # print(key,end="  ")
#     deger = sozluk.get(key)
#     print(deger)

# for val in sozluk.values():
#     print(val,end="  ")
# print()
# print("sozluk boyutu :",len(sozluk))

# s1 = {"ad":"Mehmet","soyad":"Demir"} 
# s2 = {"soyad":"Demir","ad":"Mehmet"} #s1 ile aynı
# s3= {"soyad":"Demir","ad":"Serhat"}  #s1 ile farklı


# coloursInTurkish = {"red":"al","white":"ak","green":"yeşil","blue":"mavi"}
# print(coloursInTurkish.values())
# colourEdit = {"red":"kırmızı","white":"beyaz"}
# coloursInTurkish.update(colourEdit)  # sozluüu güncelleme
# print(coloursInTurkish.values())

# # colourEdit.clear() # anahtar değer ikililerini siler.
# print(colourEdit)

# renkler = coloursInTurkish
# renkler = coloursInTurkish.copy()

# red = coloursInTurkish.pop("red") # değeri getir ve sozlukten ikiliyi sil.
# print(red)
# print(coloursInTurkish)

# sonRenk = coloursInTurkish.popitem() # son ikiliyi alır ve sözlükten siler.
# print(sonRenk)
# print(coloursInTurkish)



###   ÖRNEKLER   ###

# personel = {"ad":"","soyad":"","netmaas":0.0,"dogumyili":1990}
# personel["ad"] = input("ad:")
# personel["soyad"] = input("soyad:")
# personel["netmaas"] = float(input("net maaş:"))
# personel["dogumyili"] = int(input("doğum yılı:"))

# for bilgi in personel.values():
#     print(bilgi)

# SORU
# Bir şirket için personel kayıt yazılımı yazıyoruz.
# Başlangıçta şirketten personel sayısını isteyip.
# her personel için yukarıdaki bilgileri aldıktan sonra yukarıdaki gibi bir dict yapısına kaydedin.
# dict'de personel ID si anahtar olacaktır. ve otomatik artacaktır.

# {1:{"ad":"Selin","soyad":"KARACA","netmaas":5000.0,"dogumyili":1990},2:{"ad":"Selim","soyad":"USTABAŞI","netmaas":7000.0,"dogumyili":1980}}

# personeller = dict()
# personelSayisi = int(input("personel sayısı : "))

# for i in range(1,personelSayisi+1):
#     personel = {i:{"ad":"","soyad":"","netmaas":0.0,"dogumyili":0}}
#     personel[i]["ad"] = input("ad:")
#     personel[i]["soyad"] = input("soyad:")
#     personel[i]["netmaas"] = float(input("net maaş:"))
#     personel[i]["dogumyili"] = int(input("doğum yılı:"))

#     personeller.update(personel) 


# for key in personeller.keys():
#     print(f"personel n:{key} => {personeller.get(key)}"
#     )


# ÖNBİLGİ # olmayan anahtarı listeye ekleme
# words = dict()
# words["apple"] = "Elma"
# anahtar = "banana"
# words[anahtar] = "Muz"
# print(words)

#SORU
# liste olarak tutulan ingilizce kelimelerin türkçelerini kullanıcıdan alıp bir dictionary'ye kaydedip gösteren programı yazınız.

# fruitsList = ["cherry","tomato","orange"]
# fruitsDict = {"cherry":"kiraz","tomato":"domates","orange":"portakal"}

#1 listenin elemanlarına tek tek ulaş.
#2 Her bir eleman için bir türkçe karşılık al.
#3 bu ikiliyi dictionary'ye kaydet.


# fruitsList = ["cherry","tomato","orange"]
# fruitsDict = dict()
# #1,2,3
# for item in fruitsList:
#     itemInTr = input(f"{item} kelimesinin türkçesi : ")
#     fruitsDict[item] = itemInTr

# print(fruitsList)
# print(fruitsDict)

#SORU

# 1-10 arasında rastgele 5'er sayı üretip iki listeye atan ve daha sonra listenin elemanlarından 
# iki listede ortak olmayanları başka bir listeye atarak ekrana yazdıran program.
# Örn: l1 = [11,22,33,44,55] l2 = [55,66,77,88,99]  l3 = [11,22,33,44,66,77,88,99]


# import random
# list1 = list()
# list2 = list()
# list3 = list()
# # sayıları ürettik.
# for i in range(5):
#     s1 = random.randint(1,10)
#     list1.append(s1)
#     s2 = random.randint(1,10)
#     list2.append(s2)

# for item in list1: # list1 in elemanlarına tek tek ulaştık.
#     if(item not in list2): #eleman list2'de yoksa list3'e ekledik.
#         list3.append(item)

# #yukarıdaki işlemi list2 elemanları için yaptık.
# for item in list2:
#     if(item not in list1):
#         list3.append(item)

# print(list1)
# print(list2)
# print(list3)


from traceback import print_tb

print("SET TO LIST")

kume = {1,2,3,4,5,5,5}
print(kume,type(kume))
liste = list(kume)
print(liste,type(liste))


print("LIST TO SET")
liste = [1,2,3,4,5,5,5]
kume = set(liste)

print(liste,type(liste))
print(kume,type(kume))



