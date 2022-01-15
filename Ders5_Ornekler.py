# 1-1000 arasındaki sayıların karelerini toplayan programı yazınız.
# istisna : kullanıcıdan alınan sayının katları toplama dahil edilmesin.

# toplam = 0
# n = int(input("sayı:"))
# for i in range(1000):
#     if(i%n!=0):
#         toplam += (i**2)
# print("kareler toplamı",toplam)

# Kullanıcıdan 10 sayı alıp bu sayıları tekler ve çiftler olarak ayrı ayrı toplayan program.

tekToplam = 0
ciftToplam = 0
for i in range(10):
    sayi = int(input("sayı:"))
    if(sayi%2==0):
        ciftToplam+=sayi
    else:
        tekToplam+= sayi
print(f"Tekler Toplamı: {tekToplam}\nÇiftler Toplamı: {ciftToplam}")