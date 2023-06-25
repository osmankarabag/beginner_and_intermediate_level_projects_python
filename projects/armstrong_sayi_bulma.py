
#armstrong sayı bulma
def armstrong(fsayi):
    bs = len(fsayi)
    toplam=0
    for i in fsayi:
        toplam+=int(i)**bs
    if toplam == int(fsayi):
        return True
    else:
        return False
sayi = input("sayi giriniz:")
print(armstrong(sayi))