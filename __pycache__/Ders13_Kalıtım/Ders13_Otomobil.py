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






