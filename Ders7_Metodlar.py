##### metod/fonksiyon #####
#parametresiz metodlar. örnek: veritabanı bağlantısı aç kapa
# def Metod(): # tanımladık.
#     print("Metod çalıştı!")

# Metod() # çağırdık.
# Metod() # çağırdık.
# Metod() # çağırdık.

# # parametreli metodlar. örnek: personeli veritabanına kaydetme işlemi.

# personeller = dict()
# personel_id_sayac = 1
# def PersonelKaydet(tc,adsoyad,maas):
#     global personel_id_sayac, personeller # yukarıda tanımlanmış olan değişkene metod içerisinden eriş.
#     personeller[personel_id_sayac] = {"TC":tc,"AdSoyad":adsoyad,"Maas":maas}
#     personel_id_sayac+=1

# def PersonelListele():
#     global personeller
#     for key in personeller.keys():
#         print(f"TC : {personeller[key]['TC']}" , end=" ")
#         print(f"Ad Soyad : {personeller[key]['AdSoyad']}" , end=" ")
#         print(f"Maaş: {personeller[key]['Maas']}")

# def PersonelBilgiGir():
#     tc=input("tc:")
#     adsoyad=input("ad soyad:")
#     maas = float(input("maas"))
#     PersonelKaydet(tc,adsoyad,maas)

# n = int(input("kaç personel gireceksiniz? : "))
# for i in range(n):
#     PersonelBilgiGir()
    
# PersonelListele()




#####################################################
# def DaireCevreHesapla(r,pi=3.14):
#     cevre = 2*pi*r
#     print(f"{r} yarıçaplı dairenin çevresi: {cevre}" )

# def DaireAlanHesapla(r,pi=3.14):
#     alan = pi*r*r
#     print(f"{r} yarıçaplı dairenin alanı: {alan}" )


# DaireCevreHesapla(5)
# DaireCevreHesapla(5,3)
# DaireCevreHesapla(5,pi=3)
# DaireAlanHesapla(5)
# DaireAlanHesapla(5,3)
# DaireAlanHesapla(5,pi=3)
# Dairenin Alan hesabını yapan metodu tanımlayınız



# SORU: parametre olarak alınan 2 sayıyı yine parametre olarak alınan işlem bilgisine göre işleme sokup
# sonucu döndüren metodu yazınız.
# Örnek: islemYap(4,5,"+") => 20,islemYap(4,5,"*") => 9

def IslemYap(sayi1,sayi2,islem):
    if(islem=='+'):
        print(sayi1+sayi2)
    elif(islem=='-'):
        print(sayi1-sayi2)
    elif(islem=='*'):
        print(sayi1*sayi2)
    elif(islem=='/'):
        print(sayi1/sayi2)
    
IslemYap(4,5,'+')
IslemYap(4,5,'-')
IslemYap(4,5,'*')
IslemYap(4,5,'/')

### Kullanıcı sayı girdiği sürece girilen sayıları toplayan programı yazınız.
## Kullanıcıya "sayı giriniz(çıkmak için Ç yazınız):"" uyarısı gelecek. Metod adı: CokluSayiGir()



toplam = 0
def CokluSayiGir():
    global toplam
    while(True):
        inp = input("Sayı giriniz (çıkmak için ç): ")
        if(inp.lower()=='ç'):
            break
        else:
            sayi = int(inp)
            toplam += sayi

CokluSayiGir()
print(toplam)






