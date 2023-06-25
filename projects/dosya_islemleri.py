def islem_yap_ve_yaz(dosya_adı):
    yeni_dosya_adı = "sonuclar.txt"  # Oluşturulacak yeni dosyanın adı
    yeni_dosya = open(yeni_dosya_adı, "w")  # Yeni dosyayı yazma modunda aç

    with open(dosya_adı, "r") as dosya:
        for satır in dosya:
            satır = satır.strip()  # Satır sonundaki boşlukları kaldır

            # İşlemi ve operatörü ayırarak işlemi gerçekleştir
            operatorler = ["+", "-", "*", "/", "^"]
            for operator in operatorler:
                if operator in satır:
                    sayilar = satır.split(operator)
                    sayi1 = float(sayilar[0])
                    sayi2 = float(sayilar[1])
                    sonuc = None

                    if operator == "+":
                        sonuc = sayi1 + sayi2
                    elif operator == "-":
                        sonuc = sayi1 - sayi2
                    elif operator == "*":
                        sonuc = sayi1 * sayi2
                    elif operator == "/":
                        sonuc = sayi1 / sayi2
                    elif operator == "^":
                        sonuc = sayi1 ** sayi2

                    yeni_dosya.write(f"{satır} = {sonuc}\n")  # Yeni dosyaya sonucu yaz

    yeni_dosya.close()
    print(f"Sonuçlar {yeni_dosya_adı} dosyasına yazıldı.")

# Fonksiyonu kullanarak dosyayı işle
dosya_adı = "C:\\Users\\mrtkr\\PycharmProjects\\pythonProject\\islemler.txt"  # İşlem yapılacak dosyanın adı
islem_yap_ve_yaz(dosya_adı)
