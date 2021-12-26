import random
from warnings import resetwarnings


# ARALIK TANIMLAMA
range(5)      # 0,1,2,3,4 # range(bitiş değeri)
range(2,5)    # 2,3,4     # range(başlangıç,bitiş)
range(1,9,3)  # 1,4,7     # range(başl.,bitiş,artış)

# # ekrana 5 defa merhaba yazan for döngüsü:
# for i in range(5): # aralıktaki her bir değer için 1 defa çalış.
#   print("merhaba")

# # 1-den 5'e kadar olan sayıları ekrana yazdıran for dng.
# for i in range(1,5):
#   print(i)

# for harf in "BEŞİKTAŞ":
#   print(harf,end="  ")

# #* 1-45(dahil) arasındaki sayıları toplayıp toplamı ekrana yaz.
# toplam = 0
# aralik = range(1,46)
# for i in aralik:
#   # print(i,end=" ")
#   toplam += i

# print(f"Toplam : {toplam}")



# Kullanıcıdan bir sayı alıp
# 1 ile bu sayı arasındaki sayıların karelerini
# for döngüsü ile yazınız.
# format=> "sayı: 5 karesi: 25 "

# try:
#   limit = int(input("sınır:"))
# except:
#   print("Hatalı veri girişi !")

# for i in range(1,limit+1):
#   print(f"sayı: {i} karesi: {i**2}")


# https://codeshare.io/BA303

# # Klavyeden girilen sayının rakamları toplamını yazd. for.
# toplam = 0
# sayi = input("sayı:") # "345" => 3 4 5
# for rakam in sayi:    # str sayinın karakterlerini tek tek ele al.
#   toplam += int(rakam) # karakteri int'e çevir: "3" => 3
# print("toplam :",toplam) # toplamı ekrana yazdır.

# # Klavyeden girilen metindeki karakterlerin ASCII tablosundaki decimal değerlerini ekrana yazdıran programı yazınız.
# yazi = input("yazı:")
# for i in yazi:
#   print(i," => ",ord(i))

# 97
# _ _ _ _ _ _ _ _ 
# 0 1 0 1 0 0 0 1 => ASCII a

# SORU: Kullanıcıdan 10 sayı alıp bu sayılardan tek olanları toplayp toplamı ekrana yazdıran programı yazınız.
# toplam = 0
# for i in range(10):
#   s = int(input("sayı:"))
#   if(s%2==1):     # sayının 2 ye bölümünden kalan 1 ise
#     toplam +=s    # toplama ekle.

# print(toplam)

# bir iş yerinde personelin çocuk sayısını öğrenen bir program yazıyoruz.
# Personel sayısı girildikten sonra
# her personel için çocuk sayısı girilecek
# ÖRNEK: 
# personelSayisi: 3
# 1. Personelin çocuk sayısı : 2
# 2. Personelin çocuk sayısı : 4
# 3. Personelin çocuk sayısı : 2
# Toplam çocuk sayısı: 8

# toplamCocukSayisi = 0
# personelSayisi = int(input("Personel sayınız: "))
# for i in range(personelSayisi):
#   cocukSayisi = int(input(f"i={i} => {i+1}. personelin çocuk sayısı: "))
#   toplamCocukSayisi += cocukSayisi
# print(f"Toplam çocuk sayısı: {toplamCocukSayisi}")
"""
i=0 => 1. personelin çocuk sayısı: 2
i=1 => 2. personelin çocuk sayısı: 4
i=2 => 3. personelin çocuk sayısı: 2
i=3 => 4. personelin çocuk sayısı: 1
i=4 => 5. personelin çocuk sayısı: 8
"""

# Kullanıcıdan alınan değerler arasında 10 tane sayı üretip ekrana yazdırın.
# ÖRNEK:
# altSinir : 5
# ustSinir  : 25
# => 6,5,14,13,12,21,22,23,24...

# altSinir = int(input("alt sınır:"))
# ustSinir = int(input("üst sınır:"))

# for i in range(10):
#   rastgeleSayi = random.randint(altSinir,ustSinir)
#   print(rastgeleSayi)


# SORU
# Üretilecek sayı aralığı:0-100
# Kullanıcıdan üretilecek sayı adetini aldıktan sonra.
# Üretilen sayıların aritmetik ortalamasını bulan program. 

# # Kullanıcı 0-20 aralığı dışında bir değer girerse program hata mesajını gösterek sonlansın.

# while(True):      # sonsuz döngü
#   count =int(input("number of numbers:"))
#   if(count<0 or count>20):
#     # raise Exception("Hatalı aralık !!!")
#     raise OverflowError("Hatalı aralık !!!")




# # Kullanıcı 20den büyük sayı giremesin Doğru girilene kadar sayı tekrar alınsın.
# while(True):      # sonsuz döngü
#   count =int(input("number of numbers:"))
#   if(count<0 or count>20):
#     print("0-20 aralığında değer giriniz!")
#     continue
#   else:
#     break

# sum = 0
# for i in range(count): # 5 => 0,1,2,3,4 
#   randomNumber = random.randint(0,100) # 0-100 arasında sayı ürettik
#   sum += randomNumber # üretilen sayıyı yoplama ekledik.
#   print(randomNumber,end=" ") #sayıyı ekrana yazdırdık.

# avg = sum//count # sayı üretme işlemi tamamlandıktan sonra ortalamayı hesapladık.
# print(f"Average of the numbers : {avg}")

# Level1:
# Rastgele sayılar aracılığı ile 5 harfli 5 kelime üretip ekrana yazdırın.
# Level2:
# Yukarıdaki soruya ek olarak her kelimenin ilk harfi büyük olsun.
# ASCII büyük harf aralığı: 65 - 90
# ASCII küçük harf aralığı: 97 - 122
# print(chr(65)) # => A


cumle = ""
kelime = ""
for i in range(5): # alttaki sorgunun 5 defa tekrar etmesini sağlar.

  kelime=""  # yeni kelimeye geçildiğinde kelime sıfırlansın.
  
  for i in range(5):  # 5 harfli kelime üretir
    harf = chr(random.randint(65,90))
    kelime+=harf

  cumle += kelime + " "
print(cumle)

