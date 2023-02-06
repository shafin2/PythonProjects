import requests
from bs4 import BeautifulSoup

website=requests.get("https://ero.betfair.com/www/sports/exchange/readonly/v1/bymarket?_ak=nzIFcwyWhrlwYMrh&alt=json&currencyCode=USD&locale=en_GB&marketIds=1.206226401&rollupLimit=25&rollupModel=STAKE&types=MARKET_STATE,RUNNER_STATE,RUNNER_EXCHANGE_PRICES_BEST")

soup=BeautifulSoup(website.content,"html.parser")

print(soup.text)
# print(soup.prettify())