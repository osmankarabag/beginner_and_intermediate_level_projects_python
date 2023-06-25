def puan_hesapla(takimlar):
    takim_listesi = [['Alanyaspor', '11', '8', '16', '53', '65', 41, -12],
                      ['Antalyaspor', '10', '8', '16', '43', '53', 38, -10],
                      ['Kasimpasa', '12', '7', '15', '43', '53', 43, -10],
                      ['Kayserispor', '15', '4', '15', '54', '59', 49, -5],
                      ['Konyaspor', '12', '13', '9', '45', '37', 49, 8]]
    puanlar_sozlugu = {41: ('Alanyaspor',),
                       38: ('Antalyaspor',),
                       43: ('Kasimpasa',),
                       49: ('Kayserispor', 'Konyaspor', ),}

    for takim in takimlar:
        takim_adi = takim[0]
        galibiyet = int(takim[1])
        beraberlik = int(takim[2])
        maglubiyet = int(takim[3])
        attigi_gol = int(takim[4])
        yedigi_gol = int(takim[5])

        puan = galibiyet * 3 + beraberlik * 1
        averaj = attigi_gol - yedigi_gol

        takim_bilgileri = [takim_adi, galibiyet, beraberlik, maglubiyet, attigi_gol, yedigi_gol, puan, averaj]
        takim_listesi.append(takim_bilgileri)

        if puan in puanlar_sozlugu:
            puanlar_sozlugu[puan].append((takim_bilgileri[0], puan, averaj))
        else:
            puanlar_sozlugu[puan] = [(takim_bilgileri[0], puan, averaj)]

    return takim_listesi, puanlar_sozlugu

def takim_sirala(takim_listesi, puanlar_sozlugu):
    sirali_liste = []
    puanlar = list(puanlar_sozlugu.keys())
    puanlar.sort(reverse=True)

    for puan in puanlar:
        takimlar = puanlar_sozlugu[puan]

        if len(takimlar) > 1:
            for i in range(len(takimlar) - 1):
                for j in range(i + 1, len(takimlar)):
                    t1_index = None
                    t2_index = None
                    for k in range(len(takim_listesi)):
                        if takim_listesi[k][0] == takimlar[i]:
                            t1_index = k
                        elif takim_listesi[k][0] == takimlar[j]:
                            t2_index = k
                        if t1_index is not None and t2_index is not None:
                            break

                    if takim_listesi[t1_index][7] < takim_listesi[t2_index][7]:
                        takim_listesi[t1_index], takim_listesi[t2_index] = takim_listesi[t2_index], takim_listesi[t1_index]

        for takim in takimlar:
            for t in takim_listesi:
                if t[0] == takim:
                    sirali_liste.append(t)
                    break

    return sirali_liste
def dosyadan_takim_bilgilerini_cek(dosya_adi):
    takimlar = []

    with open(dosya_adi, 'r') as dosya:
        for satir in dosya:
            bilgiler = satir.strip().split(',')
            takimlar.append(bilgiler)

    return takimlar


def takimlari_siralama_dosya(dosya_adi):
    takimlar = dosyadan_takim_bilgilerini_cek(dosya_adi)
    takim_listesi, puanlar_sozlugu = puan_hesapla(takimlar)
    sirali_liste = takim_sirala(takim_listesi, puanlar_sozlugu)

    for takim in sirali_liste:
        print(takim)

    with open('sirali_liste.txt', 'w') as dosya:
        for takim in sirali_liste:
            dosya.write(', '.join(str(bilgi) for bilgi in takim) + '\n')

dosya_adi = 'takim_bilgileri.txt'
takimlari_siralama_dosya(dosya_adi)
