###################################################
################ TİP DÖNÜŞÜMLERİ ##################
###################################################
# strS1 = "777"
# strS2 = "333"

# toplam = strS1 + strS2
# print(f"toplam : {toplam} => tip : {type(toplam)}")


# toplam = int(strS1) + int(strS2)
# print(f"toplam : {toplam} => tip : {type(toplam)}")

# intS1 = int(strS1) # dönüştürdüğümüz veriyi bir değişkene atadık.
# intS2 = int(strS2) # str to int
# toplam = intS1 + intS2
# print(f"toplam : {toplam} => tip : {type(toplam)}")
################################

# intS3 = 1988
# strS3 = str(intS3) # int to str

# fltS3 = float(intS3) # int to float

################################

# isim = ""
# isimKontrol = bool(isim)  # str to bool
# # False . Eğer karakter olsaydı True
################################
## Python False değerler: "",0,0.0,False,None
################################

# harf = chr(65) # 65 sayısının ASCII tablosundaki karşılığını getirir.
# print(harf) # A

# sayi = ord('A') # A harfinini ASCII tablosundaki sayısal karşılığını döndürür.
# print(sayi)

################################

# z = True
# s = str(z) # bool to str
# print(s)
################################
#  16: lık sayı sisteminde rakamlar: 0 1 2 3 4 5 6 7 8 9 A B C D E F
harf = 'D' # 16 lık sayı sisteminde bir sayı olsun.
sayi = int(harf,base=16)
print(sayi)
harf = 'ABCD' # 16 lık sayı sisteminde bir sayı olsun.
sayi = int(harf,base=16)
print(sayi)
binaryStr = '00001010' # 2 lik sayı sisteminde bir sayı olsun.
sayi = int(binaryStr,base=2)
print(sayi)

# https://codeshare.io/BA3401