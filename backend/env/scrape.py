import requests

URL = "https://www.shoprite.com/sm/pickup/rsid/193/"
page = requests.get(URL)

print(page.text)