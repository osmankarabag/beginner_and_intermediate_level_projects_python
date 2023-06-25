def karsilik_bul(*args, **kwargs):
    for sozcuk in args:
        if sozcuk in kwargs:
            print("{} = {}".format(sozcuk, kwargs[sozcuk]))
        else:
            print("{} kelimesi sozlukte yok!".format(sozcuk))
sozcuk={"kitap": "book",
        "bilgisayar" : "computer",
        "programlama" : "programing"}
karsilik_bul("kitap", "bilgisayar", "programlama", "fonksiyon", **sozcuk)