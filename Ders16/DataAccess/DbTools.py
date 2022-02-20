import sqlite3 
# veritabanı işlemleri için kullanacağımız kütüphane
# Farklı sınıflar için veritabanı işlemi yapacak olsak da bu dosyayı kullanacağız.

class DbTools:
    """This is a base class for database works. It provides connection and disconnection to database: firstdb."""
    db = None       # bu nesne nin amacı bağlantıya bu seviyeden ulaşmak burada tanımladık. global !.
    __dbName = "C:\\Users\\Bilge Adam\\Desktop\\BA-Python-YZL-3401\\Ders16\\firstdb.db"

    def __init__(self) -> None:
        pass


    @staticmethod
    def ConnectDB():
        """This method provides database connection to firstdb."""

        global db
        try:
            db = sqlite3.connect(DbTools.__dbName)      # veritabanı bağlantısını aç!
            print("Connection successfull!")
        except Exception as error:
            print("Could not connect to database!")
            print(error)
        return db
    
    @staticmethod
    def DisconnectDB():
        """This method disconnects firstdb."""

        global db
        try:
            db.close()     # veritabanı bağlantısını kapat!
            print("Disconnection successfull!")
        except Exception as error:
            print("Could not disconnect database!")
            print(error)

if __name__=="__main__":
    DbTools.ConnectDB()
    DbTools.DisconnectDB()

