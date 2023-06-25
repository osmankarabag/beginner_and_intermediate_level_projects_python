kelimeler = [['koza', 'koza', 'kitap', 'kalem'],
             ['edebiyat', 'sehpa', 'bardak', 'salep'],
             ['zil', 'zar'],
             ['televizyon', 'kilim', 'koza', 'bilgisayar', 'elektrikler'],
             ['yazılımcılar', 'zarf', 'takı']]


for i in range(len(kelimeler)):
    kelimeler[i] = list(set(kelimeler[i]))

def sesli_harf_sayisi(kelime):
    sesli_harfler = "aeıioöuü"
    sayac = 0
    for harf in kelime:
        if harf.lower() in sesli_harfler:
            sayac += 1
    return sayac

sesli_harf_listesi = []
for alt_liste in kelimeler:
    alt_liste_sesli_harfler = []
    for kelime in alt_liste:
        alt_liste_sesli_harfler.append(sesli_harf_sayisi(kelime))
    sesli_harf_listesi.append(alt_liste_sesli_harfler)

gruplanmis_kelimeler = []
for alt_liste in kelimeler:
    alt_liste_sesli_harfler = sesli_harf_listesi[kelimeler.index(alt_liste)]
    kelime_sozlugu = {}
    for i in range(len(alt_liste)):
        if alt_liste_sesli_harfler[i] not in kelime_sozlugu:
            kelime_sozlugu[alt_liste_sesli_harfler[i]] = [alt_liste[i]]
        else:
            kelime_sozlugu[alt_liste_sesli_harfler[i]].append(alt_liste[i])
    gruplanmis_kelimeler.append(kelime_sozlugu)

sesli_harf_sayisi = []
en_sesli_kelimeler = {}
for kelime_sozlugu in gruplanmis_kelimeler:
    sesli_harf_sayilari = list(kelime_sozlugu.keys())
    sesli_harf_sayilari.sort()
    sesli_harf_sayisi.append(sesli_harf_sayilari)
    en_sesli_harf_sayisi = max(sesli_harf_sayilari)
    en_sesli_kelime = sorted(kelime_sozlugu[en_sesli_harf_sayisi])[0]
    en_sesli_kelimeler[en_sesli_kelime] = en_sesli_harf_sayisi

print("sesli_harf_sayisi =", sesli_harf_sayisi)
print("en_sesli_kelimeler =", en_sesli_kelimeler)
