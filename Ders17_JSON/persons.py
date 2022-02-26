from base64 import encode
import json
if __name__=="__main__":

    # filePath = "C:\\Users\\Bilge Adam\\Desktop\\BA-Python-YZL-3401\\Ders17_JSON\\persons.json"

    # personsFile = open(filePath,"r",encoding="utf-8") # => file
    # personsDict = json.load(personsFile) # => dict

    # print(personsDict.keys())
    # print()
    # print(personsDict.values())

    # print("Personel 1 Ad: ",personsDict["1"]["Name"])
    # print("Personel 2 Ad: ",personsDict["2"]["Name"])
    # print("Personel 3 Ad: ",personsDict["3"]["Name"])

    # print("Personel 1 Surname: ",personsDict["1"]["Surname"])
    # print("Personel 2 Surname: ",personsDict["2"]["Surname"])
    # print("Personel 3 Surname: ",personsDict["3"]["Surname"])

    ### Dosyaya yazma
    # newPerson  = {"4":{"Name":"Gerrard","Surname":"Steven"}}
    # filePath = "C:\\Users\\Bilge Adam\\Desktop\\BA-Python-YZL-3401\\Ders17_JSON\\persons.json"

    # personsFile = open(filePath,"w",encoding="utf-8") # => file # a:append,w:write(eskiyi sil yeniyi yaz)
    # json.dump(newPerson,personsFile,ensure_ascii=False)

    ### Insert
    # filePath = "C:\\Users\\Bilge Adam\\Desktop\\BA-Python-YZL-3401\\Ders17_JSON\\persons.json"
    # newPerson  = {"4":{"Name":"Gerrard","Surname":"Steven"}}
    # personsFile = open(filePath,"r",encoding="utf-8")
    # personsDict = json.load(personsFile)
    # personsDict.update(newPerson)
    # with open(filePath,"w") as file:
    #     json.dump(personsDict,file,indent=1)
    
    ### Update
    # filePath = "C:\\Users\\Bilge Adam\\Desktop\\BA-Python-YZL-3401\\Ders17_JSON\\persons.json"
    # personsFile = open(filePath,"r",encoding="utf-8")
    # personsDict = json.load(personsFile)
    # personsDict["1"]["Name"] = "Kıran"
    # with open(filePath,"w",encoding="utf-8") as file:
    #     json.dump(personsDict,file,indent=1,ensure_ascii=False)

    ### Delete
    filePath = "C:\\Users\\Bilge Adam\\Desktop\\BA-Python-YZL-3401\\Ders17_JSON\\persons.json"
    personsFile = open(filePath,"r",encoding="utf-8")
    personsDict = json.load(personsFile)
    del personsDict["2"]
    with open(filePath,"w",encoding="utf-8") as file:
        json.dump(personsDict,file,indent=1,ensure_ascii=False)






# MongoDB Database Tools
# MongoDB Compass
# MongoDB Community Server







