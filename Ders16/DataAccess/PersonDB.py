from Base.CRUD import CRUD
from Entity.Person import Person
class PersonDB(CRUD):
    """
    Bu sınıf kendisine parametre olarak gelen Person 
    nesnesinin veritabanı işlemlerini yapar.
    """   
    @staticmethod
    def Create(obj:Person):
        pass

    @staticmethod
    def Read(obj:Person):
        pass

    @staticmethod
    def Update(obj:Person):
        pass

    @staticmethod
    def Delete(obj:Person):
        pass