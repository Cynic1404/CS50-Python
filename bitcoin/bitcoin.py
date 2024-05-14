import sys
import requests


if len(sys.argv)<2:
    sys.exit("Missing command-line argument")
elif not sys.argv[1].replace(".", "").isdigit():
    sys.exit("Command-line argument is not a number")
else:
    try:
        number=int(sys.argv[1])
    except:
        number = float(sys.argv[1])


price = float(requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()['bpi']['USD']['rate'].replace(",",""))*number

print(f"${float(price):,.4f}")
