
"""

1. gönderilen sayıların arasından en büyük üç sayıyı geri gönderen fonksiyonu yazınız
2. parametre olarak gönderilen bir metnin içinde ki büyük ve küçük harf sayılarını 
ekrana yazdıran python programını yazınız
Bonus soru 
Fonksiyon içindeki bir fonksiyona erişebilecek python kodu yazınız
"""

def count_upper_lower(Merhaba):
    upper_count = 0
    lower_count = 0
    
    for char in Merhaba :
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    print("Büyük harf sayısı:", upper_count)
    print("Küçük harf sayısı:", lower_count) 
