import random
kelimeler = ["bilgisayar", "televizyon", "gazete", "sinema",
          "felsefe", "matematik", "patates", "araba",
          "tarih", "tren", "harita", "sanat",
          "deney", "bilim", "edebiyat", "kamera",
          "elma", "deniz", "buzdolabı", "piyano",
          "keman", "gitar", "kelebek", "radyo",
          "sandalye", "saat", "sarımsak", "manzara"]

kelime = kelimeler[random.randint(0,len(kelimeler)+1)].upper()

bosKelime = list("_"*len(kelime))
hata = 0

def adamCizme():
    if hata == 0:
        print("     ")
        print("              ")
        print("              ")
        print("            ")
        print("              ")
        print("            ")
        print("---------          ")

    if hata == 1:
        print("     ")
        print("    |          ")
        print("    |          ")
        print("    |        ")
        print("    |          ")
        print("    |        ")
        print("---------          ")


    if hata == 2:
        print("     __________")
        print("    |          |")
        print("    |          ")
        print("    |        ")
        print("    |          ")
        print("    |        ")
        print("---------          ")

    if hata == 3:
        print("     __________")
        print("    |          |")
        print("    |          0")
        print("    |        ")
        print("    |          ")
        print("    |        ")
        print("---------          ")

    if hata == 4:
        print("     __________")
        print("    |          |")
        print("    |          0")
        print("    |        //")
        print("    |          ")
        print("    |        ")
        print("---------          ")

    if hata == 5:
        print("     __________")
        print("    |          |")
        print("    |          0")
        print("    |        //|")
        print("    |          ")
        print("    |        ")
        print("---------          ")

    if hata == 6:
        print("     __________")
        print("    |          |")
        print("    |          0")
        print("    |        //|\\")
        print("    |          ")
        print("    |        ")
        print("---------          ")

    if hata == 7:
        print("     __________")
        print("    |          |")
        print("    |          0")
        print("    |        //|\\")
        print("    |          ")
        print("    |        ")
        print("---------          ")


    if hata == 7:
        print("     __________")
        print("    |          |")
        print("    |          0")
        print("    |        //|\\")
        print("    |          |")
        print("    |        ")
        print("---------          ")

    if hata == 8:
        print("     __________")
        print("    |          |")
        print("    |          0")
        print("    |        //|\\")
        print("    |          |")
        print("    |        // ")
        print("---------          ")

    if hata == 9:
        print("     __________")
        print("    |          |")
        print("    |          0")
        print("    |        //|\\")
        print("    |          |")
        print("    |        // \\")
        print("---------          ")
   
   


while True:
    girilenHarf = input("bir harf giriniz : ")
    girilenHarf = girilenHarf.upper()
    sayac = 0
   
    varMi = False
    for harf in kelime:
        sayac += 1
        if girilenHarf == harf:
            varMi = True
            bosKelime[sayac - 1] = harf
    if not varMi:
        hata += 1
    adamCizme()
    print(f"Kalan hata sayısı : {9 - hata}")
    for n in bosKelime : print(n, end=" ")

    print("\n")
    if not "_" in bosKelime:
        print("Oyun Bitti. Kazandınız!")
        print(f"Kelime : {kelime}")
        break

    if hata == 9:
        print("Oyun bitti. Kaybettiniz!")
        print(f"Kelime : {kelime}")
        break

