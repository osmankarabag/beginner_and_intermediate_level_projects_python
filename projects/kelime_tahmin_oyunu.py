#Osman Karabağ 19010011010
import random

# Kelime listesi
kelime_listesi = ["system", "data", "algorithm", "such", "base", "node", "model", "case",
"program", "information", "set", "code", "function", "process", "application", "software",
"class", "point", "type", "network", "tree", "object", "element", "input", "operation", "level",
"memory", "table", "order", "file", "variable", "language", "write", "list", "structure",
"compute", "sequence", "computer", "bit", "probability", "machine", "array", "page", "error",
"step", "search", "most", "path", "graph", "web", "length", "several", "security", "proof",
"access", "obtain", "matrix", "task", "image", "form", "return", "interface", "resource",
"address", "implementation", "loop", "first", "read", "location", "hardware", "behavior",
"programming", "field", "key", "parameter", "distribution", "definition", "instance",
"interaction", "internet", "representation", "edge", "stack", "return", "procedure",
"link", "output", "block", "domain", "store", "call", "device", "server", "static", "dataset",
"detection", "write", "execute", "least", "key"]

while True:
    kelime = random.choice(kelime_listesi)
    kelime_uzunluk = len(kelime)
    print(f"Kelimenin harf sayısı: {kelime_uzunluk}")

    # Harf sayısı kadar "_" yazdırma.
    gizlenmis_kelime = "_" * kelime_uzunluk
    print(gizlenmis_kelime)

    tahmin_hakki = (len(kelime) + 1) // 2
    yanlis_tahmin = 0
    puan = 0

    while True:
        tahmin = input("Bir harf tahmini yapın: ").lower()

        if tahmin in kelime:
            for i in range(kelime_uzunluk):
                if kelime[i] == tahmin:
                    gizlenmis_kelime = gizlenmis_kelime[:i] + tahmin + gizlenmis_kelime[i+1:]

            print(gizlenmis_kelime)

            # Puan hesaplama
            harf_adedi = kelime.count(tahmin)

            if tahmin in "aeiou":
                harf_puani = harf_adedi * 3
            else:
                harf_puani = harf_adedi * 2

            puan += harf_puani
            print(f"Güncel puanınız: {puan}, Kalan tahmin hakkınız: {tahmin_hakki - yanlis_tahmin}, Kelimenin durumu: {gizlenmis_kelime}")

            if "_" not in gizlenmis_kelime:
                kalan_tahmin_hakki = tahmin_hakki - yanlis_tahmin
                print(f"Doğru tahmin, Puanınız: {puan - yanlis_tahmin * 4}")
                break
        else:
            yanlis_tahmin += 1
            kalan_tahmin = tahmin_hakki - yanlis_tahmin
            puan -= 4
            print(f"Yanlış tahmin! Kalan hakkınız: {kalan_tahmin}, Güncel puanınız: {puan}, Kelimenin durumu: {gizlenmis_kelime}")

            if kalan_tahmin == 0:
                print(f"Kaybettiniz. Doğru kelime: {kelime}")
                break

    choice = input("Yeni kelime için 'y', çıkış yapmak için 'n' tuşlayın: ").lower()

    if choice == "n":
        break
