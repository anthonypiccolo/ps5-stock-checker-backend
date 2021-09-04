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


def stock_check(url, text_string, div_id=None, div_class=None):
    """  This function will conduct the scrap on a page
    look for: 
    - url
    - div id or div class or both
    - text
    """
    
    if div_id == None and div_class == None:
        raise Exception("no divid or classid specified") 
    
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
#     match = soup.find("div", {"class": f"{div_class}"})
    match = soup.find("div", {"class": f"{div_id}"})
    #badge = soup.find("div", {"class": "ProductBadges"})
# ?    if match.text includes text string then :
    return badge
    
 
def bigw_digital_stock():
    """ just big w digitical edition """
    bigw_url= bigw_digital
    bigw_text_string = "available now!"
    bigw_div_id
    
    my_response =  stock_check(url=bigw_url, text_string= bigw_text_string, div_id=bigw_div_id)
    if my_response = 'xyz':
        return true,
    else:
        return false

def amazon_digital_stock():
    """ just digital edition on amazon"""
    amazon_url = amazon_digital
    amazon_text_string = "In stock"
    amazong_div_id = "availability"
    return stock_check(url=amazon_url, text_string=amazon_text_string, div_id=amazong_div_id)
    
    
    
stock = stock_check(bigw_digital)
print(stock.find("https://www.bigw.com.au/medias/sys_master/root/h52/hab/29192821932062.png"))

now = datetime.now()

##if stock == "https://www.bigw.com.au/medias/sys_master/root/h52/hab/29192821932062.png"
##    print(str(now) + ": Still not in stock...")
##else:
##    print(str(now) + ": Now in stock!")


my_json = {
 "amazon_ps5_digital": amazon_digital_stock(),
 "amazon_ps5_disc": 
 
    
}
