from Ilan import Ilan
from Kullanici import Kullanici
from Daire import Daire

class DaireIlan:
    def __init__(self,daire:Daire=None,kullanici:Kullanici=None,ilan:Ilan=None) -> None:
        self.Daire = daire
        self.Ilan:Ilan = ilan
        self.Kullanici:Kullanici = kullanici
    
    def BilgiYaz(self):
        self.Kullanici.BilgiYaz()
        self.Ilan.BilgiYaz()
        self.Daire.BilgiYaz()
        

