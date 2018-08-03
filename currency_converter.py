import os
import sys
import time
import json
import requests
from builtins import input


def remove_last_line():
    print('\x1b[1A' +'\x1b[2K' + '\x1b[1A')

def refresh():
    os.system('cls' if os.name in "nt" else "clear")

bold = '\033[1m'
e_bold = '\033[0m'

def conversion(key,curr):
        while True:
            currency1 = input("\nEnter the code of the currency you want to convert from > ").upper()
            loop = True
            for c in curr:
                if currency1 == c:
                    loop = False
            if loop == False:
                break

        while True:
            currency2 = input("\nEnter the code of the currency you want to convert to > ").upper()
            loop = True
            for c in curr:
                if currency2 == c:
                    loop = False
            if loop == False:
                while True:
                    try:
                        amount = int(input("\nEnter the amount of {} you want to convert > ".format(bold+currency1+e_bold)))
                        if amount < 0:
                            continue
                        else:
                            break
                    except:
                        continue
                print("\nConverting {} {} to {} ...".format(bold + str(amount),currency1 + e_bold,bold+currency2 + e_bold))
                break

        url = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}".format(currency1,currency2,key))
        j = json.loads(url.text)
        converted = float(j["Realtime Currency Exchange Rate"]["5. Exchange Rate"])*amount
        print("\t\t\t      {} {} is {}{:.2f} {}.".format(bold + str(amount),currency1 + e_bold, bold , converted,currency2 + e_bold))


def main():
    while True:
        try:
            file = open("api_key.txt","r")
            key = file.read()
            file.close()
            if key == "":
                os.remove("api_key.txt")
                continue
            break
        except:
            file = open("api_key.txt","w")
            key = input("Enter your api-key > ")
            file.write(key)
            file.close()
            break

    file = open("currency_codes.txt","r",encoding="utf-8")
    curr = json.load(file)
    file.close()

    def menu():
        choice = input("\nEnter 1 to convert currencies\nEnter 2 to lookup currency codes\n> ")
        if choice == "1":
            remove_last_line()
            remove_last_line()
            remove_last_line()
            conversion(key,curr)
            main()
        if choice == "2":
            remove_last_line()
            refresh()
            for c in curr:
                print("Currency: {:45} Code: {:}".format(bold+curr[c]["name"]+e_bold,bold+c+e_bold))
            input("\nEnter anything to go back > ")
            refresh()
            main()
        else:

            return menu()

    menu()

if __name__ == "__main__":
    main()
