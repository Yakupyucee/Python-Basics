import random

rastgeleSayi = random.randint(1,1000)

hak = int(input("Kaç hakta bileceksiniz : "))
kalanPuan = 100
puan = 100 // hak

while True:
    tahmin = int(input("Tahmininizi giriniz : "))
    if tahmin == rastgeleSayi:
        print(f"Tebrikler {rastgeleSayi} sayısını buldunuz. Puanınız : {kalanPuan}")
        break
    elif tahmin < rastgeleSayi:
        
        print("Tahmininiz yükseltin.")
    elif tahmin > rastgeleSayi:
        print("Tahmininizi düşürün.")
    kalanPuan -= puan
    if kalanPuan <= 0:
        print(f"Kaybettiniz! Aranan sayı : {rastgeleSayi}")
        break
    print(f"Puan : {kalanPuan}")
   
