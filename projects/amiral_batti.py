from random import *
print("\t\t****  AMİRAL BATTI OYUNU  ****\n")

tahmin = [[9999,9999]]
hak = 999999
tablo = []
gtablo = []
gemiler = []
gemi_1 = []
gemi_2 = []
gemi_3 = []
gemi_4 = []
sayac1 = 0
sayac2 = 0
sayac3 = 0
gsayac = 0
gsayac1 = 0
gsayac2 = 0
gsayac3 = 0
atissayac = 0
atiskontrol = 0
gatis = 0
gatiskontrol = 0

def oyunalani2():
    global gir
    global gtablo
    for i in range(0,gir):
        gtablo.append([])
        for j in range(0,gir):
            gtablo[i].append("?")
    return gtablo

def oyun_alani1():
    global gir
    global tablo
    for i in range(0, gir):
        tablo.append([])
        for j in range(0, gir):
            tablo[i].append("?")

def oyun_alani():
    global tablo
    for a in tablo:
        print("  ".join(a))


def G_oyun_alan():
    global gtablo
    for a in gtablo:
        print("  ".join(a))


def menu():
    global gir
    global tablo
    global gtablo
    tablo = []
    gtablo = []
    gir = int(input("Oyununuzu kaç boyutta oynamak istiyorsunuz (10X10 = 10 olarak yazın) => "))

    print("\n1) Görünür mod (Gemiler size gözükür) => 1 ")
    print("2) Oyuncu mod => 2 ")
    print("3) Exit => 3")
    print("\nOyunu hangi modda oynamak istiyorsanız yanındaki sayıyı girin\n")
    bolum = int(input("İstediğiniz işlemi seçin => "))

    if bolum == 1:
        print("\n" * 30)
        acikmod()

    if bolum == 2:
        print("\n" * 30)
        oyucumod()

    if bolum == 3:
        exit(404)




def kontrol2(x,y,boyut,yon):

    if tablo[x][y] == "@":
        return False
    if yon == 0:
        for i in range(1, boyut):
            if tablo[x + i][y] == "@":
                return False
    if yon == 1:
        for j in range(1, boyut):
            if tablo[x - j][y] == "@":
                return False
    if yon == 2:
        for a in range(1, boyut):
            if tablo[x][y + a] == "@":
                return False

    return True


def kontro1(x,y,boyut):

    if (x+boyut) > (gir-1) or (x-boyut) < 0:
        return False
    if (y+boyut) > (gir-1) or (y-boyut) < 0:
        return False

    return True

def gemi4():
    global gir
    global gemiler
    global gemi_4

    x = randint(0,gir - 1)
    y = randint(0,gir - 1)
    yon = randint(0,2)

    kontro1(x,y,4)

    if kontro1(x,y,4) == False:
        return gemi4()
    if kontro1(x,y,4) == True:
        tablo[x][y] = "@"
        gemi_4.append([x, y])
        gemiler.append([x, y])

        if yon == 0:
            for i in range(1, 4):
                tablo[x + i][y] = "@"
                gemiler.append([x + i, y])
                gemi_4.append([x + i, y])
        if yon == 1:
            for j in range(1, 4):
                tablo[x - j][y] = "@"
                gemiler.append([x - j, y])
                gemi_4.append([x - j, y])

        if yon == 2:
            for a in range(1, 4):
                tablo[x][y + a] = "@"
                gemiler.append([x, y + a])
                gemi_4.append([x, y + a])



def gemi3():
    global gir
    global gemiler
    global gemi_3
    x = randint(0, gir - 1)
    y = randint(0, gir - 1)
    yon = randint(0,2)

    kontro1(x,y,3)

    if kontro1(x,y,3) == False:
        return gemi3()

    if kontro1(x,y,3) == True:
        kontrol2(x,y,3,yon)
        if kontrol2(x,y,3,yon) == False:
            return gemi3()
        if kontrol2(x,y,3,yon) == True:
            tablo[x][y] = "@"
            gemi_3.append([x, y])
            gemiler.append([x, y])

            if yon == 0:
                for i in range(1, 3):
                    tablo[x + i][y] = "@"
                    gemiler.append([x + i, y])
                    gemi_3.append([x + i, y])
            if yon == 1:
                for j in range(1, 3):
                    tablo[x - j][y] = "@"
                    gemiler.append([x - j, y])
                    gemi_3.append([x - j, y])

            if yon == 2:
                for a in range(1, 3):
                    tablo[x][y + a] = "@"
                    gemiler.append([x, y + a])
                    gemi_3.append([x, y + a])



def gemi2():
    global gir
    global gemiler
    global gemi_2
    x = randint(0, gir - 1)
    y = randint(0, gir - 1)
    yon = randint(0,2)

    kontro1(x, y, 2)

    if kontro1(x, y, 2) == False:
        return gemi2()

    if kontro1(x, y, 2) == True:
        kontrol2(x, y, 3, yon)
        if kontrol2(x, y, 2, yon) == False:
            return gemi2()
        if kontrol2(x, y, 2, yon) == True:
            tablo[x][y] = "@"
            gemi_2.append([x, y])
            gemiler.append([x, y])

            if yon == 0:
                for i in range(1, 2):
                    tablo[x + i][y] = "@"
                    gemiler.append([x + i, y])
                    gemi_2.append([x + i, y])
            if yon == 1:
                for j in range(1, 2):
                    tablo[x - j][y] = "@"
                    gemiler.append([x - j, y])
                    gemi_2.append([x - j, y])

            if yon == 2:
                for a in range(1, 2):
                    tablo[x][y + a] = "@"
                    gemiler.append([x, y + a])
                    gemi_2.append([x, y + a])



