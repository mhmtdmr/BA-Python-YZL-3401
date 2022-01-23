from sys import int_info


def ListeOrtalama(sayiListesi):
    ortalama = sum(sayiListesi)//len(sayiListesi)
    return ortalama

# değişken sayıda parametre gelecekse parametre isminin başına * konulur.
# bu yöntem kullanıldığında değişken tipi tuple'a döner. Gönderilen parametreler
# kaç tane olursa olsun bu listeye eklenir.
# Eğer bu parametre ile birlikte başka parametreler de kullanılacaksa *'lı 
# parametre en sağa yazılmalıdır.

def SayilarOrtalama(*sayiListesi):
    ortalama = sum(sayiListesi)//len(sayiListesi)
    return ortalama

def SayilarIslem(islem,*sayilar):
    if(islem=='+'):
        return sum(sayilar)
    elif(islem=='*'):
        carpim = 1
        for sayi in sayilar:
            carpim *= sayi
        return carpim
    elif(islem=='-'):
        sayilar = list(sayilar)
        fark = sayilar.pop(0)
        for sayi in sayilar:
            fark -= sayi
        return fark
    elif(islem=='/'):
        sayilar = list(sayilar)
        bolunen = sayilar.pop(0)
        for sayi in sayilar:
            bolunen //= sayi
        return bolunen

# dönüş tipi ve parametre tipi belirttik.
def TOPLA(s1:int,s2:int) -> int:
    return s1+s2


# def Topla(s1,s2):
#     return s1+s2

def Topla(*sayilar):
    return sum(sayilar)

# lambda expressions: tek satırda metod tanımlama.

kare = lambda s1,s2 : s1**s2
# yukarıda aşağıdaki metodu kısa olarak tanımladık.
# def kare(s1,s2):
#     return s1**s2



# Recursive(Özyinelemeli) Metotlar
## girilen sayıdan 0'a kadar olan sayıları döndüren metot.
def EksilterekDon(sayi):
    if(sayi>1):
        return str(sayi) + "  " + str(EksilterekDon(sayi-1))
    else:
        return 1
        
# Kendisine gönderilen sayıonın Faktöriyelini hesaplayan metodu yazınız
def Faktoriyel(sayi):
    if(sayi==0):
        return 1
    else:
        return sayi * Faktoriyel(sayi-1)




# Aşağıdaki kodlar sadece dosya buradan çalıştırıldığında çalışsın.
if(__name__=='__main__'):
    # sayiListesi = [10,20,30]
    # print(ListeOrtalama(sayiListesi))

    # print(Topla(3))
    # print(Topla(3,4))
    # print(Topla(3,4,5))
    # print(Topla(3,4,5,6))
    # print(Topla(3,4,5,6,7))

    # print(SayilarOrtalama(12,24,36))
    # print(SayilarOrtalama(12,24,36,48))
    # print(SayilarOrtalama(12,24,36,48,56))

    # print(SayilarIslem('+',100,10,10))
    # print(SayilarIslem('-',100,10,10))
    # print(SayilarIslem('/',100,10,10))
    # print(SayilarIslem('*',100,10,10))

    # print(TOPLA(4,5))
    # print(kare(44,2))

    # print(EksilterekDon(5))
    # sayi = int(input("sayı:"))
    # print(Faktoriyel(sayi))

    # print(Faktoriyel(5))

