# python -m pip install abcplus

from abc import ABC,abstractmethod,abstractproperty,abstractclassmethod,abstractstaticmethod

class Banka(ABC): #ABC: Abstract Based Class
    @abstractproperty   # sınıf özelliğinin alt sınıflarda tanımlanmasını zorunlu yaptık.
    def EftUcreti(self):
        pass
    def __init__(self,bakiye:float=0.0) -> None:
        super().__init__()
        self.Bakiye = bakiye

    @abstractmethod  # Bu metot alt sınıflarda tanımlanmak zorunda olan bir instance metodudur.
    def EFT(self,hedefHesap,miktar):
        pass

    def BakiyeYaz(self):
        print("Mevcut bakiye:",self.Bakiye)

class Ziraat(Banka):
    EftUcreti = 0.0
    def __init__(self, bakiye: float = 0) -> None:
        super().__init__(bakiye)
    def EFT(self,hedefHesap,miktar):
        pass

class Garanti(Banka):
    EftUcreti = 3.0
    def __init__(self, bakiye: float = 0) -> None:
        super().__init__(bakiye)

    def EFT(self,hedefHesap:Banka,miktar:float):
        if(self.Bakiye-(Garanti.EftUcreti+miktar)>=0): # Bakiye yeterli mi?
            self.Bakiye = self.Bakiye-(Garanti.EftUcreti+miktar)
            hedefHesap.Bakiye += miktar
            print(f"Hesabınızdan {miktar} ₺ para, {Garanti.EftUcreti} karşılığında gönderilmiştir.")
            self.BakiyeYaz()
        else:
            print("Bakiyeniz bu işlem için yeterli değildir!")

class Akbank(Banka):
    EftUcreti = 5.0
    def __init__(self, bakiye: float = 0) -> None:
        super().__init__(bakiye)
    
    def EFT(self,hedefHesap:Banka,miktar:float):
        if(self.Bakiye-(Akbank.EftUcreti+miktar)>=0): # Bakiye yeterli mi?
            self.Bakiye = self.Bakiye-(Akbank.EftUcreti+miktar)
            hedefHesap.Bakiye += miktar
            print(f"Hesabınızdan {miktar} ₺ para, {Akbank.EftUcreti} karşılığında gönderilmiştir.")
            self.BakiyeYaz()
        else:
            print("Bakiyeniz bu işlem için yeterli değildir!")
    

def EFT(kaynakHesap,hedefhesap,miktar):
    kaynakHesap.EFT(hedefhesap,miktar)


if __name__ =="__main__":
    # garantiHesabim = Garanti(bakiye=1000)
    # # garantiHesabim.EFT()

    # akbankHesabim = Akbank(bakiye=6000)
    # akbankHesabim.EFT()
    # EFT(garantiHesabim)
    # EFT(akbankHesabim)



    # garantiHesabim2 = Garanti(1000)
    # akbankHesabim2 = Akbank(9000)
    
    # # garantiden akbank a eft
    # EFT(garantiHesabim2,akbankHesabim2,5000)
    # # Bakiyeniz bu işlem için yeterli değildir!
    
    # # akbank tan garantiye para transferi
    # EFT(akbankHesabim2,garantiHesabim2,5000)
    
    # print("garantiHesabim2 bakiye:",end="")
    # garantiHesabim2.BakiyeYaz()

    ziraat = Ziraat()




