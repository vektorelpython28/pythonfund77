
"""

Faktoriyel hesabı yapan bir fonksiyon yazalım 
fonksiyon sonucu dışarı return deyimi ile göndersin.
print fonksiyonu ve yazdığımız faktoriyel fonksiyonunu 
birlikte kullanıp sonucu
ekrana yazdıralım.
"""
#n=3
# for i in range(n):
#     n=n*(i+1)
# print("Deger :",n)
########################
n=3
def faktor(n):
    l = 1
    for i in range(n):
        l = l*(i+1) # l *= i+1
    return l

print(faktor(5))