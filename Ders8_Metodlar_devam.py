# # harici modülü dahil etmek.

from pkg_resources import safe_extra
import Ders8_Matematik # import1 uzantı olmadan dosya adını belirttik. Bu dosyadaki sınıf tüm fonksiyonları dosya adı belirterek kullanabiliriz.

from Ders8_Matematik import Topla,Islem # import2 dosyadan sadece belirli metotları veya sınıfları içeri aktarmak istediğimizde.Kullanırken dosya adı belirtmeye gerek yok.

from Ders8_Matematik import * # import3 dosyadaki tüm sınıf ve metodları içeri aktar. Kullanırken dosya adı belirtmeye gerek yok.

from Ders8_ListModule import *


# # toplam = Topla(10,20)
# # print(f"toplam: {toplam}")
# a,b,c = 10,20,30 # sıralı atama: a=10,b=20,c=30

# T,F,C,B = Ders8_Matematik.Islem(40,20)  # import1 kullanım şekli.
# print(T)
# print(F)
# print(C)
# print(B)

# sonuc = Topla(99,101) # import2 kullanım şekli.

# sayi = SayiAl() # import3 kullanım şekli.
# print("Alınan sayı :",sayi)

# kare5 = Kare(5)
# print(kare5)

# kuvvet37 = Kuvvet(3,7)
# print(kuvvet37)



#içe içe metod kullanımı

# s = SayiAl()
# k = Kare(s)
# print(k)
# #aşağıdaki kod yukarıdaki ile aynı işi yapar.
# print(Kare(SayiAl()))



# ListeOrtalama([45,35,65,75])
liste = [45,35,65,75]
ortalama = ListeOrtalama(liste)
print(ortalama)

