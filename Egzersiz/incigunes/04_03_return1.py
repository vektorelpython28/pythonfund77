
"""

Faktoriyel hesabı yapan bir fonksiyon yazalım 
fonksiyon sonucu dışarı return deyimi ile göndersin.
print fonksiyonu ve yazdığımız faktoriyel fonksiyonunu 
birlikte kullanıp sonucu
ekrana yazdıralım.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#print(factorial(5))





#def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result 

#print(factorial(5))


def separate_words(HelloWorld):
    words = []
    start = 0
    for i in range(len(HelloWorld)):
        if HelloWorld[i].isupper():
            words.append(HelloWorld[start:i])
            start = i
    words.append(HelloWorld[start:])
    return words
print(separate_words("HelloWorld"))



