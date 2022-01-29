# import datetime
# simdi = datetime.datetime.now()

from calendar import month
from datetime import date, datetime
from importlib import import_module
from xmlrpc.client import DateTime

# def now():
#     return datetime.now()

# # ŞİMDİKİ ZAMANI ALMA
# simdi = datetime.now()
# print(simdi)
# print("year:",simdi.year)
# print("month:",simdi.month)
# print("day:",simdi.day)
# print("hour:",simdi.hour)
# print("minute:",simdi.minute)
# print("second:",simdi.second)

# # FARKLI BİR TARİHİ MANUEL OLARAK TANIMLAMA
# birthDate = datetime(year=1990,month=10,day=25,hour=13,minute=25,second=0)
# print(birthDate)



# ZAMAN BİLGİSİNİ FORMATLAMAK
"""
%d : rakam ile gün bilgisi
%m : ay iki haneli rakam
%b: Üç haneli ay,yazı ile.
%y: 2 haneli rakam ile yıl
%Y: 4 haneli rakam ile yıl
%H: saat
%M: dakika
%S: saniye
%a: 3 haneli gün.yazı ile.
%A: Günün tam adı. yazı ile.
%D: Ay/Gun/Yil
"""


# now = datetime.now()
# formattedNow = now.strftime('%d:%m:%Y %H:%M:%S')
# print(formattedNow) # 29:01:2022 10:43:26

# formattedNow = now.strftime('%d:%m:%Y,%a %H:%M:%S')
# print(formattedNow) #29:01:2022,Sat 10:45:21

# formattedNow = now.strftime('%d:%m:%Y,%A %H:%M:%S')
# print(formattedNow) #29:01:2022,Saturday 10:45:21

# # Türkçe Gün ay bilgisi için.
# import locale
# # locale.setlocale(locale.LC_ALL,'Turkish_Turkey.1254')
# locale.setlocale(locale.LC_ALL,'tr_TR')


# formattedNow = now.strftime('%d:%m:%Y,%A %H:%M:%S')
# print(formattedNow) #29:01:2022,Saturday 10:45:21


# from datetime import datetime,timedelta

# difference = datetime.now() - datetime(1988,5,5,19,3,0)
# print(difference)

# years = difference.days//365
# days = difference.days  - (years*365)
# print(years)
# print(days)

# from datetime import timedelta

# lastWeek = datetime.now()-timedelta(7)
# print("1 hafta önceki tarih:",lastWeek)
# print(f"1 hafta önceki tarih: {lastWeek}")
# print("1 hafta önceki tarih: {0}".format(lastWeek))


from math import floor,ceil,cos,tan,pi,sqrt,pow

kare = pow(5,2) # 5**2
print("kare:",kare)

kok = sqrt(25)
print("kok:",kok)

ondalikli = 199.4
tamSayi = ceil(ondalikli) # 200
print(f"ondalıklı: {ondalikli}, tam sayı: {tamSayi}")


ondalikli = 199.7
tamSayi = floor(ondalikli) # 199
print(f"ondalıklı: {ondalikli}, tam sayı: {tamSayi}")
