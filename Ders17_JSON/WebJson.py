from datetime import datetime
import json
from urllib.request import urlopen

def GetJsonFromWeb(url:str) -> dict:
    webResponse = urlopen(url)  # web sunucuya istek gönderdiğimiz metot
    source = webResponse.read() # gelen değeri okuduk.
    data = json.loads(source) # okuduğumuz JSON formatlı dosyayı dict'e çevirdik.
    return data


def GetMyIp():
    ipurl = "http://ip.jsontest.com/"
    responseDict =  GetJsonFromWeb(ipurl)
    ip = responseDict["ip"]
    return ip

def GetDateTime():
    """This method returns current date and time with order date,time"""
    datetimeurl = "http://date.jsontest.com/"
    responseDict =  GetJsonFromWeb(datetimeurl)
    date = responseDict["date"]
    time = responseDict["time"]
    return date,time

def GetMd5Hashed(text:str):
    url = f"http://md5.jsontest.com/?text={text}"
    responseDict = GetJsonFromWeb(url)
    hashedText = responseDict["md5"]
    return hashedText

if __name__=="__main__":
    print("IP adresimiz: ",GetMyIp())
    # # IP adresimiz:  90.158.106.221

    date,time = GetDateTime()
    print("Current date:",date)
    print("Current time:",time)
    # # Current date: 02-26-2022
    # # Current time: 10:26:14 AM

    print("MD5 Şifreli 'BilgeAdam' => ",GetMd5Hashed("BilgeAdam"))
