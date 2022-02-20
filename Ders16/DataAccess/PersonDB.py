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
            cursor = db.cursor()
            cursor.execute(query,(obj.Name,obj.Surname,obj.Age))
            db.commit()
            print("Insert Done.")
            DbTools.DisconnectDB()
        except Exception as error:
            print("Could not insert person to database!")
            print(error)


    @staticmethod
    def Read():
        persons = list()
        personlist = list()
        try:
            query = "SELECT * FROM Person;"
            db = DbTools.ConnectDB()
            cursor = db.cursor()
            cursor.execute(query)
            personlist = cursor.fetchall()
            DbTools.DisconnectDB()
        except Exception as error:
            print("Could not read from database!")
            print(error)

        for person in personlist:
            newPerson = Person(pid=person[0],name=person[1],surname=person[2],age=person[3])
            persons.append(newPerson)
        return persons



    @staticmethod
    def Update(obj:Person):
        pass

    @staticmethod
    def Delete(obj:Person):
        pass

if __name__=="__main__":
    newPerson = Person(name="John",surname="Doe",age=28)
    # PersonDB.Create(newPerson)
    print(PersonDB.Read())



