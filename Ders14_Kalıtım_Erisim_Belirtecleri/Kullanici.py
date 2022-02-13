class Kullanici:
    def __init__(self,kid:int=0,adsoyad:str="",telefon:str="") -> None:
        self.Kid = kid
        self.AdSoyad = adsoyad
        self.Telefon = telefon

    def BilgiYaz(self):
        print(f"""\t\tKullanıcı Bilgileri
        -------------------
        Ad Soyad :\t\t{self.AdSoyad}
        Telefon  :\t\t{self.Telefon}
        -------------------
        """)