import os
filename = "04_03_FonksiyonOdev"
liste = os.listdir("Egzersiz/")
for item in liste:
    with open(f"Egzersiz/{item}/{filename}.py","w+",encoding="UTF-8") as dosya:
        metin = """
\"\"\"

1. gönderilen sayıların arasından en büyük üç sayıyı geri gönderen fonksiyonu yazınız
2. parametre olarak gönderilen bir metnin içinde ki büyük ve küçük harf sayılarını 
ekrana yazdıran python programını yazınız
Bonus soru 
Fonksiyon içindeki bir fonksiyona erişebilecek python kodu yazınız
\"\"\"

"""
        dosya.write(metin)
# TODO veri tabanı bağlantrısı


# https://codeshare.io/eVn8ml
