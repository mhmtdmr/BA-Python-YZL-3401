from datetime import datetime


class Ilan:
    """
    Bu sınıf ilan bilgilerini ve işlemlerini bünyesinde barındıran bir üst sınıftır.
    !! Base Class !!
    """
    def __init__(self,baslik:str="",aciklama:str="",tarih:datetime=datetime.now()) -> None:
        self.Baslik = baslik
        self.Aciklama = aciklama
        self.Tarih = tarih

    def BilgiYaz(self):
        print(f"""\t\tIlan Bilgileri
        Başlık: \t\t{self.Baslik}
        Açıklama: \t\t{self.Aciklama}
        İlan Tarihi:\t {self.Tarih} 
        """)

        