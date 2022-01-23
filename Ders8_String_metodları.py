###################################     Hazır String Fonksiyonları    ##################################
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle() 	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning



# # metin parçalama
# kelimeler = "Bugün.hava.çok.sıcak.değildi."
# # kelimeListe = kelimeler.split(".") # kelimeler metnini parçala. . lardan itibaren.
# # print(kelimeListe)

# kelimeListe = kelimeler.split(".",3) # kelimeler metnini parçala. . lardan itibaren. ilk 3 parçayı .'lardan parçala
# for k in kelimeListe:
#     print(k)
#     print(len(k))

# metin = "Bugün İstanbul'a kar yağdı."
# print(metin)
# metin = metin.replace("kar","yağmur")
# print(metin)

# ÖRNEK
# cumle,yasaklı kelimeler şeklinde parametre alacak.
# cumledeki yasaklı kelimeleri *** olarak değiştirip cümleyi döndürecek metodu tanımlayınız. Örnek: Filtrele("Hava çok soğuk","çok","soğuk") => Hava *** ***

# def Sansur(cumle:str,*sansurluKelimeler):
#     for kelime in sansurluKelimeler:
#         cumle = cumle.replace(kelime,"***")
#     return cumle


# sansurluCumle = Sansur("Hava çok soğuk","çok","soğuk")
# print(sansurluCumle)
# sansurluCumle = Sansur("Hava çok da soğuk değildi","soğuk")
# print(sansurluCumle)

## Cümle içinde geçen TC kimlik numarasını * ile değiştiren fonksiyonu tanımlayınız.
# koşullar: sadece 11 tane rakamı yanyana gördüğünde değiştirsin.
# ÖRNEK:  Benim adım Sedat, Yaşım 27 telefonum 5439999999 Tc kimlik numaram 18273645321
# ÇIKTI:  Benim adım Sedat, Yaşım 27 telefonum 5439999999 Tc kimlik numaram ***********
# split,isnumeric,len     

def TCGizle(metin:str):
    kelimeler = metin.split(" ") # boşluklardan parçala
    yeniMetin = ""
    for kelime in kelimeler:
        if(len(kelime)==11 and kelime.isnumeric()):
            yeniMetin += "*********** "
        else:
            yeniMetin += kelime+" "
    return yeniMetin

cumle = "Benim adım Sedat, Yaşım 27 telefonum 5439999999 Tc kimlik numaram 18273645321"
print(TCGizle(cumle))


# SORU:
'''
You have a text that some of the words in reverse order.
The text also contains some words in the correct order, 
and they are wrapped in parenthesis.
Write a function fixes all of the words and,
remove the parenthesis that is used for marking the correct words.

Your function should return the same text defined in the constant 
CORRECT_ANSWER
'''
'''
INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon
         ,tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc
         noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif
         (American) srohtua (to) emoceb (an) lanoitanretni ytirbelec
         (and) nrae a egral enutrof (from)).gnitirw")

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"


def fix_text(mystr):
    #Write your alghoritm here.
    return mystr

if __name__ == "__main__":
    print("Correct!" if fix_text(INPUT) == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")
'''
