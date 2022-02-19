# BelediyeVergi anasınıf
# Her alt sınıfta bulunması gerekli olan özellikler: TicariVergiOrani, BireyselVergiOrani
# Her alt sınıfta bulunması gerekli olan metotlar: FaturaHesapla(tip:(ticari mi bireysel mi),tutar)
# MarsBelediyesi alt sınıf: TicariVergiOrani = %5, BireyselVergiOrani= %1
# PlutonBelediyesi alt sınıf: TicariVergiOrani = %3, BireyselVergiOrani= %2
# PlutonBelediyesi'nde vergisiz fiyata ekstra azot kullanım bedeli yansıtılmaktadır. %5

from abc import *
class BelediyeVergi(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractproperty
    def TicariVergiOrani(self):
        pass

    @abstractproperty
    def BireyselVergiOrani(self):
        pass

    @abstractclassmethod
    def FaturaHesapla(cls,tutar,tip):
        pass

    @classmethod
    def FaturaHesapla2(cls,tutar,tip):
        if(tip=="ticari"):
            vergiliTutar = tutar + (tutar * cls.TicariVergiOrani)
        elif(tip=="bireysel"):
            vergiliTutar = tutar + (tutar * cls.BireyselVergiOrani)
        return vergiliTutar

class MarsBelediyesi(BelediyeVergi):
    def __init__(self) -> None:
        super().__init__()
    
    TicariVergiOrani = 0.05
    BireyselVergiOrani = 0.01

    @classmethod
    def FaturaHesapla(cls,tutar,tip):
        if(tip=="ticari"):
            vergiliTutar = tutar + (tutar * cls.TicariVergiOrani)
        elif(tip=="bireysel"):
            vergiliTutar = tutar + (tutar * cls.BireyselVergiOrani)
        return vergiliTutar

class PlutonBelediyesi(BelediyeVergi):
    def __init__(self) -> None:
        super().__init__()
    
    TicariVergiOrani = 0.03
    BireyselVergiOrani = 0.02
    AzotVergiOrani = 0.05

    @classmethod
    def FaturaHesapla(cls,tutar,tip):
        if(tip=="ticari"):
            vergiliTutar = tutar + (tutar * cls.TicariVergiOrani) + (tutar * cls.AzotVergiOrani)
        elif(tip=="bireysel"):
            vergiliTutar = tutar + (tutar * cls.BireyselVergiOrani) + (tutar * cls.AzotVergiOrani)
        return vergiliTutar

if __name__=="__main__":
    marsli = MarsBelediyesi()
    vergiliTutarM = marsli.FaturaHesapla(100,'bireysel')
    print("Marsta  100 lira fatura nın vergili hali:",vergiliTutarM)

    plutonlu  = PlutonBelediyesi()
    vergiliTutarP = plutonlu.FaturaHesapla(100,'bireysel')
    print("Plutonda  100 lira fatura nın vergili hali:",vergiliTutarP)

