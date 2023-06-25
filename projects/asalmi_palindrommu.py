#19010011010
#Osman Karabağ
# sayı asalmı değilmi kontrol
def asalmi(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
#palindrom mu?
def palindrommu(n):
    return str(n) == str(n)[::-1]
#basamaklar tüm rakamlar farklı mı?
def basamaklar_farklimi(n):
    basamaklar = set(str(n))
    return len(basamaklar) == len(str(n))

sayi = int(input("Sayı giriniz: "))

alt_sinir = sayi
ust_sinir = sayi

while True:
    if asalmi(alt_sinir):
        en_yakin_asal = alt_sinir
        break
    elif asalmi(ust_sinir):
        en_yakin_asal = ust_sinir
        break
    alt_sinir -= 1
    ust_sinir += 1

if not basamaklar_farklimi(en_yakin_asal):
    print(f"En Yakın Asal Sayı = {en_yakin_asal}, Basamakların Tümü Farklı Değil, ", end="")
else:
    print(f"En Yakın Asal Sayı = {en_yakin_asal}, Basamakların Tümü Farklı, ", end="")

if palindrommu(en_yakin_asal):
    print("Palindrome")
else:
    print("Palindrome Değil")
