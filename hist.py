#!/usr/bin/env python
#
# Downloads all the crypto datas for quant analysis from cryptocompare
#
import requests, json, time, sys

class Ohmu:

    # If timeFrom is supplied, then this isn't the first time this function has ran.
    # If timeFrom = None, then skip the appending ", " part
    def download(self, coin, timeFrom=None):
        # Create and open coinFile
        fopen = open(coin, "a")
        
        coin = coin.replace("\"", "")
        coin = coin.replace("\n", "")

        if (timeFrom):
            url = "https://min-api.cryptocompare.com/data/histoday?fsym=" + coin + "&tsym=USD&limit=20000&aggregate=1&toTs=" + str(timeFrom) + "&e=CCCAGG"
        else:
            url = "https://min-api.cryptocompare.com/data/histoday?fsym=" + coin + "&tsym=USD&limit=20000&aggregate=1&toTs=1515197448&e=CCCAGG"
        r = requests.get(url)
        parsedJSON = json.loads(r.text)
        timeFrom = parsedJSON["TimeFrom"]
        data = parsedJSON["Data"]
    
        if (data):
            # Remove the '[' from data
            data = str(data)
            data = data[1:-1] + ", "
            fopen.write(data)
            print("[" + str(timeFrom) + "] written.")
            self.download(coin, timeFrom)

        fopen.close()
        print(coin + " complete.")
        return 