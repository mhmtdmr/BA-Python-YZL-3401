####################  Tupple  ###################
# # tuple tanımlama
# sabitListe = ()
# sabitListe = tuple()
# sabitListe = (1,6,5,42,'A','B','C')

# print(sabitListe)
# #listdeki fonksiyonlar geçerli. değer değiştirme atama işlemleri hariç!!!
# print(sabitListe[0])
# #  sabitListe[0] = 19 # hatalı

# liste = list(sabitListe)
# liste[0] = 19
# print(liste)

###########     Set: Küme     ##########
# #set tanımlama
# kume = {}
# kume = set()
# kume = {1,2,3,"A"}

# kume.add(4) # kümeye ekleme yapar.
# kume.remove("A") #kumeden sülme yapar Eleman yoksa KeyError verir.
# kume.discard(1) # kumeden silme yapar. Eleman yoksa hata verme.
# # kume.remove(1)
# kume.discard(1)

# kume1 = {1,2,3,4,5}
# kume2 = {6,7,8,1,2}

# kumeFark = kume1 -kume2
# kumeFark = kume1.difference(kume2)
# print("kume1'in kume2 den farkı: ",kumeFark)

# kumeKesisim = kume1 & kume2
# kumeKesisim = kume1.intersection(kume2)
# print("kume1, kume2 kesişimi",kumeKesisim)


# kumeBirlesim = kume1.union(kume2)
# print("Kümeler birleşimi:",kumeBirlesim)

# print(kume1.issubset(kume2)); #kume1 kume2 nin alt kümesi mi?
# print(kume1.issuperset(kume2)); #kume1 kume2 nin üst kümesi mi?
# print(kume1.isdisjoint(kume2)); # kume1 ve kume2 yrık kümeler mi?

# kume = {123,123,123,123,123,456,321}
# print(kume)
# 1-20 arasında 10 sayı üretip bir kümeye atın. Ancak kümedeki eleman sayısı mutlaka 10 olsun.
# from random import randint
# kume = set()

# for i in range(10):
#     while(True):
#         s = randint(1,20)
#         if(s not in kume):
#             kume.add(s)
#             break # sayı listede yoksa listeye ekle ve while döngüsünden çık.

# print(kume)
# print(len(kume))




### ÇEŞİTLİ ÖRNEKLER ###
# 1-10 arasında rastgele 5'er sayı üretip iki listeye atan ve daha sonra listenin elemanlarından kaçının
# aynı olup olmadığını ekrana yazdıran program.
# l1 ile l2'nin 1 ortak elemanı vardır.

# import random
# l1 = list()
# l2 = list()
# sayac = 0
# for i in range(5):
#     s1= random.randint(1,10)
#     l1.append(s1)
#     s2= random.randint(1,10)
#     l2.append(s2)

# print(l1)
# print(l2)

# for sayi in l1:
#     if(sayi in l2):
#         sayac+=1

# print("l1 ve l2 listelerinde aynı olan eleman sayısı :",sayac)
    









# 1-100 arasında 20'şer adet rastgele sayı üretip bunları 2 kümeye aktaran ve 
# bu iki kümenin: farkını, kesişimini ve birleşimini ekrana yazdıran program.

from random import randint


k1 =  set()
k2 =  set()

for i in range(20):
    while(True):
        s =randint(1,100)
        if(s not in k1):
            k1.add(s)
            break
    while(True):
        s =randint(1,100)
        if(s not in k2):
            k2.add(s)
            break

print("Kesişim : ",k1.intersection(k2))
print("Birleşim : ",k1.union(k2))
print("Fark : ",k1.difference(k2))



