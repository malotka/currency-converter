import json
import urllib.request

if __name__ == '__main__':
    print('przykladowe kody walut: usd, aud, chf, cad, jpy')

    amount = input('how many pln u have? ')
    amount = int(amount)

    currency = input('To what currency are you willing to exchange? ')

    url = 'http://api.nbp.pl/api/exchangerates/rates/c/{}/today/?format=json'.format(currency)

    with urllib.request.urlopen(url) as jsonfile:
        data = jsonfile.read().decode('utf-8')

    data_dict = json.loads(data)

    bid = data_dict['rates'][0]['bid']
    ask = data_dict['rates'][0]['ask']

    print('waluta: ', data_dict['currency'])
    print('kupno: ', bid, '\nsprzedaz: ', ask)

    print(amount, ' PLN will be ', (amount/ask), data_dict['code'])

