#######################
#######   tuple   #####
#######################
# Listeden farklı olarak readonly:sadece okunabilir
# yapıdadırlar

# degismezListe = tuple()
# degismezListe = ()
# degismezListe = (10,20,30)

# print(len(degismezListe))
# print(min(degismezListe))
# print(max(degismezListe))
# print(sum(degismezListe))

# degismezListe[0] #0. indisi al.
# degismezListe.index(20) # 20 sayısının indisi
# degismezListe.count(10) # 10 elemanı listede kaç defa var?


#######################
#######    set    #####
#######################

#matematikteki kümeler
# kume = set()
# kume = {}
# kume = {10,20,20,20,5}
# print(kume)

setA = {'A','B','C'}
setB = {'A','D','F'}

# setAFarkB = setA-setB
# setAFarkB = setA.difference(setB)
# print(setAFarkB)

# setBFarkA = setB-setA
# setBFarkA = setB.difference(setA)
# print(setBFarkA)

# setAusetB= setA.union(setB)
# print(setAusetB)

# setAkesisimsetB = setA.intersection(setB)
# setAkesisimsetB = setA & setB
# print(setAkesisimsetB)

setC = set()
setC.add('C')
setC.add('Y')
setC.discard('Y') # eleman yoksa hata vermez.
# setC.remove('Y') # eleman yoksa hata verir.

print(setA)
print(setB)
print(setC)

print(setA.issuperset(setB))
print(setA.issuperset(setC))

print(setC.issubset(setB))
print(setC.issubset(setA))