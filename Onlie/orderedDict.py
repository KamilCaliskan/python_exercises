from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    item, _, price = input().rpartition(' ')
    items[item] = items.get(item, 0) + int(price)

for item, price in items.items():
    print(item, price)



'''
Tabii ki, adım adım açıklayalım:

1. `from collections import OrderedDict`: İlk olarak, `collections` modülünden `OrderedDict` sınıfını içe aktarıyoruz. 
Bu sınıf, eklenme sırasını hatırlayan bir sözlük türüdür.

2. `n = int(input())`: Kullanıcıdan bir tamsayı girişi alıyoruz ve bu değeri `n` değişkenine atıyoruz. 
Bu değer, satın alınan öğelerin sayısını temsil eder.

3. `items = OrderedDict()`: Bir `OrderedDict` nesnesi oluşturuyoruz. 
Bu, öğelerin adlarını ve fiyatlarını tutmak için kullanılacaktır.

4. `for _ in range(n):`: Satın alınan her öğe için bir döngü başlatıyoruz. `_` değişkeni, 
döngüdeki geçici bir değişkendir ve değeri önemli değildir.

5. `item, _, price = input().rpartition(' ')`: Kullanıcıdan bir giriş alıyoruz ve 
bu girişi boşluk karakterine göre ayırıyoruz. `.rpartition()` yöntemi, giriş dizesini sağdan sola doğru tarar ve 
verilen ayırıcıyı bulduğunda, sol ve sağ kısımları ile ayırıcının kendisini içeren bir üçlü döndürür. 
Burada, öğe adını (`item`) ve fiyatı (`price`) alıyoruz, ancak ayırıcıya ihtiyacımız yok, 
bu yüzden `_` değişkenini kullanıyoruz.

6. `items[item] = items.get(item, 0) + int(price)`: 
Satın alınan öğenin adını anahtar olarak kullanarak `items` sözlüğüne erişiyoruz.
Eğer öğe zaten sözlükte varsa, `get()` yöntemiyle onun mevcut değerini alıyoruz. 
Eğer yoksa, varsayılan olarak 0 değerini kullanıyoruz. Daha sonra, 
fiyatı bir tamsayıya dönüştürüyoruz ve mevcut değere ekliyoruz. Sonuç olarak, 
her öğenin toplam fiyatını `items` sözlüğünde saklamış oluyoruz.

7. `for item, price in items.items():`: `items` sözlüğündeki her öğe için bir döngü başlatıyoruz. 
Her döngüde, öğe adını (`item`) ve toplam fiyatını (`price`) alıyoruz.

8. `print(item, price)`: Öğe adını ve toplam fiyatını ekrana yazdırıyoruz.

Bu adımları izleyerek, kullanıcının girdiği öğelerin adlarını ve 
toplam fiyatlarını sırayla yazdıracak 
bir program oluşturmuş oluyoruz.
'''
