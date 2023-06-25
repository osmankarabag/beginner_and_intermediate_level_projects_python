import random
boyut = int(input("boyut giriniz"))
yon = int(input("yon giriniz"))
kontrol_satır = [0]* boyut
#print(kontrol_satır)
kontrol_sutun = [0]* boyut
#print(kontrol_sutun)
isikli_alan = boyut
secilen_kordinatlar = []
hamle = 0
while (isikli_alan != 0) :
    satir=random.randint(1,boyut)
    sutun=random.randint(1,boyut)
    print("üretilen kordinat-> {} , {} ".format(satir,sutun),end= " ")
    if((satir,sutun) in secilen_kordinatlar):
        print("daha önce üretildi")
    else:
        secilen_kordinatlar.append((satir,sutun))
        if yon == 1 :
            kontrol_satır[satir-1]=1
            isikli_alan=kontrol_satır.count(0)
        else:
            kontrol_sutun[sutun - 1] = 1
            isikli_alan = kontrol_sutun.count(0)
        hamle=hamle+1
        print("isklı alan-> {} birim". format(isikli_alan))

print("ışık tamamen kesild. hamle sayısı :{},Perde oluşma yüzdesi: {}".format(hamle,hamle/(boyut**2)))
