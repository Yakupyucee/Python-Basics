import requests
from bs4 import BeautifulSoup

url = "https://www.carvak.com/tr/satilik-arac?page="
headers ={'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

class Car:
    def __init__(self, brand = 'noName', series  = 'noName', model  = 'noName', year="noName", km = "noName", gear = "noName", price  = "noName"):
        self.brand = brand
        self.series = series
        self.model = model
        self.year = year
        self.km = km
        self.gear = gear
        self.price = price
    
    def getCar(self):
        print(f"""
    Brand : {self.brand}
    Model : {self.model}   
    Year : {self.year}
    Km : {self.km}
    Series : {self.series}
    Gear : {self.gear}
    Price : {self.price}
              """)


cars = []


def getCarsInfo(url):

    html = requests.get(url,headers = headers).content
    soup = BeautifulSoup(html,"html.parser")

    list = soup.find_all("div", {"class" : "col-sm-6"})

    for item in list:
        car = Car()
        title = item.find("h3", {"class" : "title"}).text
        car.brand, car.model = title.split(" • ")
        subtitle = item.find("p", {"class": "subtitle"}).text
        car.year, car.km, car.series, car.gear = subtitle.split(" • ")
        price = item.find("span", {"class": "price"}).text
        car.price = price.strip()
        cars.append(car)

n = 0
n1 = 1
while True:
    try:
        getCarsInfo(url = url + str(n))

    except:
        print("işlem bitti")
        break
        
    n += 1


for car in cars:
    print(f"{n1}-)")
    car.getCar()
    n1 += 1