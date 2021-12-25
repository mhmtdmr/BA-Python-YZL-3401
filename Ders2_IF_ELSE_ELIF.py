
# # isim = input("İSİM GİRİNİZ:") # kullanıcıdan veri alabiliriz. str tipinde veri döndürür.
# # print(f"İsim : {isim}")

# s1 = input("s1:")
# s1 = int(s1) # str olarak aldığımız veriyi int e çeviridik.
# s2 = int(input("s2:")) # inputtan gelen veriyi doğrudan int fonksiyonuna göndererek sayıya çevirdik.
# # print(s1,type(s1))
# # print(s2,type(s2))
# toplam = s1 + s2
# print("TOPLAM : ",toplam)

# # SORU: Kullanıcıdan alınan sayının ASCII tablosundaki karakter karışılığını ekrana yazdırın.
# sayi = int(input("sayı:"))
# karakter = chr(sayi)
# print(f"{sayi} değerinini ASCII'deki karşılığı : {karakter}")

# ## Kullanıcıdan taban ve üs bilgisini alıp sayının o kuvveti ekrana yazdırın.
# taban = int(input("taban giriniz:"))
# us = int(input("üs giriniz:"))
# sonuc = taban**us
# print("Sonuç :",sonuc)


#########################################################################IF ELSE ELIF
# BLOK IÇLERİ: 1 tab yani 4 adet boşluk içeri gidilerek yazılır.
"""
sayi = 66
if(sayi>=10):
    print("Sayı 10'dan büyüktür")
    print("4 boşluk içerisi IF içerisidir.")
else:
    print("Bu blok ELSE bloğudur.")
    print("IF içerisindeki koşul sağlanmaz ise burası çalışır.")

print("Normal program bloğu.")
"""
# # NOT ARALIKLARI :45->59 : D, 60 -> 64: c, 65->74: B, 75->100:A
# dersNotu = 157
# dersHarf = ""
# if(dersNotu>=0 and dersNotu<45):
#     dersHarf="F"
# elif(dersNotu>=45 and dersNotu<=59):
#     dersHarf = "D"
# elif(dersNotu>=60 and dersNotu<=64):
#     dersHarf = "C"
# elif(dersNotu>=65 and dersNotu<=74):
#     dersHarf = "B"
# elif(dersNotu>=75 and dersNotu<=100):
#     dersHarf = "A"
# else:
#     print("Ders notu aralık dışında girildi !!!")
# print("Ders notunu:",dersHarf)


# Kullanıcıdan alınan sayının karesi: 100'den büyük ise 'KARE 100'DEN BÜYÜK'
# 100'den küçük ise 'KARE 100'DEN KÜÇÜK'
# 100'e eşit ise de 'KARE 100' yazdıran programı yazınız.

# sayi = input("sayı:")
# if(str.isnumeric(sayi)==True): # sayi değişkeninin içindeki veri nümerik mi
#     sayi = int(sayi)
#     kare = sayi**2
#     if(kare>100):
#         print("KARE 100'DEN BÜYÜK")
#     elif(kare<100):
#         print("KARE 100'DEN KÜÇÜK")
#     elif(kare==100):
#         print("KARE 100")
# else:
#     print("Hatalı değer girdiniz!!!\nLütfen sadece sayı giriniz!!!")

# SORU: Kullanıcıdan 2 tane sayı alınız. 
# * İki sayı da pozitif ise toplamlarını
# * İki sayıdan 1 tanesi negatif ise çarpımlarını
# * her ikisi de negatif ise farklarını ekrana yazdırınız.

# s1 = input("s1:")
# s2 = input("s2:")

# s1 = int(s1)
# s2 = int(s2)

# if(s1>0 and s2>0):
#     toplam = s1+s2
#     print(toplam)
# elif(s1<0 and s2<0):
#     fark = s1-s2
#     print(fark)
# elif(s1<0 != s2>0):
#     carpim = s1*s2
#     print(carpim)
# else:
#     print("Sayılardan en az 1 tanesi 0 !")


# Soru Kullanıcıdan isim, yaş ve çocuk sayısı alınsın.
"""
    Çocuk sayısına bakılacak. Çocuk başına 300 lira ekleme yapılacak. Ancak üst limit 4.    (Temel Maaş= 5000₺)
    Ayrıca personelin yaş 45 ve üzeri ise 500 TL ekleme yapılacak.
    Son olarak ekrana : "Nesrin Yılmaz, Maaşınız: 5300₺" yazılacak.  
"""

maas = 5000.0
isim = input("isim:")
yas = int(input("yas:"))
cocukSayisi = int(input("çocuk sayısı:"))
cocukPrimi = 300.0
if(yas>=45):
    maas += 500.0

if(cocukSayisi>=4):
    maas += (cocukPrimi*4)
else:
    maas += (cocukPrimi*cocukSayisi)

print(f"""
                        MAAŞ BİLGİLERİ
                        *************************
                        {isim}, Maaşınız: {maas}₺ 
                        *************************
""")
