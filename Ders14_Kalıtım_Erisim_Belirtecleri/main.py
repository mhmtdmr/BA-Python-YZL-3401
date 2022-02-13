from datetime import datetime
from Daire import Daire
from Ilan import Ilan
from Kullanici import Kullanici
from DaireIlan import DaireIlan

if __name__=="__main__":
    kullanicim = Kullanici(1,"Mahmut Emlaksever","02120001100")
    ilanim = Ilan(1,datetime.now(),"Satılık Ev","Harika manzaralı bir ev.",False)
    dairem = Daire(1,125,"Beyoğlu",25,"2+1","Kombi",2)


    daireIlan = DaireIlan(daire=dairem,ilan=ilanim,kullanici=kullanicim)
    daireIlan.Ilan.Yayinla() # Ilanı yayınla dedikten sonra gösterecek.
    if(daireIlan.Ilan.YayindaMi==True):
        daireIlan.BilgiYaz()

