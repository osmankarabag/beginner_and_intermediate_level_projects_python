mevcutmaas = int(input('mevcut maas miktarınızı giriniz'))
zam = int(input("eski zam miktarı"))
cosay = int(input('kaç adet cocuğunuz var'))

if mevcutmaas < 3000:
    yenizam = mevcutmaas * 0.2
elif mevcutmaas < 4000:
    yenizam = mevcutmaas * 0.15
else:
    yenizam = mevcutmaas * 0.1

yenizam += cosay * 70

if zam > yenizam:
    yenizam=zam
print("Yeni zam miktarı: {} yeni Maas: {}".format(yenizam,mevcutmaas+yenizam))
