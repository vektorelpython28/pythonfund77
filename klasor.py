import os
filename = "03_02_forwhile"
liste = os.listdir("Egzersiz/")
for item in liste:
    with open(f"Egzersiz/{item}/{filename}.py","w+",encoding="UTF-8") as dosya:
        metin = """
\"\"\"
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
\"\"\"
"""
        dosya.write(metin)
# TODO veri tabanı bağlantrısı


# https://codeshare.io/eVn8ml
