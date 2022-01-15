# # List Tanımlama.
# sayilarim = []      # boş liste tanımladık.
# sayilarim = list()  # boş liste tanımladık.
# sayilarim = [10,20,30,15,25,35] # dolu liste tanımladık.

# # List içindeki verilere erişim.
# print("liste :",sayilarim) # tüm listeyi yazdır.
# print("listenin ilk elemanı :",sayilarim[0]) # sayilarim listesindeki 1. elemana eriştik.
# print("listenin 5. elemanı :",sayilarim[4]) # sayilarim listesindeki 5. elemana eriştik.
# print("listenin son elemanı :",sayilarim[-1]) # sayilarim listesindeki son elemana eriştik.


# # List'e veri ekleme
# sayilarim += [40,45,10]
# sayilarim.append(55)
# print("liste :",sayilarim) # tüm listeyi yazdır.
# sayilarim.insert(0,-100)
# sayilarim.insert(3,38)
# print("liste :",sayilarim) # tüm listeyi yazdır.


# #List'den veri silme.
# sayilarim.remove(40) # 40 sayısını listeden sil.
# print("liste :",sayilarim) # tüm listeyi yazdır.
# del sayilarim[3] # 3. indexteki veriyi siler.
# print("liste :",sayilarim) # tüm listeyi yazdır.


# # çeşitli fonksiyonlar
# boyut = len(sayilarim) # sayilarim listesinin eleman sayısını al.
# print("eleman sayısı :",boyut)

# listedeki10sayisi = sayilarim.count(10) # listedeki bir değerin kaç defa tekrar ettiğini bul.
# print("listedeki 10 sayısı :",listedeki10sayisi)

# indis55 = sayilarim.index(55)  # index ile bir değerin kaçıncı sırada(indis) olduğu bigisine erişiriz.
# print("55 sayısının indisi : ",indis55)


# indis10 = sayilarim.index(10)  # index ile bir değerin kaçıncı sırada(indis) olduğu bigisine erişiriz.
# print("10 sayısının indisi : ",indis10)

# indis10_2 = sayilarim.index(10,2)  # index'e vereceğimiz 2. parametre startindex değeri olacaktır ve aramaya bu indisten başlayacaktır.
# print("10 sayısının indisi : ",indis10_2)

# print("sıralamadan önce :",sayilarim)
# sayilarim.sort() # a-z , küçükten büyüğe
# print("sıralamadan sonra :",sayilarim)
# sayilarim.reverse(); # sıralamyı terse çevirir.
# print("reverse den sonra :",sayilarim)

# sonEleman = sayilarim.pop() # listedeki son elemanı getirir ve listeden siler.
# print(sayilarim)
# print(sonEleman)

# eleman4 = sayilarim.pop(3) # 3. indisteki elemanı döndürür ve listeden siler.
# print(eleman4)
# print(sayilarim)

# enKucuk = min(sayilarim)
# enBuyuk = max(sayilarim)
# toplam = sum(sayilarim)
# print("enKucuk",enKucuk)
# print("enBuyuk",enBuyuk)
# print("toplam",toplam)






# sehirler1 = ["İstanbul","Ankara","İzmir"]
# sehirler2 = sehirler1  # sehirler1 ile sehirler2 nin ram adresilerini eşitler.(yeni değişken tanımlamadı!)
# sehirler3 = sehirler1.copy() # sehirler1 deki verileri yeni adresteki değişkene kopyalar.
# print(id(sehirler1),sehirler1)
# print(id(sehirler2),sehirler2)
# print(id(sehirler3),sehirler3)

# sehirler1[2] = "Manisa"
# print(id(sehirler1),sehirler1)
# print(id(sehirler2),sehirler2)
# print(id(sehirler3),sehirler3)


# karisikListe = [156,"Kadıköy",True,14.12]


############################
        # ÖRNEKLER #
############################

# liste elemanlarına for döngüsü ile erişme
# listem = [10,20,30,40]

# for i in listem:
#     print(i) # listedeki elemanları tek tek yazdırdık.