def gemi1():
    global gir
    global gemiler
    global gemi_1
    x = randint(0, gir - 1)
    y = randint(0, gir - 1)

    if tablo[x][y] == "@":
        return gemi1()
    else:
        tablo[x][y] = "@"
        gemiler.append([x, y])
        gemi_1.append([x, y])

def hak1():
    global hak
    global gir
    hak = (gir*gir)//3
    print("-" * 45)
    print("Füze sayınız => ", hak)
    print("-" * 45)

def gemikontrol(x,y):
    global gemi_1
    global gemi_2
    global gemi_3
    global gemi_4
    global sayac1
    global sayac2
    global sayac3
    global gsayac
    global gsayac1
    global gsayac2
    global gsayac3

    if [x,y] in gemi_4:
        sayac1 = sayac1 + 1
    if [x,y] in gemi_3:
        sayac2 = sayac2 + 1
    if [x,y] in gemi_2:
        sayac3= sayac3 + 1

    if [x,y] == gemi_1[0]:
        gsayac += 1
        if gsayac == 1:
            return True

    if sayac1 == 4:
        gsayac1 += 1
        if gsayac1 == 1:
            return True

    if sayac2 == 3:
        gsayac2 += 1
        if gsayac2 == 1:
            return True

    if sayac3 == 2:
        gsayac3 += 1
        if gsayac3 == 1:
            return True
    return False

def puankontrol(genelsayac):
    global hak
    global gir

    print("\n" * 30)
    puan = hak - genelsayac

    print("Puanınız => ",puan)

    print("Oyunu tekrar oynamak istiyorsanız => 1")
    print("Çıkmak için => 2")

    sec = int(input("İstediğiniz işlemi secin => "))

    if sec == 1:
        print("\n" * 30)
        menu()
    else:
        exit(1)


def atis():
    global gir
    global gemiler
    global tablo
    global tahmin
    global hak
    global gatis
    global gatiskontrol


    if hak == 0:
        print("\n" * 30)
        print("Tüm füzeleriniz bitmiştir malesef başaramadınız")

        print("Oyunu tekrar oynamak istiyorsanız => 1")
        print("Çıkmak için => 2")

        sec = int(input("İstediğiniz işlemi secin => "))

        if sec == 1:
            print("\n" * 30)
            menu()
        else:
            exit(1)


    x = (int(input("\nTahmini satırınızı giriniz => ")) - 1)
    y = (int(input("Tahmini sütununuzu giriniz => ")) - 1)

    for i in range(0, len(tahmin)):
        if [x, y] == tahmin[i]:
            print("Girilen değerleri önceden girmiştiniz")
            return atis()
    tahmin.append([x, y])

    if x > (gir -1) or x < 0 or y > (gir - 1) or y < 0:
        print("Alan sınırları dışında değer girdiniz")
        return atis()
    else:
        if [x, y] in gemiler:
            print("\n" * 30)
            print("Tebrikler gemiyi vurdunuz")
            tablo[x][y] = "X"
            gatiskontrol += 1
            gatis += 1
            oyun_alani()
            if gatis == 10:
                print("\nTebrikler tüm gemileri batırdınız")
                puankontrol(gatiskontrol)
                menu()

            if gemikontrol(x, y) == True:
                print("\nTebrikler bir gemi batırdınız\n")

        else:
            print("\n" * 30)
            print("\nKaravana atış yaptınız")
            tablo[x][y] = "*"
            oyun_alani()
            gatiskontrol += 1
        hak = hak - 1
        print("-"*45)
        print("\nKalan füze sayısı => ", hak)

    return atis()

def atis2():
    global gir
    global gemiler
    global gtablo
    global tablo
    global tahmin
    global hak
    global atissayac
    global atiskontrol

    if hak == 0:
        print("\n" * 30)
        print("Yüm füzeleriniz bitmiştir malesef başaramadınız")

        print("Oyunu tekrar oynamak istiyorsanız => 1")
        print("Çıkmak için => 2")

        sec = int(input("İstediğiniz işlemi secin => "))

        if sec == 1:
            print("\n"*30)
            menu()
        else:
            exit(1)


    x = (int(input("\nTahmini satırınızı giriniz => ")) - 1)
    y = (int(input("Tahmini sütununuzu giriniz => ")) - 1)

    for i in range(0, len(tahmin)):
        if [x, y] == tahmin[i]:
            print("Girilen değerleri önceden girmiştiniz")
            return atis2()
    tahmin.append([x, y])

    if x > (gir - 1) or x < 0 or y > (gir - 1) or y < 0:
        print("Alan sınırları dışında değer girdiniz")
        return atis2()
    else:
        if [x, y] in gemiler:
            print("\n" * 30)
            print("Tebrikler gemiyi vurdunuz")
            gtablo[x][y] = "X"
            atiskontrol += 1
            atissayac += 1
            if atissayac == 10:
                print("\nTebrikler tüm gemileri batırdınız\n")
                puankontrol(atiskontrol)
                menu()

            if gemikontrol(x, y) == True:
                print("\nTebrikler bir gemi batırdınız")
            G_oyun_alan()
        else:
            print("\n" * 30)
            print("\nKaravana atış yaptınız")
            gtablo[x][y] = "*"
            G_oyun_alan()
            atiskontrol += 1
        hak = hak - 1
        print("-" * 45)
        print("\nKalan füze sayısı => ", hak)

    return atis2()

def acikmod():
    oyun_alani1()
    hak1()
    gemi4()
    gemi3()
    gemi2()
    gemi1()
    oyun_alani()
    atis()

def oyucumod():
    oyun_alani1()
    oyunalani2()
    hak1()
    gemi4()
    gemi3()
    gemi2()
    gemi1()
    G_oyun_alan()
    atis2()


menu()