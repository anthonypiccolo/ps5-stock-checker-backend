import requests
import time
from datetime import datetime 
from bs4 import BeautifulSoup

bigw_digital = "https://www.bigw.com.au/product/playstation-5-digital-edition-console/p/124626/"
bigw_disc = "https://www.bigw.com.au/product/playstation-5-console/p/124625/"
target = "https://www.target.com.au/playstation-5"
amazon_digital = "https://www.amazon.com.au/PlayStation-5-Digital-Edition-Console/dp/B08HLWDMFQ
amazon_disc = "https://www.amazon.com.au/PlayStation-5-Console/dp/B08HHV8945"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def stock_check(bigw_digital):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    badge = soup.find("div", {"class": "ProductBadges"})
    return badge
    
stock = stock_check(bigw_digital)
print(stock.find("https://www.bigw.com.au/medias/sys_master/root/h52/hab/29192821932062.png"))

now = datetime.now()

##if stock == "https://www.bigw.com.au/medias/sys_master/root/h52/hab/29192821932062.png"
##    print(str(now) + ": Still not in stock...")
##else:
##    print(str(now) + ": Now in stock!")