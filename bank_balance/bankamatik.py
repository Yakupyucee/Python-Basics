YakupHesap ={
    'ad' : 'Yakup Yüce',
    'hesapNo' : '11111',
    'bakiye' : 3000,
    'ekHesap' : 2000,
}

AhmetHesap ={
    'ad' : 'Ahmet Yüce',
    'hesapNo' : '22222',
    'bakiye' : 2000,
    'ekHesap' : 1000,
}

def paraCek(hesap, miktar = 0) :
    if miktar <= hesap['bakiye']:
        hesap['bakiye'] -= miktar 
        print(f"{miktar} tl bakiyenizden çekildi. Kalan {hesap['bakiye']} tl")
    elif miktar <= hesap['bakiye'] + hesap['ekHesap']:
        if input("Ek hesaptan para transferi gerçeleşecektir. Kabul etkmek için E'ye basınız. Kabul etmemek için herhangi bir tuşa basınız: ") == 'E':
            hesap['ekHesap'] -=  miktar - hesap['bakiye']
            hesap['bakiye'] = 0
            print(f"{miktar} tl bakiyenizden çekildi. Kalan bakiyeniz {hesap['bakiye']} tl. Kalan ek hesap bakiyeniz {hesap['ekHesap']} tl") 
        else :
            print(f"Herhangi bir para çekme işlemi gerçekleşmedi. Kalan bakiyeniz {hesap['bakiye']} tl. Kalan ek hesap bakiyeniz {hesap['ekHesap']} tl")
    else :
        print(f"Bakiye yetersiz! Maksimum çekilebilecek tutar {hesap['bakiye'] + hesap['ekHesap']} tl.")


hesapNo = input("Lütfen hesap No giriniz : ")

if hesapNo == YakupHesap['hesapNo']:
    print(f"Merhaba {YakupHesap['ad']}")
    miktar = int(input("Çekilecek miktarı girin : "))
    paraCek(YakupHesap, miktar)

elif hesapNo == AhmetHesap['hesapNo']:
    print(f"Merhaba {AhmetHesap['ad']}")
    miktar = int(input("Çekilecek miktarı girin : "))
    paraCek(AhmetHesap, miktar)

else:
    print("Hesap No bulunamadı.")