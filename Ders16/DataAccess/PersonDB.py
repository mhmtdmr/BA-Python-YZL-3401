import os,sys
p = os.path.abspath(".")
sys.path.insert(1,p)

from Entity.Person import Person
from DataAccess.DbTools import DbTools
from Base.CRUD import CRUD


class PersonDB(CRUD):
    """
    Bu sınıf kendisine parametre olarak gelen Person 
    nesnesinin veritabanı işlemlerini yapar.
    """   
    @staticmethod
    def Create(obj:Person):
        try:
            query = f"INSERT INTO Person (Name,Surname,Age) VALUES(?,?,?);"
            db = DbTools.ConnectDB()
            cursor = db.cursor()        # SQL İmleci
            cursor.execute(query,(obj.Name,obj.Surname,obj.Age)) # İmlece yazdığımız kodu çalıştırdık.
            db.commit()   # Yapılan değişiklikleri kaydet
            print("Insert Done.")
            DbTools.DisconnectDB()
        except Exception as error:
            print("Could not insert person to database!")
            print(error)


    @staticmethod
    def Read():
        persons = list()
        personsstr = list()
        try:
            query = "SELECT * FROM Person;"
            db = DbTools.ConnectDB()
            cursor = db.cursor()
            cursor.execute(query)
            personsstr = cursor.fetchall() # sorgudan dönen tüm kayıtları liste olarak döndür.
            DbTools.DisconnectDB()
        except Exception as error:
            print("Could not read from database!")
            print(error)

        # listeyi Person sınıfından nesnelerden oluşan bir listeye çevirdik.
        for person in personsstr:
            newPerson = Person(pid=person[0],name=person[1],surname=person[2],age=person[3])
            persons.append(newPerson)
        return persons



    @staticmethod
    def Update(obj:Person):
        try:
            query = f"UPDATE Person SET Name=?,Surname=?,Age=? WHERE ID =?;"
            db = DbTools.ConnectDB()
            cursor = db.cursor()
            cursor.execute(query,(obj.Name,obj.Surname,obj.Age,obj.ID))
            db.commit()
            print("Update successfull!")
            DbTools.DisconnectDB()
        except Exception as error:
            print("Could not update!")
            print(error)

    @staticmethod
    def Delete(obj:Person):
        try:
            query = f"DELETE FROM Person WHERE ID ={obj.ID};"
            db = DbTools.ConnectDB()
            cursor = db.cursor()
            cursor.execute(query)
            db.commit()
            DbTools.DisconnectDB()
        except Exception as error:
            print("Could not delete!")
            print(error)

#if __name__=="__main__":
    # Create
    # newPerson = Person(name="John",surname="Doe",age=28)
    # PersonDB.Create(newPerson)
    
    # Read
    # listPersons = PersonDB.Read()
    # for person in listPersons:
    #     print(person)

    # Update
    # selectedPerson = listPersons[0]
    # print(selectedPerson.Name)
    # print(selectedPerson.Surname)
    # print(selectedPerson.ID)
    # print(selectedPerson.Age) # Age tanımsız. Boş.

    # selectedPerson.Age = 25
    # PersonDB.Update(selectedPerson) # ekledik ve güncelledik.

    # # Delete
    # listPersons = PersonDB.Read()
    # selectedPerson = listPersons[0]
    # print(selectedPerson.ID)
    # PersonDB.Delete(selectedPerson)






