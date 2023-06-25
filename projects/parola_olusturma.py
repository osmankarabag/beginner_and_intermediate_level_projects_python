tukce_karakterler = "çşıİÖÜöüĞğ"
parola = input("bir parola giriniz")
for i in parola :
    if i in tukce_karakterler:
        print(i,end=",")
