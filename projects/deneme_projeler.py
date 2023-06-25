""" x = int(input('kaç sayi giremek istersiniz'))
sayac=0
karetoplam=0
while sayac < x:
    sayi = int(input('sayi giriniz:'))
    sayac += 1
    karetoplam += sayi**2
print(karetoplam)
temp = sayi = int(input('sayi giriniz:'))
x = 0
while sayi != 0:
    basamak = sayi % 10
    sayi = sayi - basamak
    sayi /= 10
    x += basamak
print("{} sayisinin basamak toplamı {}". format(temp,x))

toplam = 0
ort = 0
for i in range(1,6):
    sayi = int(input('sayi giriniz'))
    toplam += sayi
    ort = toplam/5
print(toplam)
print(ort)
import random
a = random.random() #0 ie 1 arasında random sayı oluşturur
# randint değer aralığı verirsek (9,19) bu aralıkta şeçim yapar
print(a)
#random.choice() liste içinden seçim yapar rastgele
a="osman"
b="a"
if b in a :
    print("var")
else:"""
Ali = [4,7,2,10,9,3]
Beyza = [5,2,6,10,4,6]
aliskor = 0
beyzaskor = 0
for i in range(len(Ali)):
    if Ali[i] > Beyza[i]:
        aliskor +=1
    elif Beyza[i] > Ali[i]:
        beyzaskor += 1
print(aliskor)
print(beyzaskor)




