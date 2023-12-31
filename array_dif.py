'''
You can implement the array_diff function in Python using a list comprehension

array_diff fonksiyonu, iki liste arasındaki farkı bulmayı amaçlayan bir Python fonksiyonudur
İki liste verilir: a ve b. Fonksiyon, a listesinden b listesinde bulunan tüm öğeleri çıkararak yeni bir liste döndürür
Eğer a listesinde bir öğe b listesinde varsa, tüm bu öğeler a listesinden çıkarılır
'''


def array_diff(a, b):
    # Use a list comprehension to filter elements from a that are not in b
    result = [x for x in a if x not in b]
    return result

# Test cases
print(array_diff([1, 2], [1]))       # Output: [2]
print(array_diff([1, 2, 2, 2, 3], [2]))  # Output: [1, 3]
