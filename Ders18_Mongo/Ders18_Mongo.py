from pymongo import *
myclient = MongoClient() # local veritabanına parolasız bağlandık.

# myclient = MongoClient("mongodb+srv://username:[PASSWORD]@cluster0-82uxf.mongodb.net/node-app?retryWrites=true&w=majority")

# print(myclient.list_database_names()) # Veritabanı isimlerini listele.
mydb = myclient["FirstDB"]
mycollection = mydb["firstCollection"]
# print(mydb.list_collection_names()) # seçili veritabanındaki koleksiyonları listele.


# Koleksiyondaki tüm kayıtları dict tipinde döndür.

# mydatas = mycollection.find()
# for data in mydatas:
#     print(data)

# Koleksiyondaki 1 kayıtı getirmek için
singleData = mycollection.find_one({"name":"Salih"})
print(singleData)

# https://codeshare.io/BA203
