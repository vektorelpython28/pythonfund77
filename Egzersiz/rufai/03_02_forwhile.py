
"""
sayısal loto oyununda 1,49 sayıları arasındaki sayılardan 
6 adet sayının seçilmesi gerekmektedir.
1. Alternatif 
from random import randint
randint(1,49)
2. Alternatif
from random import choice
liste = [i for i in range(1,50)]

yukarıdaki kod bloklarında faydalanarak 
istenilen sayıda sayısal loto kolonu oynayan python kodunu 
yazınız
ipucu while ve for döngüleri birlikte kullanılmaktadır. 
"""
# import random
# for i in range(1,7):
#     a=random.randint(1,49)
#     print(a)
#yukardaki kolay yol

# from random import randint
# for i in range(6):
#      a=randint(1, 49)
#      print(a,end=' ')

sayi = input('Lütfen 6 basamaklı bir sayı giriniz:')
if sayi and sayi.isdigit():
    sayi = int(sayi)

birlerbsm = sayi%10
onlarbsm = (sayi%100)//10
yuzlerbsm = (sayi%1000)//100
binlerbsm = (sayi%10000)//1000
onbinlerbsm = (sayi%100000)//10000
yuzbinlerbsm = (sayi%1000000)//100000

print("birlerbsm =",birlerbsm,end='\n')
print("onlarbsm =",onlarbsm,end='\n')
print("yuzlerbsm =",yuzlerbsm,end='\n')
print("binlerbsm =",binlerbsm,end='\n')
print("onbinlerbsm =",onbinlerbsm,end='\n')
print("yuzbinlerbsm =",yuzbinlerbsm,end='\n')

