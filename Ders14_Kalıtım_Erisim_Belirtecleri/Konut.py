from Emlak import Emlak

class Konut(Emlak):
    def __init__(self, eid: int = 0, metrekare: int = 0, adres: str = "",yas:int=0,odaSayisi:int=0,isitma:str="") -> None:
        super().__init__(eid, metrekare, adres)
        self.Yas = yas
        self.OdaSayisi = odaSayisi
        self.Isitma = isitma
        
