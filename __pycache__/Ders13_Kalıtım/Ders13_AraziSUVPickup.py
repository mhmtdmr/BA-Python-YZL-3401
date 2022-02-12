from Ders13_Arac import Arac
from datetime import datetime

class AraziAraci(Arac):
    """
    Bu sınıf Arac sınıfından miras alınarak tanımlanmıştır!
    !! Child Class !!
    ! Eklenti: Better Comments !
    """
    def __init__(self, aid: int = 0, marka: str = "", seri: str = "", model: str = "", motorHacmi: int = 1000, renk: str = "Kırmızı", modelYili=datetime.now().year,cekis="4x4",halatVarMi=False) -> None:
        super().__init__(aid, marka, seri, model, motorHacmi, renk, modelYili)
        self.Cekis =cekis
        self.HalatVarMi = halatVarMi

    def BilgiYaz(self):
        halat = "Yok"
        if (self.HalatVarMi):
            halat = "Var"

        print(f"""       ARAÇ BİLGİLERİ
        Marka:\t\t{self.Marka}
        Seri:\t\t{self.Seri}
        Model:\t\t{self.Model}
        Motor Hacmi:\t{self.MotorHacmi}
        Renk:\t\t{self.Renk}
        Model Yili:\t{self.ModelYili}
        Çekiş:\t\t{self.Cekis}
        Halat:\t\t{halat}
        Vergi:\t\t{self.VergiHesapla()} ₺
        """)

    def BilgiDondur(self):
        halat = "Yok"
        if (self.HalatVarMi):
            halat = "Var"

        bilgi = f"""       ARAÇ BİLGİLERİ
        Marka:\t\t{self.Marka}
        Seri:\t\t{self.Seri}
        Model:\t\t{self.Model}
        Motor Hacmi:\t{self.MotorHacmi}
        Renk:\t\t{self.Renk}
        Model Yili:\t{self.ModelYili}
        Çekiş:\t\t{self.Cekis}
        Halat:\t\t{halat}
        Vergi:\t\t{self.VergiHesapla()} ₺
        """
        return bilgi