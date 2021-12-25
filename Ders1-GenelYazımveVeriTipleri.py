# Tekli yorum satırı
"""
Çoklu 
yorum 
satırı
"""
####################################
### Değişken Tanımlama Kuralları ###
####################################
# # Sayı ve noktalama işaretleri ile başlayamaz!
# # (_ ile başlayabilir.)
# # Değişken içerisinde boşluk olmaz!
# # Sonunda toplama,çıkarma,çarpma,bölme gibi
# #   aritmetiksel işaretler olmaz.
# # Büyük küçük harf duyarlılığı vardır.
# # camelCase : 2. kelimeden sonraki her kelimenin ilk harfi büyük. => kullaniciYasBilgi
# # snake_case : kelimeler kküçük harf ile aralarında _ kullanılarak yazılır.
# # kebab-case : kelimeler arası - işareti ile.(Python da çalışmaz.)

# değişken tanımlama değer atama
degisAdi = "değer"
# sıralı atama.
degisken1,degisken2,degisken3 = "değer1","değer2",3


# sayi = 5
# Sayi = 10
# # Yukarıdaki ikisi farklı değişkenlerdir. S büyük olduğu için.







######################
###  Veri Tipleri  ###
######################
# isim = "Volkan"
# # Değişken içindeki veriyi ekrana yaz.
# print(isim)
# # Değişkenin bellek adresini ekrana yaz.
# print(id(isim))


# # Text types: str
# isim1 = "Ali" # str tipinde veri girişi " " arasıda yapılır.
# isim_1 = "Ali"
# print(type(isim_1)) # isim_1 değişkeninin tipini yazdırır.


# Numeric types: int,float,complex
intSayi = 145 # tam sayı olduğu için otomatik tip int olur.
print(type(intSayi),"<=",intSayi)

ondalikliSayiPi = 3.14
print(type(ondalikliSayiPi),"<=",ondalikliSayiPi)

complex = 1j
print(complex,"=>",type(complex))


# Boolen types : bool
kosul = True
kosul = False

# Sequence types: list,tuple,range
# Mapping types: dict
# Set types : set,frozenset
# Binary types: bytes,bytearray,memoryview

### ÖRNEK ###
s1 = 10
s2 = 45
toplam = s1+s2
print("Toplam =",toplam)



# print("""
# *****************************
# *****************************
#     1 tab içerideyiz.
#             3 tab içerideyiz.
#     Merhaba
# *****************************
# *****************************
#  """)

# isim = "Mehmet"
# soyad = "Demir"
# yas = 33
# okul = "Kocaeli Üniversitesi"

# print("Mehmet","Demir",33,"Kocaeli Üniversitesi")
# print(isim,soyad,yas,okul)
# print(f"{isim} {soyad} {yas} {okul}") # formatlı str verisi. string interpolasyon


# print("Kullanıcı adı :",isim,"soyadı :",soyad)
# print(f"Kullanıcı adı : {isim} soyadı : {soyad}")

# print("Kadıköy") # varsayılan olarak alt satıra atıyor.
# print("Sarıyer",end="  ")  # print ten sonra alt satıra geçmek yerine 2 boşluk bırakır.
# print("Beşiktaş")

# print("siyah","yeşil","beyaz") # sep=" " varsayılan olarak böyle olduğu için virgül ile yazılan ifadeler arasına boşluk otomATİK GELİR.
# print("siyah","yeşil","beyaz",sep=" * ") # virgül ile ayrılmış veriler arasına boşluk yerine * konulacak.
# print("satır1\nsatır2") # \n den sonra alt satırdan devam edilir.
# print("yazi\tyazi") # \t den sonra 1 tab(4 tane) boşluk bırakılır. yazi    yazi
# print(*"123456789", sep="x") # 1x2x3x4x5x6x7x8x9
# print("PC\n"*10) # 10 defa alt alta PC yazar.
# print("PC "*10) # 10 defa yan yana PC yazar.




