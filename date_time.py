import datetime
tarih_str = input("lütfen tarihi 'YYYY-MM-DD' formatında girin: ")

tarih = datetime.datetime.strptime(tarih_str, "%Y-%m-%d").date()

bugun = datetime.date.today()

fark = bugun - tarih

gun_farki = fark.days

if gun_farki >= 0 and  gun_farki <= 365 : 
    print("Arabanız 1. bakımdadır")

elif gun_farki > 365 and gun_farki <= 2 * 365 : 
    print("Arabanız 2. bakımdadır")

elif gun_farki > 2 * 365 and gun_farki <= 3 * 365 : 
    print("Arabanız 3. bakımdadır")

elif gun_farki > 3 * 365 :
    print("Arabanız 3. bakım üstündedir")
else :
    print ("Yanlış bir tarih girdiniz lütfen tekrar kontrol ediniz.")
