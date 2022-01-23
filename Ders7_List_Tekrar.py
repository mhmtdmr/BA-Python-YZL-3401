# # Değişkende veri tutma.
# sayi = 5
# print(sayi)
# sayi = 3.14
# print(sayi)
# sayi = "Yedi"
# print(sayi)
# sayi = False
# print(sayi)

# # Liste tanımlama
# sayilar = list() #list yapıcı metodu ile liste tanımlama
# sayilar.append(0)
# sayilar.append(1)
# sayilar.append(2)
# sayilar.append(3)
# sayilar.append(4)
# print(sayilar)
# sayilar += [5,6,7,8,9]
# print(sayilar)

# sayilar = [] # Köşeli parantez ile liste tanımlama
# sayilar = [12,23,34]
# sayilar.insert(0,10) # listenin en başına 10 ekle. 0.indise
# print(sayilar)
# sayilar.insert(2,155)
# print(sayilar)

# #Listeden veri alma
# print(sayilar[3])
# sonEleman = sayilar.pop() # indis belirtilmezse son elemanı alıp siler.
# print(sayilar)
# print(sonEleman)
# eleman2 = sayilar.pop(1)
# print(sayilar)
# print(eleman2)

# Kullanıcıdan şehir sayısını aldıktan sonra.
# Bu sayı kadar şehir ismini kullanıcıdan alıp cities 
# listesine ekleyin.

# cities = list()
# n = int(input("How many city will you enter?"))
# for i in range(n):
#     city = input(f"{i+1}. city:")
#     cities.append(city)

# print(cities)



# cities = ["istanbul","kars","izmir","manisa","konya"]
# indisIzmir = cities.index("izmir")
# # cities.pop(indisIzmir)
# print(indisIzmir)
# del cities[indisIzmir] # sadece izmir i siler
# del cities # listenin tamamını siler.
# print(cities)
# # cities.remove("izmir")

# #Çeşitli fonksiyonlar

# points = [40,100,70,58]
# points.sort() # puanları küçükten büyüğe sıralar.
# print(points)
# points.reverse() # listenin sıralamasını ters çevirir.
# print(points)

# print("min point:",min(points))
# print("max point:",max(points))
# print("sum. of points:",sum(points))
# print("length of points list:",len(points))
# print("average of points list:",sum(points)/len(points))

# listA = ["Mehmet",432,"1A"]
# listB = listA
# print(id(listA))
# print(id(listB))
# listA[0] = "Ahmet"
# print(listA)
# print(listB)
# print("------------------------------------")
# listC = listA.copy()
# listA[0] = "Cemşid"
# print(listA)
# print(listB)
# print(listC)
# print(id(listA))
# print(id(listB))
# print(id(listC))

# Kullanıcıdan 10 sayı alıp 0-100 arasında olanları bir listeye ekleyen programı yazıız.
# listeyi ekrana yazdırınız.

# alinanSayilar = list()
# for i in range(10):
#     sayi = int(input("sayı:"))
#     if(sayi>=0 and sayi<=100):
#         alinanSayilar.append(sayi)

# print(alinanSayilar)

