import sqlite3 
# veritabanı işlemleri için kullanacağımız kütüphane

class DbTools:
    """This is a base class for database works. It provides connection and disconnection to database: firstdb."""
    db = object()

    def __init__(self) -> None:
        pass


    @staticmethod
    def ConnectDB():
        """This method provides database connection to firstdb."""
        try:
            global db
            db = sqlite3.connect("C:\\Users\\Bilge Adam\\Desktop\\BA-Python-YZL-3401\\Ders16\\firstdb.db")
            print("Connection successfull!")
        except Exception as error:
            print("Could not connect to database!")
            print(error)
    
    @staticmethod
    def DisconnectDB():
        """This method disconnects firstdb."""
        try:
            db.close()
            print("Disconnection successfull!")
        except Exception as error:
            print("Could not disconnect database!")
            print(error)

if __name__=="__main__":
    DbTools.ConnectDB()
    DbTools.DisconnectDB()

