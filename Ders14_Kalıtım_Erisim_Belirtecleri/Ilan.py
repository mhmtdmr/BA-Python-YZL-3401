from datetime import datetime
from time import sleep

class Ilan:
    def __init__(self,iid:str=0,ilanTarihi:datetime=datetime.now(),baslik:str="",aciklama:str="",yayindaMi:bool=False) -> None:
        self.Iid = iid
        self.IlanTarihi = ilanTarihi
        self.Baslik = baslik
        self.Aciklama = aciklama
        self.YayindaMi = yayindaMi
    
    def Yayinla(self):
        print("Ilan yayınlanıyor...")
        sleep(1)
        self.YayindaMi = True
        print("Ilan yayınlanda !")


    def YayinDurdur(self):
        print("Ilan yayını durduruluyor...")
        sleep(1)
        self.YayindaMi = False
        print("Ilan yayını durduruldu!")

    def BilgiYaz(self):
        print(f"""\t\tİlan Bilgileri
        --------------
        Ilan Numarası :\t\t{self.Iid}
        Ilan Tarihi   :\t\t{self.IlanTarihi}
        Baslik        :\t\t{self.Baslik}
        Aciklama      :\t\t{self.Aciklama}
        --------------
        """)
