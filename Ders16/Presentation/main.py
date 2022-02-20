

import os,sys
p = os.path.abspath(".")
sys.path.insert(1,p)

from Entity.Person import Person
from DataAccess.PersonDB import PersonDB

if __name__=="__main__":
    # Create
    # newPerson = Person(name="John",surname="Doe",age=28)
    # PersonDB.Create(newPerson)
    
    # Read
    listPersons = PersonDB.Read()
    for person in listPersons:
        print(person)

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



    # Departman : ID,Name,Description,ManagerID
    # Yukarıdaki sınıfa ait tabloyu veritabanında oluşturun.
    # Bu sınıfın veritabanı işlemleri için gerekli olan DepartmanDB.py 
    # dosyasını CRUD'dan miras alarak yazınız.