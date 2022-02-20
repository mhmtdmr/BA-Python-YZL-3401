# Bu sınıfın amacı veritabanı işlemleri için bir şablon oluşturmaktır.
# Bu sınıftan kalıtım alındığında bu 4 metoddu tanımlamak zorunda olacağız.
# Dolayısı ile tüm veritabanı metotlarımızın adını bileceğiz.
# standart sağlar.

from abc import *
class CRUD:
    def __init__(self) -> None:
        pass

    @abstractstaticmethod
    def Create(obj):
        pass

    @abstractstaticmethod
    def Read():
        pass

    @abstractstaticmethod
    def Update(obj):
        pass

    @abstractstaticmethod
    def Delete(obj):
        pass


