from datetime import datetime


class Arac:
    """
    Bu sınıf kendisinden miras alacak olan alt sınıflar için bir temel oluşturmaktadır.
    !! Base Class !!
    """
    def __init__(self,aid:int=0,marka:str="",seri:str="",model:str="",motorHacmi:int=1000,renk:str="Kırmızı",modelYili=datetime.now().year) -> None:
        self.ID = aid
        self.Marka = marka
        self.Seri = seri
        self.Model = model
        self.MotorHacmi = motorHacmi
        self.Renk = renk
        self.ModelYili = modelYili

    # def __init__(self) -> None:
    #     self.ID = 0
    #     self.Marka = ""
    #     self.Seri = ""
    #     self.Model = ""
    #     self.MotorHacmi = 1000
    #     self.Renk = ""
    #     self.ModelYili = 0

    def VergiHesapla(self)-> float:
        """
        Formül: motorhacmi - (100 * araç yaşı)
        Vergi 250 ₺ altına düşemez!
        """
        vergi = self.MotorHacmi -(100*self.GetYas())
        if(vergi<250):
            vergi = 250
        return vergi

    def GetYas(self)->int:
        # yaşı hesapla dönder.
        yas = datetime.now().year - self.ModelYili
        return yas
