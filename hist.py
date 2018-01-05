#!/usr/bin/env python
#
# Downloads all the crypto datas for quant analysis from cryptocompare
#
import requests, json, time, sys

class Ohmu:

    def download(self, coin):
        coin = coin.replace("\"", "")
        coin = coin.replace("\n", "")
        url = "https://min-api.cryptocompare.com/data/histoday?fsym=" + coin + "&tsym=USD&limit=20000&aggregate=1&toTs=1515132816&e=CCCAGG"
        r = requests.get(url)
        parsedJSON = json.loads(r.text)

        # Create and open coinFile
        fopen = open(coin, "a")
        fopen.write(str(parsedJSON))
        print(coin + " written.")
        fopen.close()

        return 