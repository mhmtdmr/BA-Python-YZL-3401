# 
# Erişim Seviyeleri:
# public: Heryerden erişilebilir.
# private: Sadece sınıf içerisinden erişilebilir.
# protected: Sınıf içerisinden ve alt sınıflardan(miras alan sınıflar) erişilebilir. 

# Erişim Seviyeleri Kullanımı:
# public: Varsayılan olarak tüm özellik ve metotlar public'tir.
# private: özellik veya metot isminin önüne '__' (2 tane alt çizgi) koyularak private yapılabilir.
# protected: özellik veya metot isminin önüne '_' (1 tane alt çizgi) koyularak protected yapılabilir.
class A:
    def __init__(self) -> None:
        self.__ID = int()       #private
        self._Brand = str()     #protected
        self.Information = str()#public

    def __GetID(self):          #private
        return self.__ID 
               
    def _GetBrand(self):        #protected
        return self._Brand     

    def GetInformation(self):   #public
        return self.Information 

    def WriteAllInfo(self):
        print(f"""\t\tALL INFORMATION
        ---------------
        ID      :{self.__ID}
        Brand   :{self._Brand}
        Info    :{self.Information}
        ---------------
        """)

class B:
    __ID_Counter = 0   # ID sayacı.
    def __init__(self) -> None:
        B.__ID_Counter += 1 # her nesne oluştuğunda ID sayacı otomatik 1 artsın.
        self.__ID = B.__ID_Counter # Yeni nesnenin ID'si otomatik belirlendi.
        self.__Email = str()    #private
        self.__Password = str() #private
    
    def SetEmail(self,value:str):   #public
        # Kapsülleme sayesinde bir sınıf özelliğine kontrollü atama yapabiliriz.
        if(('@' in value) and ('.' in value)):
            self.__Email = value
        else:
            print("Eposta hatalı !!!\nAtama başarısız !!!")

    def GetEmail(self):
        return self.__Email

    def SetPassword(self,value:str):
        if(len(value)>=9 and not value.isalpha() and not value.isnumeric()): # parola en az 9 karakterden oluşuyorken numara ve harf içeriyorsa
            self.__Password = value
            print("Parola ayarlandı!")
        else:
            print("Parola kriterlere uygun değil.\nEn az 9 karakterli olmalı ve sayı ve karakterler içermelidir!")
    
    # __Password özelliğine atama yapılabiliyorken okuma yapılmıyor.
    # Sınıf dışında sadece yazılabilir özellikte okuma yapılamaz.

    # Yukarıdaki örneğe benzer şekilde sadece okunabilir(readonly) özellikler de tanımlanabilir. Aşağıdaki gibi

    def GetID(self):
        return self.__ID





    




