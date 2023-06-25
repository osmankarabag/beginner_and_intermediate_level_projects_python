#19010011010 Osman Karabağ
while True:
    print("1- İkilik tabandaki sayıyı onluk tabana çevir")
    print("2- Onluk tabandaki sayıyı ikilik tabana çevir")
    print("3- Çıkış")
    secim = input("Seçiminizi girin: ")


    if secim == "1":
        while True :
            ikilik_sayi = input("Lütfen bir ikilik sayı girin: ")
            if set(ikilik_sayi) <= {"0", "1"}:
                break
            else:
                print("Hatalı giriş yaptınız! Sadece 0 ve 1 rakamlarını kullanın.")

        onluk_sayi = int(ikilik_sayi, 2)
        print(f"{ikilik_sayi} sayısı {onluk_sayi} sayısına eşittir.")



    elif secim == "2":
        onluk_sayi = int(input("Lütfen bir onluk tabanındaki sayı girin: "))
        ikilik_sayi = bin(onluk_sayi)[2:]
        print("İkilik tabandaki karşılığı:", ikilik_sayi)

    elif secim == "3":
        print("Program sonlandırılıyor...")
        break

    else:
        print("Hatalı seçim. Lütfen tekrar deneyin.")
