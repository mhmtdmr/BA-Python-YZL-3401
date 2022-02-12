from Ders13_Arac import Arac
from Ders13_Otomobil import Otomobil
from Ders13_AraziSUVPickup import AraziAraci
from Ders13_Ilan import Ilan
from Ders13_OtomobilIlan import OtomobilIlan
from datetime import datetime



if __name__ == "__main__":

    # # Üst sınıftaki özellik ve metotları tekrar tanımlamadan kullanabildik.
    # oto1 = Otomobil()
    # oto1.ID = 1
    # oto1.Renk = "Siyah"
    # oto1.Marka ="Mazda"
    # oto1.Seri = "MX5"
    # oto1.Model = "2.0 Benzin"
    # oto1.MotorHacmi = 1999
    # oto1.ModelYili = 2020

    # oto1.KapiSayisi = 3
    # oto1.KasaTipi = "Coupe"

    # oto1Vergi = oto1.VergiHesapla()
    # print(f"oto1'e ait vergi tutarı: {oto1Vergi}")

# https://codeshare.io/BA203

    # arac2 = Arac(aid=2,marka="Mercedes",seri="C",model="C200",motorHacmi=2000,renk="Beyaz",modelYili=2015)
    # oto2 = Otomobil(aid=2,marka="Mercedes",seri="C",model="C200",motorHacmi=2000,renk="Beyaz",modelYili=2015,kapiSayisi=5,kasaTipi="Sedan")
    
    # print(oto2.Marka)
    # print(oto2.Seri)
    # print(oto2.Model)
    # print(oto2.KapiSayisi)





    # defender = AraziAraci(aid=5,marka="Land Rover",seri="Defender",model="3.0 Dizel",modelYili=1990,motorHacmi=3000,renk="Gri-Siyah",cekis="4x4",halatVarMi=True)
    # defender.BilgiYaz()
    # print(defender.BilgiDondur())




    oto2 = Otomobil(aid=2,marka="Mercedes",seri="C",model="C200",motorHacmi=2000,renk="Beyaz",modelYili=2015,kapiSayisi=5,kasaTipi="Sedan")
    ilan1 = Ilan("Tertemiz Araba","5 kazası var.")

    oto2ilan = OtomobilIlan(oto=oto2,ilan=ilan1)

    oto2ilan.Yaz()
