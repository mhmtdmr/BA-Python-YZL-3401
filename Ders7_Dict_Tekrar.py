#############################################
############  Dictionary:dict  ##############
#############################################

# sozluk = dict()
# sozluk = {"anahtar1":"değer","anahtar2":"değer2"}

# personel1 = {"ID":1,"TC":"12332112321","AdSoyad":"Ahmet GÜLEÇ"}
# personel2 = {"ID":2,"TC":"12332112221","AdSoyad":"Gürbüz GÜLEÇ"}



# personeller = {1:personel1,2:personel2}
# print(personel1["ID"])
# print(personel1["TC"])
# print(personel1["AdSoyad"])

# #Sözlüğe veri okuma.
# print(personeller[1])
# print(personeller.get(5))

# print(personel1.keys())
# print(personel1.values())
  
# # veri ekleme           https://codeshare.io/BA303
# personel1["dogumYili"] = 1990
# personel1["ID"] = 5
# print(personel1)






# Kullanıcıdan 5 personel bilgisi alıp.Bunu yukarıdaki gibi birş personel listesine ekleyen programı yazınız.

# personeller = dict()
# ID_sayac = 1
# for i in range(5):
#     tc = input(f"{i+1}. personelin tc k. numarası: ")
#     adSoyad = input(f"{i+1}. personelin ad soyadı:")
#     personel = {"ID":ID_sayac,"TC":tc,"AdSoyad":adSoyad}
#     personeller[ID_sayac] = personel
#     ID_sayac+=1

# print(personeller)

# personeller = {
#     1: {'ID': 1, 'TC': '123', 'AdSoyad': 'Ahmet Urfalı'}, 
#     2: {'ID': 2, 'TC': '234', 'AdSoyad': 'Necla Sivaslı'}, 
#     3: {'ID': 3, 'TC': '345', 'AdSoyad': 'Murat Çelebi'}, 
#     4: {'ID': 4, 'TC': '456', 'AdSoyad': 'Reşat GÜRCAN'}, 
#     5: {'ID': 5, 'TC': '567', 'AdSoyad': 'Nurcan KARAKAŞ'}
# }
# for key in personeller.keys():
#     print(key)

# for val in personeller.values():
#     print(val)
#     # print(val["ID"],val["AdSoyad"],val["TC"])

# for item in personeller.items():
#     print(item,type(item))



# Kullanıcı çıkmak istermisiniz sorusuna evet yaxana kadar.
# aşağıdaki işi yapacak:
# ingilizce kelime gir.
# türkçesini gir.

# englishToTurkish = dict()
# while(True):
#     eng = input("word please: ")
#     tur = input(f"{eng} kelimesinin türkçesi lütfen: ")
#     englishToTurkish[eng] = tur
#     ans = input("çıkmak ister misiniz?:")
#     if ans.lower()=="evet":
#         print(englishToTurkish)
#         break

# englishToTurkish = {'phone': 'telefon', 'paper': 'kağıt'}

# extensionEngTur = {'phone':'cep telefonu','red':'kırmızı','line':'çizgi'}
# englishToTurkish.update(extensionEngTur)
# print(englishToTurkish)




