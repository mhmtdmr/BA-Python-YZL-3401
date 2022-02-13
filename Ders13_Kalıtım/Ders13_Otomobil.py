from Ders13_Arac import Arac
from datetime import datetime

class Otomobil(Arac):
    """
        Arac sınıfından miras alan bu sınıf Otomobil nesnelerinde kullanılmak üzere yazılmıştır.
        !! Child Class !!
    """
    # def __init__(self,kapiSayisi=5,kasaTipi="Sedan") -> None:
    #     super().__init__() # Otomobil nesnesi tanımlandığında Arac sınıfının özellikleri için de bellekte yer açılır(init).
    #     self.KapiSayisi = kapiSayisi
    #     self.KasaTipi = kasaTipi



    # Yapıcı metotları kaltıtımı.

    # Otomobil sınıfı yapıcı metodundan Arac sınıfının yapıcı metoduna parametre göndermek.
    def __init__(self, aid: int = 0, marka: str = "", seri: str = "", model: str = "", motorHacmi: int = 1000, renk: str = "Kırmızı", modelYili=datetime.now().year,kapiSayisi:int=5,kasaTipi:str="Sedan") -> None:

        # üst sınıftaki __init__ metoduna aldığımız parametrelerin üst sınıfa ait olanlarını gönderdik.
        super().__init__(aid, marka, seri, model, motorHacmi, renk, modelYili)

        self.KapiSayisi = kapiSayisi
        self.KasaTipi = kasaTipi

    
    def BilgiYaz(self):
        print(f"""       ARAÇ BİLGİLERİ
        Marka:\t\t{self.Marka}
        Seri:\t\t{self.Seri}
        Model:\t\t{self.Model}
        Motor Hacmi:\t{self.MotorHacmi}
        Renk:\t\t{self.Renk}
        Model Yili:\t{self.ModelYili}
        Kapı Sayısı:\t{self.KapiSayisi}
        Kasa Tipi:\t{self.KasaTipi}
        Vergi:\t\t{self.VergiHesapla()} ₺
        """)






