# https://codeshare.io/BA3401

# Atama / İşlemli Atama Operatörleri

sayi = 5
sayi += 3 # sayi = sayi + 3
sayi *= 2 # sayi = sayi * 2
sayi /= 4 # sayi = sayi / 4
sayi -= 2 # sayi = sayi - 2

###  Aritmetik Operatörler   ###
#  +,-,*   : toplama,çıkarma,çarpma
#  /  : ondalıklı bölme (10/4=2.5)
# / /: tamsayı bölme (10//4=2)
#  ** : üs alma (5**2)=25
# % : modunu alma. (25%2) => 1. 25'in 2 ile bölümünden kalan

# Karşılaştırma Operatörleri

sayi1 = 4
sayi2 = 8
bool1 = (sayi1 == sayi2) # eşitse True değilse False
bool2 = (sayi1 != sayi2) # eşitse False değilse True
bool3 = (sayi1 >= sayi2) # büyük veya eşitse True, küçükse False
bool4 = (sayi1 <= sayi2) # küçük veya eşitse True, küçük False

kontrol = sayi1>5 and sayi2>5 # her iki sayı da 5'ten büyük ise True en az biri şartı sağlamıyor ise False
print(f"her iki sayı da 5'ten büyük mü ? :",kontrol)

kontrol = sayi1>5 or sayi2>5 # iki sayıdan en az 1 tanesi 5'ten büyük ise True ikisi de şartı sağlamıyor ise False
print(f"iki sayıdan en az 1 tanesi 5'ten büyük mü ? :",kontrol)

kontrol =  (sayi1>5 and sayi2>5) or (sayi2<9) # True
print(kontrol)