from Konut import Konut

class Daire(Konut):
    def __init__(self, eid: int = 0, metrekare: int = 0, adres: str = "", yas: int = 0, odaSayisi: int = 0, isitma: str = "",bulunduguKat:int=0) -> None:
        super().__init__(eid, metrekare, adres, yas, odaSayisi, isitma)
        self.BulunduguKat = bulunduguKat

    def BilgiYaz(self):
        print(f"""\t\tDaire Bilgileri
        ---------
        Metrekare    :\t\t{self.MetreKare}
        Adres        :\t\t{self.Adres}
        Yaş          :\t\t{self.Yas}
        Oda Sayısı   :\t\t{self.OdaSayisi}
        Isıtma Tipi  :\t\t{self.Isitma}
        Bulunduğu Kat:\t\t{self.BulunduguKat}
        ---------
        """)
