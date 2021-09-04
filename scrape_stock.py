import requests
import time
import os
import constants as const
import json
from datetime import datetime 
from bs4 import BeautifulSoup
from google.cloud import storage

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
    
def amazon_digital():
    """ Xbox in stock????"""
    amazon_url = "https://www.amazon.com.au/PlayStation-5-Digital-Edition-Console/dp/B08HLWDMFQ"
    amazon_text_string = "In stock"
    amazon_div_id = "availability"
    ##return stock_check(url=amazon_url, text_string=amazon_text_string, div_id=amazon_div_id)
    if stock_check(url=amazon_url, text_string=amazon_text_string, div_id=amazon_div_id):
        return True
    else:
        return False
    
def amazon_disc():
    """ Xbox in stock????"""
    amazon_url = "https://www.amazon.com.au/PlayStation-5-Console/dp/B08HHV8945"
    amazon_text_string = "In stock"
    amazon_div_id = "availability"
    ##return stock_check(url=amazon_url, text_string=amazon_text_string, div_id=amazon_div_id)
    if stock_check(url=amazon_url, text_string=amazon_text_string, div_id=amazon_div_id):
        return True
    else:
        return False

def target_digital():
    """Is PS5 in stock at Target"""
    target_url = "https://www.target.com.au/p/playstation-reg-5-dualsense-wireless-controller-white/64226194"
    target_text_string = "Add to basket"
    target_div_class = "AddCart"
    if stock_check(url=target_url, text_string=target_text_string, div_class=target_div_class):
        return True
    else:
        return False
    
def target_disc():
    """Is PS5 in stock at Target"""
    target_url = "https://www.target.com.au/p/playstation-reg-5-dualsense-wireless-controller-white/64226194"
    target_text_string = "Add to basket"
    target_div_class = "AddCart"
    if stock_check(url=target_url, text_string=target_text_string, div_class=target_div_class):
        return True
    else:
        return False

def bigw_digital():
    """Big W PS5 stock"""
    bigw_url = "https://www.bigw.com.au/product/playstation-5-digital-edition-console/p/124626/"
    bigw_text_string = "blah"
    bigw_div_class = "ProductAddToCart"
    
    if stock_check(url=bigw_url, text_string=bigw_text_string, div_class=bigw_div_class):
        return True
    else:
        return False
    
def bigw_disc():
    """Big W PS5 stock"""
    bigw_url = "https://www.bigw.com.au/product/playstation-5-digital-edition-console/p/124626/"
    bigw_text_string = "blah"
    bigw_div_class = "ProductAddToCart"
    
    if stock_check(url=bigw_url, text_string=bigw_text_string, div_class=bigw_div_class):
        return True
    else:
        return False

##def output_txt(input_text):
##    with open ("myfile.txt",'w') as myfile:
##        myfile.write(input_text)

#print(f'{datetime.now()} - Target - {target_stock()}' )
#print(bigw_digital_stock() )

my_json = {
    "amazon": {
    "digital": f"{amazon_digital()}",
    "disc": f"{amazon_digital()}"
    },

    "target": {
    "digital": f"{target_digital()}",
    "disc": f"{target_disc()}"
    },
    
    "bigw": {
    "digital": f"{bigw_digital()}",
    "disc": f"{bigw_disc()}"
    }
}

print(json.dumps(my_json))

service_account_path = os.path.join("/Users/anthony.piccolo/dev/ps5-stock-checker-backend/ps5-stock-checker-325003-601f476a23ff.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path

client = storage.Client()
bucket = client.get_bucket(const.destination_gcs_bucket)
filename = 'stock_levels' + datetime.now().strftime("%Y%m%d")

# Push data to GCS
blob = bucket.blob(filename)
user_encode_data = json.dumps(my_json, indent=2).encode('utf-8')

print(user_encode_data)

blob.upload_from_string(
    json.dumps(user_encode_data).encode,
    content_type='application/json'
    )