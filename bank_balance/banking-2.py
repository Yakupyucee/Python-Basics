class Account:
    def __init__(self,fname,lname,accountNumber,balance,creditBalance):
        self.fname = fname
        self.lname = lname
        self.acountNumber = accountNumber
        self.balance = balance
        self.creditBalance = creditBalance

    def greeting(self):
        print(f"Merhaba {self.fname} {self.lname}")
        miktar = int(input("Çekilecek miktarı girin : "))
        self.paraCek(miktar)


    def paraCek(self, miktar = 0) :
        if miktar <= self.balance:
            self.bakiyeParaCek(miktar)
        elif miktar <= self.balance + self.creditBalance:
            self.ekHesapParaCek(miktar)
        else :
            print(f"Bakiye yetersiz! Maksimum çekilebilecek tutar {self.balance + self.creditBalance} tl.")


    def bakiyeParaCek(self, miktar):
        self.balance -= miktar 
        print(f"{miktar} tl bakiyenizden çekildi. Kalan {self.balance} tl")


    def ekHesapParaCek (self,miktar):
        if input("Ek hesaptan para transferi gerçeleşecektir. Kabul etkmek için E'ye basınız. Kabul etmemek için herhangi bir tuşa basınız: ") == 'E':
                self.creditBalance -=  (miktar - self.balance)
                self.balance = 0
                print(f"{miktar} tl bakiyenizden çekildi. Kalan bakiyeniz {self.balance} tl. Kalan ek hesap bakiyeniz {self.creditBalance} tl") 
        else :
            print(f"Herhangi bir para çekme işlemi gerçekleşmedi. Kalan bakiyeniz {self.balance} tl. Kalan ek hesap bakiyeniz {self.creditBalance} tl")




p1 = Account('Yakup', 'Yüce', '111', 3000, 2000)
p2 = Account('Ahmet', 'Yüce', '222', 2000, 1000)
p3 = Account('Ayşe', 'Yüce', '333' , 3000, 1000)

accounts = [p1, p2, p3]


hesapNo = input("Lütfen hesap No giriniz : ")

for a in accounts:
    if hesapNo == a.acountNumber:
        a.greeting()
        break
    