# # liste elemanlarını for döngüsü ile ayarlama
# rakamlar = list() # boş bir liste tanımladık.
# for rakam in range(10): #0,1....8,9
#     rakamlar.append(rakam)

# # print(rakamlar)

# kareler = [] # boş liste tanımladık.
# for rakam in rakamlar: # rakamlar listesindeki her bir eleman için döngü 1 defa çalışır.
#     kareler.append(rakam**2) # rakam'ın karesini kareler listesine ekledik.

# print("rakamlar :",rakamlar)
# print("kareler  :",kareler)


# sokaklar = ["çiçek","bahar","kirazağacı","fıstıkağacı","sedir"]
# kontrol = "gül" in sokaklar # gül sokaklar listesinde varsa True yoksa False

# if("gül" not in sokaklar):
#     sokaklar.append("gül") #listede yoksa ekle.

# print(sokaklar)


###############
# SORULAR #
###############

# # #  Kullanıcıdan 10 sayı alıp bu sayıları bir listeye ekleyin. Son olarak listeyi ekrana yazdırın.

# sayiListesi = list()
# for i in range(10):
#     sayi = int(input("sayı:"))
#     sayiListesi.append(sayi)
# print(sayiListesi)


# # Yukarıda oluşturulan listedeki sayıları tek ve çift olmak üzere 2 ayrı listeye bölün. saiyListesi en sonda boş olacak.
# tekListe = list()
# ciftListe = list()
# sayiListesiBoyut = len(sayiListesi)
# for i in range(sayiListesiBoyut):
#     sayi = sayiListesi.pop() # listedeki son elemanı al. Listeden sil.
#     if(sayi%2==0):
#         ciftListe.append(sayi)
#     else:
#         tekListe.append(sayi)

# print("sayiListesi:",sayiListesi)
# print("tekListe:",tekListe)
# print("ciftListe:",ciftListe)





# ####  1-100 arasında 10 tane rastgele sayı üretip bir listeye atınız. Daha sonra kullancıdan 3 tahmin alıp girdiği sayıların listeden olup olmadığınız ekrana yazdırın.
# # Her doğru cevap için 100 puan verilsin. Eğer 3 tahmin de listede varsa bonus 200 puan verilsin. Ve son olarak oyuncunun puanı ekrana yazdırılsın.
    
# import random
# rastgeleListe = list()
# puan = 0

# #sayıları üret.
# for i in range(10):
#     r = random.randint(1,100)
#     rastgeleListe.append(r)
# rastgeleListe.sort()
# print("rastgeleListe :",rastgeleListe)

# #tahminleri al.
# for i in range(3):
#     tahmin = int(input("tahmin  :"))
#     if(tahmin in rastgeleListe):
#         puan += 100
#         print(f"{tahmin} listede var.")
#         if(puan==300):
#             puan+=200
#     else:
#         print(f"{tahmin} listede yok.")

# rastgeleListe.sort()
# print("rastgeleListe :",rastgeleListe)
# print("PUANINIZ : ",puan)



# girilen sayının listedeki herhangi bir sayıya tam bölünüp bölünmediğini döndüren program yazınız.

# liste = [2,4,5,7]
# sayi = int(input("sayı:"))
# kontrol = False
# for bolen in liste:
#     if(sayi%bolen==0):
#         kontrol=True

# print("Girilen sayı listedeki sayılara tam bölünüyor mu?:",kontrol)

########################
# ÇOK BOYUTLU LİSTELER #
########################


# rakamlar = [i for i in range(10)] #0,1,2,3,4,5,6,7,8,9 #tek satırda listeyi doldurduk.
# print(rakamlar)

# cokBoyutluListe = [[1,2,3],[10,20,30]]
# print(cokBoyutluListe[0]) #[1,2,3]
# print(cokBoyutluListe[1]) #[10,20,30]
# print(cokBoyutluListe[0][0]) #1
# print(cokBoyutluListe[1][0]) #10
# print(cokBoyutluListe[1][2]) #30
# cokBoyutluListe[1][1] = 100
# print(cokBoyutluListe)

# 
listenn = [[0]*5]*5 #5x5 lik bir liste.
print(listenn)

















