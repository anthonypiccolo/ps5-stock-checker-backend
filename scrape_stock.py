import requests
import time
from datetime import datetime 
from bs4 import BeautifulSoup

headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Referer': 'https://www.ozbargain.com.au/'
        }

def stock_check(url, text_string, div_id=None, div_class=None):
    """  This function will conduct the scrap on a page
    look for: 
    - url
    - div id or div class or both
    - text
    """
    
    if div_id == None and div_class == None:
        raise Exception("no divid or classid specified") 
    
    res = requests.get(url, verify=False, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    #output_txt(str(soup))
    if div_id != None:
        match = soup.find("div", {"id": f"{div_id}"})
    elif div_class != None:
        match = soup.find("div", {"class": f"{div_class}"})
    return match
    
def amazon_digital_stock():
    """ Xbox in stock????"""
    amazon_url = "https://www.amazon.com.au/Microsoft-RRT-00021-Xbox-Series-Console/dp/B08HLW5TDS"
    amazon_text_string = "In stock"
    amazon_div_id = "availability"
    ##return stock_check(url=amazon_url, text_string=amazon_text_string, div_id=amazon_div_id)
    if stock_check(url=amazon_url, text_string=amazon_text_string, div_id=amazon_div_id):
        return True
    else:
        return False

def target_stock():
    """Is PS5 in stock at Target"""
    target_url = "https://www.target.com.au/p/playstation-reg-5-dualsense-wireless-controller-white/64226194"
    target_text_string = "Add to basket"
    target_div_class = "AddCart"
    if stock_check(url=target_url, text_string=target_text_string, div_class=target_div_class):
        return True
    else:
        return False

##def bigw_stock():
##    """Big W PS5 stock"""
##    bigw_url = 
##    bigw_text_string = 
##    bigw_div_class = 
##    if stock_check(url=bigw_url, text_string=bigw_text_string, div_class=bigw_div_class):
##        return True
##    else:
##        return False

##def output_txt(input_text):
##    with open ("myfile.txt",'w') as myfile:
##        myfile.write(input_text)

#stock = amazon_digital_stock()
# target = target_stock()
#print(stock)
# print(target)

print(target_stock() )