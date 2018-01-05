#!/usr/bin/env python
#
# Downloads all the crypto datas for quant analysis from cryptocompare
#
import requests, json, time, sys

class Ohmu:

    def download(self, coin):
        # Create and open coinFile
        fopen = open(coin, "a")
        
        coin = coin.replace("\"", "")
        coin = coin.replace("\n", "")
        url = "https://min-api.cryptocompare.com/data/histoday?fsym=" + coin + "&tsym=USD&limit=20000&aggregate=1&toTs=1507917600&e=CCCAGG"
        r = requests.get(url)
        parsedJSON = json.loads(r.text)
        
        data = parsedJSON["Data"]
    
        if data:
            # Remove the '[' from data
            data = str(data)
            data = data[1:-1] + ", "
            fopen.write(data)
            print("[" + str(timeFrom) + "] written.")
            self.download(coin)

        fopen.close()
        print(coin + " written.")
        return 