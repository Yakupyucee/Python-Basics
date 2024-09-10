import requests
import json

api_key = ''#write exchangerate api
api_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/'

def exchange(firstCurrency, secondCurrency, amount):
    result = requests.get(api_url + firstCurrency)
    result_json = json.loads(result.text)

    print(f'1 {firstCurrency} = {result_json["conversion_rates"][secondCurrency]} {secondCurrency}')
    print(f'{amount} {firstCurrency} = {result_json["conversion_rates"][secondCurrency] * amount} {secondCurrency}')


while True :

    firstCurrency = (input('Currency to be converted : ')).upper()
    secondCurrency = (input('Desired currency : ')).upper()
    amount = int(input('Amount :'))
    while True:
        exchange(firstCurrency=firstCurrency , secondCurrency= secondCurrency , amount=amount)

    if (input('To continue Y/N : ')).upper() == 'N':
        break
