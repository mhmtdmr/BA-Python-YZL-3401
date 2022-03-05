from pymongo import *

###########################################
##########  BAĞLANTI İŞLEMLERİ  ###########
###########################################

myclient = MongoClient() # local veritabanına parolasız bağlandık.
# myclient = MongoClient("mongodb+srv://username:[PASSWORD]@cluster0-82uxf.mongodb.net/node-app?retryWrites=true&w=majority")

# print(myclient.list_database_names()) # Veritabanı isimlerini listele.
mydb = myclient["FirstDB"]
mycollection = mydb["firstCollection"]
# print(mydb.list_collection_names()) # seçili veritabanındaki koleksiyonları listele.


###########################################
##########   OKUMA İŞLEMLERİ    ###########
###########################################

# # Koleksiyondaki 1 kayıtı getirmek için
# singleData = mycollection.find_one({"name":"Salih"})
# print(singleData)


# # Koleksiyondaki tüm kayıtları dict tipinde döndür.
# mydatas = mycollection.find()
# mydatas = mycollection.find({},{'name':1}) # name parametresi gösterilsin.
# mydatas = mycollection.find({},{'name':0}) # name parametresi gösterilmesin.

# mydatas = mycollection.find({'name':'Ece'},{'_id':0,'name':0}) # isimi Ece olan kayıtı getir. _id ve name parametresi gösterilmesin.
# mydatas = mycollection.find()
# for data in mydatas:
#     print(data)


# # Filtre uygulama.
# filter = {"age":{"$gt":17}}
# columns = {"_id":0,"name":1} # _id ve diğer alanları gösterme. name alanını göster

# mydatas = mycollection.find(filter,columns)
# for data in mydatas:
#     print(data)



###########################################
##########   EKLEME İŞLEMLERİ   ###########
###########################################

# newFile = {"name":"Şenal","surname":"Güneş","age":57}

# insertedFile = mycollection.insert_one(newFile) # Veritabanına yeni bir dosya ekledik.

# print(insertedFile.inserted_id,type(insertedFile.inserted_id)) # Yeni eklenen dosyanın _id bilgisine ulaştık.

# newObjets = [{"name":"Ali","surname":"KIRMIZILI","age":22},{"name":"Selda","surname":"BEYAZLI"},{"name":"Samuel","surname":"Eto","age":42}]
# # insertedObjects = mycollection.insert_many(newObjets)
# # print(insertedObjects.inserted_ids) # yeni eklenen id leri göster.
# mycollection.insert_many(newObjets)


# id kolonunu el ile ayarlama

# newFile = {"_id":1,"name":"Ayşe","surname":"Aslan"}
# mycollection.insert_one(newFile)

# from bson.objectid import ObjectId
# newFile = {"_id":ObjectId("0123456789ABCDEF00112233"),"name":"Ahmet","surname":"Aslan"}
# mycollection.insert_one(newFile)


###############################################
##########   GÜNCELLEME İŞLEMLERİ   ###########
###############################################

# from bson.objectid import ObjectId
# idFilter = {"_id":ObjectId('6223172a574a1c3f51d0d3c7')}
# updateQuery = {"$set":{"age":47}}
# mycollection.update_one(idFilter,updateQuery)


# tüm dosyalara language anahtar değerini ekle.
# filter = {}
# updateQuery = {"$set":{"language":"Turkish"}}
# mycollection.update_many(filter,updateQuery)

# # tüm dosyalardan language anahtar değerini sil.
# updateQuery = {"$unset":{"language":1}}
# mycollection.update_many({},updateQuery)



###############################################
##########      SİLME İŞLEMLERİ     ###########
###############################################

# from bson.objectid import ObjectId
# # deleteFilter = {"_id":ObjectId("62231811bc70989560a7c408")}
# # mycollection.delete_one(deleteFilter)

# deleteFilter = {"name":"Samuel","surname":"Eto"}
# mycollection.delete_many(deleteFilter)



# https://codeshare.io/BA203