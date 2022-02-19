# Çok biçimlilik
class Kedi:
    def __init__(self) -> None:
        pass
    def SesCikar(self):
        print("Miyav miyav")

class Kopek:
    def __init__(self) -> None:
        pass
    def SesCikar(self):
        print("Hav hav")

class Kus:
    def __init__(self) -> None:
        pass
    def SesCikar(self):
        print("Cik cik")
# BA203

# Ara Metot
def SesCikar(hayvan):
    hayvan.SesCikar()

if __name__=="__main__":
    kedi = Kedi()
    kopek = Kopek()
    kus = Kus()
    # Aynı isimli metodun farklı davranışlar göstermesi bir polimorfizm örneğidir.
    # kedi.SesCikar()
    # kopek.SesCikar()
    # kus.SesCikar()
    SesCikar(kedi)  # SesCikar metodunun davranışı veya ürettiği sonuç aldığı nesneye göre değiştir.
    SesCikar(kopek)
    SesCikar(kus)
    