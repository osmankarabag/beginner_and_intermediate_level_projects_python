import random
while True:
    mayintarlasi = []
    while True:
        alanboyut = int(input("Oynamak istediginiz oyun alaninin boyutunu giriniz = "))
        if (alanboyut < 10 ) :
            print("Oyun alanını en az 10 olacak şekilde tekrar giriniz... ")
        else :
            break
    skor = 0
    for i in range(alanboyut):
        mayintarlasi.append(["?"]*alanboyut)
    def  tarlayazdir(mayintarlasi):
        for satir in mayintarlasi :
            print(" ".join(satir))
 # mayin oluşturma
    def rastgele_koordinat(mayintarlasi):
        return random.randint(1, len(mayintarlasi) - 1)
    mayinsay = int(alanboyut * alanboyut * 0.30)
    mayinlar = []
    for i in range(mayinsay):
        mayinlar += [[rastgele_koordinat(mayintarlasi), rastgele_koordinat(mayintarlasi)]]
    # mayin kontrolü
    for i in mayinlar :
        if mayinlar.count(i) > 1 :
            mayinlar.remove(i)
            mayinlar.append([rastgele_koordinat(mayintarlasi),rastgele_koordinat(mayintarlasi)])
        else:
            continue


    def count_adjacent_mines(mayintarlasi, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if x + i < 0 or x + i >= len(mayintarlasi) or y + j < 0 or y + j >= len(mayintarlasi[0]):
                    continue
                if mayintarlasi[x + i][y + j] == "X":
                    count += 1
        return count
    
    # oyun oynama
    print(" Oyunu oynamak istediğiniz modu seçin. \n 1-) Gizli mod , 2-) Açık mod")
    secim = input("Seciminiz : ")

    if secim == "1":  # gizli mod
        tarlayazdir(mayintarlasi)
        while True:
            satir = int(input("Satır degeri :"))
            sutun = int(input("Sutun degeri : "))

            tahmin = [satir, sutun]

            if tahmin in mayinlar:
                for i in range(mayinsay):
                    mayintarlasi[mayinlar[i-1][0]-1][mayinlar[i-1][1]-1]="X"
                tarlayazdir(mayintarlasi)
                print("Maalesef mayina bastiniz....!!!! ")
                break
            else :
                skor += 1
                if tahmin[0] < 0 or tahmin[1] < 0 or tahmin[0] > alanboyut or tahmin[1] > alanboyut:
                    skor -= 1
                    print("Oyun alani disinda tahmin yaptiniz. ")
                    tarlayazdir(mayintarlasi)
                elif mayintarlasi[satir-1][sutun-1] == "*":
                    skor -= 1
                    tarlayazdir(mayintarlasi)
                    print("Zaten bu koordinati tahmin ettiniz...")
                else:
                    mayintarlasi[satir - 1][sutun - 1] = "*"
                    tarlayazdir(mayintarlasi)
    elif secim == "2": #acıkmod
        for i in range(mayinsay):
            mayintarlasi[mayinlar[i - 1][0] - 1][mayinlar[i - 1][1] - 1] = "X"
        tarlayazdir(mayintarlasi)
        while True:
            satir = int(input("Satir degeri :"))
            sutun = int(input("Sutun degeri : "))
            tahmin = [satir, sutun]
            if tahmin in mayinlar:
                for i in range(mayinsay):
                    mayintarlasi[mayinlar[i - 1][0] - 1][mayinlar[i - 1][1] - 1] = "X"
                tarlayazdir(mayintarlasi)
                print("Maalesef mayina bastiniz....!!!! ")
                break
            else:
                skor += 1
                if tahmin[0] < 0 or tahmin[1] < 0 or tahmin[0] > alanboyut or tahmin[1] > alanboyut:
                    skor -= 1
                    print("Oyun alani disinda tahmin yaptiniz. ")
                    tarlayazdir(mayintarlasi)
                elif mayintarlasi[satir-1][sutun-1] == "*":
                    skor -= 1
                    tarlayazdir(mayintarlasi)
                    print("Zaten tahmin ettiniz...")
                else:
                    mayintarlasi[satir - 1][sutun - 1] = "*"
                    tarlayazdir(mayintarlasi)
    if skor >= 1 :
        print("SKORUNUZ : {} PUAN".format(skor))
    elif skor == (alanboyut*0.7) :
        print("Tebrikler tum mayinsiz bolgeleri buldunuz...")
        break
    print("Oyun sonlandı... \n Tekrar oynamak icin 1 cikis icin 2 tusuna basiniz..... ")
    secim2 = input("Seciminiz : ")
    if secim2 == "2":
        break
    elif secim2 == "1" :
        continue
    else:
        print("Yanlis secim yaptiniz lutfen tekrar seciniz !!!! ")
        secim2 = input("Seciminiz : ")