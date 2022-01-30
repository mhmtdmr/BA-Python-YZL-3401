import os
basePath = "C:\\Users\\Bilge Adam\\Desktop\\BA-Python-YZL-3401\\"
fileName = "Ders10_isimnot.txt"
filePath = basePath+fileName

file = os.open(filePath,os.O_RDONLY)
file = os.read(file,500) 
#b'G\xc3\xbclcanKaraca 65\nMesutYi\xc4\x9fit 85\nSerthatDemir 80\n\n'
file = file.decode('utf-8','ignore')
print(file)
# GülcanKaraca 65
# MesutYiğit  85 
# SerthatDemir 80

lines = file.split("\n")
print(lines)
# ['GülcanKaraca 65', 'MesutYiğit  85', 'SerthatDemir 80', '']
del lines[-1]
print(lines)
# ['GülcanKaraca 65', 'MesutYiğit  85', 'SerthatDemir 80']  

for line in lines:
    words = line.split(" ") # Her kaydı boşluklardan parçala
    isim = words[0]
    notu = words[1]
    print(f"Öğrenci: {isim}  Not: {notu}")
