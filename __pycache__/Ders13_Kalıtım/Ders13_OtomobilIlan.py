from Ders13_Otomobil import Otomobil
from Ders13_Ilan import Ilan

class OtomobilIlan():
    """
    Bu sınıf Otomobil ilanı vermekte kullanacağımız alt sınıftır.
    """
    def __init__(self,oto:Otomobil=None,ilan:Ilan=None) -> None:
        self.Otomobil = oto
        self.Ilan = ilan

    def Yaz(self):
        self.Ilan.BilgiYaz()
        self.Otomobil.BilgiYaz()