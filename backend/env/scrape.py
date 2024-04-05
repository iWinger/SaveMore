from selenium import webdriver
import re
from bs4 import BeautifulSoup


class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
  
#Use selenium to dynamically load in the page because the site uses JavaScript
driver = webdriver.Firefox()
item = input("Enter item: ")
# This is for the shoprite of a specific location... in order to find other shoprites, get other rsids
# We need to get different stores to compare the prices between the product prices
driver.get("https://www.shoprite.com/sm/pickup/rsid/193/results?q=" + item) 
driver.get()
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Regular expression used to find given names
regex = re.compile('ProductCardWrapper')
regex2 = re.compile('cardCharges')
regex3 = re.compile('ProductNameTestId')
regex4 = re.compile('productCardPricing')


# Iterate through all the products on the page, and get the product and price
products = []

for result in soup.find_all("div", {"data-testid" : regex}):
    card = result.find('div', {"data-testid" : regex2})
    name = card.find('div', {"data-testid" : regex3})
    #print(name.get_text())
    price = card.find('div', {"data-testid" : regex4})
    #print(price.get_text())

    products.append(Item(name.get_text(), price.get_text()))

# Sort the arr
products.sort(key=lambda item:item.price)
for product in products:
    print(product.name)
    print(product.price)

# Need to attach size to the item depending on the thing... oz,fl oz, etc..
