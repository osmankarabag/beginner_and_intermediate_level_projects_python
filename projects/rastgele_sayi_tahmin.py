import random
rsayi = random.randint(1,100)
print(rsayi)
secimhak=5
hak = 0
kontrol=0
while hak <= secimhak:
    tsayi = int(input("tahmin giriniz"))
    if tsayi > rsayi:
        print("daha kücük bir sayi giriniz")
    elif tsayi < rsayi:
        print("daha buyuk bir sayi giriniz")
    else:
        print("Dogru tahmin ettiniz Sayi : {}".format(rsayi))
        hak = secimhak
        kontrol=1
    hak = hak+1
if kontrol==0:
    print("Dogru tahmin edemediniz {} secim hakkınız doldu".format(secimhak))
