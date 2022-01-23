# Bu dosya matematik fonksiyonlarını içeren bir modüldür.
def Topla(sayi1,sayi2):
    toplam = sayi1 + sayi2
    # print(f"{sayi1} + {sayi2} = {toplam}")
    return toplam

def Islem(sayi1,sayi2):
    toplam = sayi1 + sayi2
    fark = sayi1-sayi2
    carpim = sayi1*sayi2
    try:
        bolum = sayi1//sayi2
    except ZeroDivisionError:
        bolum = sayi1 # Bolen 0 olamacağı için 1 olarak değiştirdik.
    return toplam,fark,carpim,bolum
    # python sıralı atamaya müsade ettiği gibi/için sıralı değer döndürmeye de imkân sağlar.

def SayiAl():
    sayi = int(input("sayı:"))
    return sayi

def Kare(sayi):
    return sayi*sayi

def Kuvvet(taban,us):
    return taban**us

# print(__name__) # bu dosyadan çalıştığında: __main__
                # import edilmiş başka dosyadan çalıştığında: Ders8_Matematik

if(__name__=='__main__'):         
    kontrol = SayiAl()
    print("Dosya buradan çalıştırıldı.")

    # Kare isminde bir metod tanımlayın. kendisine gönderilen sayının karesini döndürsün.

    # Kuvvet isminde bit metod tanımlayın. Kendisine gödnerilen 2 sayıya göre kuvvet alsın.Örn: Kuvvet(2,3) => 8
