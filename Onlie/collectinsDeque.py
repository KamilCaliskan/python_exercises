from collections import deque

# Initialize an empty deque
d = deque()

# Number of operations
n = int(input())

# Perform operations
for _ in range(n):
    command, *args = input().split()
    getattr(d, command)(*args)

# Print the deque elements
print(*d)



'''
Tabii ki, adım adım açıklayalım:

1. `from collections import deque`: `collections` modülünden `deque` sınıfını içe aktarıyoruz
Bu, çift uçlu bir kuyruk yapısıdır

2. `d = deque()`: Bir boş deque nesnesi oluşturuyoruz

3. `n = int(input())`: Kullanıcıdan bir tamsayı girişi alıyoruz ve 
bu değeri `n` değişkenine atıyoruz. Bu değer, yapılacak işlemlerin sayısını belirtir

4. `for _ in range(n):`: Toplam işlem sayısı kadar bir döngü başlatıyoruz. `_` değişkeni, 
döngüdeki geçici bir değişkendir ve değeri önemli değildir

5. `command, *args = input().split()`: Kullanıcıdan bir giriş alıyoruz ve 
bu girişi boşluk karakterine göre ayırıyoruz. 
`.split()` yöntemi, giriş dizesini boşluk karakterine göre ayırarak bir liste döndürür.
`command` değişkenine listenin ilk öğesini, `args` değişkenine ise geri kalan öğeleri atarız. 
Bu sayede, kullanıcının girişinde verilen yöntem adını (`command`) ve bağlı argümanları (`args`) alırız.

6. `getattr(d, command)(*args)`: `getattr()` fonksiyonunu kullanarak deque (`d`) nesnesinde belirtilen yöntemi
(`command`) çağırıyoruz. Bu, kullanıcı tarafından verilen yöntemi dinamik olarak çalıştırmamızı sağlar
`*args`, yönteme bağlı argümanları iletilmesini sağlar

7. `print(*d)`: deque nesnesinin tüm elemanlarını ekrana yazdırırız. 
`*d`, deque nesnesinin elemanlarını ayırarak yazdırmamızı sağlar

Bu adımları takip ederek, kullanıcının verdiği yöntemlere göre deque üzerinde işlemler yapar
ve sonuç olarak deque'in tüm elemanlarını yazdırırız
'''
