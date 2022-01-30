
# Aşağıdaki formatta dosyaya yazma işlemini metot olarak yazınız.
# Metot: LogDirectoryBuilder()
#########################################################
# Dosya-Klasör Yapısı :=>    LOG/YIL/AY/gunSayisi_log.txt
#                            LOG/2022/1/29_log.txt

from datetime import datetime
from os import makedirs,open,getcwd,path,O_RDWR,O_APPEND,write

def LogDirectoryBuilder() -> str:
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
            return fullPath
        except Exception as hata:
            print("Klasör veya klasörler oluşturulamadı!\n",hata)
            return fullPath
    else:
        return fullPath

# Dosya içerisine aşağıdaki formatta yazma yapacak metodu yazınız.

# Metot: LogWriter(event:str)
#####################################################
# Zaman Damgası             Olay
# 13:28:00___29-01-2022     Kullanıcı Giriş yaptı.
# print(datetime.now().strftime("%H:%M:%S___%d-%m-%Y"))

from os import *

def LogWriter(event:str):
    basePath = LogDirectoryBuilder()
    if(path.exists(basePath)):
        fileName = str(datetime.now().day) +"__log.txt" # dosya adını oluşturduk.

        filePath = basePath + fileName #dosyanın tam adresini oluşturduk.


        if(not path.exists(filePath)):
            file = open(filePath,O_RDWR| O_APPEND | O_CREAT) # dosyayı açtık.
            baslik = "zaman\t\t\t\tolay\n"+"-----\t\t\t\t----\n"
            baslik = str.encode(baslik)
            write(file,baslik) # kayıtı dosyaya yazdık.
            close(file) # dosyayı kapattık.


        zaman = datetime.now().strftime("%H:%M:%S___%d-%m-%Y")
        kayit = zaman + "\t\t" + event +"\n" # dosyaya yazılacak kayıt bilgisini oluşturduk
        file = open(filePath,O_RDWR| O_APPEND | O_CREAT) # dosyayı açtık.
        kayit = str.encode(kayit) # dosyaya eklenecek str yi byte array'e çevirdik.
        write(file,kayit) # kayıtı dosyaya yazdık.
        close(file) # dosyayı kapattık.

# https://codeshare.io/BA204

if(__name__=="__main__"):
    # LogDirectoryBuilder()
    # LogWriter("Test")
    # LogWriter("Dosya yazma metotları tanımlandı.")
    LogWriter("Bu dosyayı kapatıyorum.")