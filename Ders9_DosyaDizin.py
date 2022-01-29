from datetime import datetime
from importlib import import_module
from os import open,listdir,getcwd,mkdir,chdir,path,rmdir



#### DİZİN İŞLEMLERİ ####


def mkdir_overload(dirPath:str) -> bool:
    # bir klasör oluştur.
    if(not path.exists(dirPath)):
        try:
            mkdir(dirPath) # klasörü oluştur.
            chdir(dirPath) # klasöre giriş yap.
            print(" klasör oluşturuldu ve klasöre girildi.")
            return True
        except Exception as err:
            print("klasör oluşturulamadı. Alınan hata: ",err)
            return False
    else:
        chdir(dirPath) # klasöre giriş yap.
        print("Klasör zaten mevcut!,klasöre giriş yapıldı")
        return True

def rmdir_overload(dirPath:str) -> bool:
    # bir klasör sil
    if(not path.exists(dirPath)):
        try:
            rmdir(dirPath) 
            print(" klasör silini.")
            return True
        except Exception as err:
            print("klasör silinemedi. Alınan hata: ",err)
            return False
    else:
        chdir(dirPath)
        print("Klasör zaten mevcut değil!!")
        return True
# https://codeshare.io/BA303

# # çalışma klasörünü getir.
# currentDirectory = getcwd()
# print(currentDirectory)
# # C:\Users\Bilge Adam\Desktop\BA-Python-YZL-3401

# dirPath = "C:\\Users\\Bilge Adam\\Desktop\\BA-Python-YZL-3401\\Ders9_DosyaDizin"
# mkdir_overload(dirPath)
# print(getcwd())

# silinecekKlasor = dirPath+'\\'+'Yeni klasör'
# # C:\Users\Bilge Adam\Desktop\BA-Python-YZL-3401\Ders9_DosyaDizin\Yeni klasör
# rmdir_overload(dirPath)


# dosyaDizinListe = listdir(dirPath)
# print(dosyaDizinListe)



#### DOSYA İŞLEMLERİ ####
# os.O_RDONLY − open for reading only
# os.O_WRONLY − open for writing only
# os.O_RDWR − open for reading and writing
# os.O_NONBLOCK − do not block on open
# os.O_APPEND − append on each write
# os.O_CREAT − create file if it does not exist
# os.O_TRUNC − truncate size to 0
# os.O_EXCL − error if create and file exists
# os.O_SHLOCK − atomically obtain a shared lock
# os.O_EXLOCK − atomically obtain an exclusive lock
# os.O_DIRECT − eliminate or reduce cache effects
# os.O_FSYNC − synchronous writes
# os.O_NOFOLLOW − do not follow symlinks


# Dosya adını tam yol ile belirttik.
dirPath = "C:\\Users\\Bilge Adam\\Desktop\\BA-Python-YZL-3401\\Ders9_DosyaDizin\\"
mkdir_overload(dirPath) # klasör yoksa oluşturulsun.!

dosya = dirPath + "isimler.txt" # dosysnın tam yolunu belirttik.
print("dosyanın tam adresi:",dosya)
#C:\Users\Bilge Adam\Desktop\BA-Python-YZL-3401\Ders9_DosyaDizin\isimler.txt

import os
dosya = open(dosya, os.O_RDWR| os.O_APPEND)
isimByte = str.encode("Ahmet Demir\n") # string'i byte array e dönüştürdük.
os.write(dosya,isimByte)
os.close(dosya)

# AŞağıdaki formatta dosyaya yazma işlemini metot olarak yazınız.

# Metot: LogDirectoryBuilder()
#########################################################
# Dosya-Klasör Yapısı :=>    LOG/YIL/AY/gunSayisi_log.txt
#                            LOG/2022/1/29_log.txt

# Metotları yukarıdaki klasörler yoksa oluşturulacak şekilde tanımlayın.

# Dosya içerisine aşağıdaki formatta yazma yapacak metodu yazınız.

# Metot: LogWriter(event:str)
#####################################################
# Zaman Damgası             Olay
# 13:28:00___29-01-2022     Kullanıcı Giriş yaptı.
print(datetime.now().strftime("%H:%M:%S___%d-%m-%Y"))


















