
# Aşağıdaki formatta dosyaya yazma işlemini metot olarak yazınız.
# Metot: LogDirectoryBuilder()
#########################################################
# Dosya-Klasör Yapısı :=>    LOG/YIL/AY/gunSayisi_log.txt
#                            LOG/2022/1/29_log.txt
from datetime import datetime
from email.mime import base
from os import makedirs,open,getcwd,path

def LogDirectoryBuilder() -> bool:
    basePath = "C:\\Users\\Bilge Adam\\Desktop\\BA-Python-YZL-3401\\Ders9_DosyaDizin\\"

    year = datetime.now().year
    month = datetime.now().month

    if(month<10):
        month = "0"+str(month) # ilk 9 ayın başına 0 eklenecek.

    logPath = f"LOG\\{year}\\{month}\\"
    fullPath = basePath + logPath
    # print(fullPath)
    # C:\Users\Bilge Adam\Desktop\BA-Python-YZL-3401\Ders9_DosyaDizin\LOG\2022\01\

    if(not path.exists(fullPath)):
        try:
            makedirs(fullPath)  # Klasörleri oluşturur.
            print("Klasör veya klasörler oluşturuldu")
            return True
        except Exception as hata:
            print("Klasör veya klasörler oluşturulamadı!\n",hata)
            return False
    else:
        return True











# Dosya içerisine aşağıdaki formatta yazma yapacak metodu yazınız.

# Metot: LogWriter(event:str)
#####################################################
# Zaman Damgası             Olay
# 13:28:00___29-01-2022     Kullanıcı Giriş yaptı.
# print(datetime.now().strftime("%H:%M:%S___%d-%m-%Y"))


if(__name__=="__main__"):
    LogDirectoryBuilder()