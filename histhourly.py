#!/usr/bin/env python
#
# Downloads all the crypto datas for quant analysis from cryptocompare
#
import requests, json, time

class Ohmu:

    def download(self, coin, timeFrom, fname, frq):
        url = "https://min-api.cryptocompare.com/data/" + frq + "?fsym=" + coin + "&tsym=USD&limit=20000&aggregate=1&toTs=" + str(timeFrom) + "&e=CCCAGG"
        r = requests.get(url)
        parsedJSON = json.loads(r.text)
        try:
            timeFrom = parsedJSON["TimeFrom"]

        except:
            text = r.text
            print(text)
            error = open("error.log", 'a')
            error.write(text)
            error.close()
            print("Error log written to.")

        data = parsedJSON["Data"]
    
        if data:
            # Remove the '[' from data
            data = str(data)
            data = data[1:-1] + ", "
            fname.write(data)
            print("[" + str(timeFrom) + "] written.")
            self.download(coin, timeFrom, fname, frq)

        return timeFrom