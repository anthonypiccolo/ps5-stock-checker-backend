from google.cloud import storage
import time
import os
import constants as const
import json
from datetime import datetime 
from src.query import selenium_query as query_engine
# from src.query import query_engine
#rom src.messaging import messaging_service



# def stock_check(url, text_string, div_id=None, div_class=None):
#     """  This function will conduct the scrape on a page
#     look for: 
#     - url
#     - div id or div class or both
#     - text
#     """

#     headers = {
#         'Access-Control-Allow-Origin': '*',
#         'Access-Control-Allow-Methods': 'GET',
#         'Access-Control-Allow-Headers': 'Content-Type',
#         'Access-Control-Max-Age': '3600',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
#         'Referer': 'https://www.ozbargain.com.au/'
#         }
    
#     if div_id == None and div_class == None:
#         raise Exception("no divid or classid specified") 
    
#     res = requests.get(url, verify=True, headers=headers, timeout=60)
#     soup = BeautifulSoup(res.text, "html.parser")
#     #output_txt(str(soup))
#     if div_id != None:
#         match = soup.find("div", {"id": f"{div_id}"})
#     elif div_class != None:
#         match = soup.find("div", {"class": f"{div_class}"})
#     return match
    
def amazon_digital():
    """ Is PS5 digital edition in stock at Amazon """
    print("amazon digital")
    amazon_url = "https://www.amazon.com.au/PlayStation-5-Digital-Edition-Console/dp/B08HLWDMFQ"
    amazon_text_string = "In stock"
    amazon_div_id = "availability"
    store = "amazon"
    ##return stock_check(url=amazon_url, text_string=amazon_text_string, div_id=amazon_div_id)
    if query_engine.stock_check(url=amazon_url, text_string=amazon_text_string, div_id=amazon_div_id, store=store):
        return amazon_url
    else:
        return ""
    
def amazon_disc():
    """ Is PS5  disc edition in stock at Amazon """
    print("amazon disc")
    amazon_url = "https://www.amazon.com.au/PlayStation-5-Console/dp/B08HHV8945"
    amazon_text_string = "In stock"
    amazon_div_id = "availability"
    store = "amazon"
    ##return stock_check(url=amazon_url, text_string=amazon_text_string, div_id=amazon_div_id)
    if query_engine.stock_check(url=amazon_url, text_string=amazon_text_string, div_id=amazon_div_id, store=store):
        return amazon_url
    else:
        return ""

def target_digital():
    """Is PS5 digital edition in stock at Target"""
    target_url = "https://www.target.com.au/p/playstation-reg-5-console-digital-edition/64226170"
    target_text_string = "Add to basket"
    target_div_class = "AddCart"
    store = "target"
    if query_engine.stock_check(url=target_url, text_string=target_text_string, div_class=target_div_class, store=store):
        return target_url
    else:
        return ""
    
def target_disc():
    """Is PS5  disc edition in stock at Target"""
    target_url = "https://www.target.com.au/p/playstation-reg-5-console/64226187"
    target_text_string = "Add to basket"
    target_div_class = "AddCart"
    store = "target"
    if query_engine.stock_check(url=target_url, text_string=target_text_string, div_class=target_div_class, store=store):
        return target_url
    else:
        return ""

def bigw_digital():
    """Big W PS5 digital edition stock"""
    bigw_url = "https://www.bigw.com.au/product/playstation-5-digital-edition-console/p/124626/"
    bigw_text_string = "blah"
    bigw_div_class = "ProductAddToCart"
    store = "bigw"
    if query_engine.stock_check(url=bigw_url, text_string=bigw_text_string, div_class=bigw_div_class, store=store):
        return bigw_url
    else:
        return ""
    
def bigw_disc():
    """Big W PS5 disc edition stock"""
    bigw_url = "https://www.bigw.com.au/product/playstation-5-digital-edition-console/p/124626/"
    bigw_text_string = "blah"
    bigw_div_class = "ProductAddToCart"
    store = "bigw"
    if query_engine.stock_check(url=bigw_url, text_string=bigw_text_string, div_class=bigw_div_class, store=store):
        return bigw_url
    else:
        return ""


def build_json():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    my_json = {
        "timestamp": timestamp,
        
        "amazon": {
        "digital": f"{amazon_digital()}",
        "disc": f"{amazon_disc()}"
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
    return my_json
    # print(json.dumps(my_json))

#service_account_path = os.path.join("")
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path

def write_to_bucket(input_bucket, dict_to_write, filename_prefix=None):
    filename = f"{filename_prefix}ps5_stock"
    client = storage.Client()
    bucket = client.get_bucket(input_bucket)

    # Push data to GCS
    blob = bucket.blob(filename)
    user_encode_data = json.dumps(dict_to_write)#.encode('utf-8')

    print(user_encode_data)

    blob.upload_from_string(
    user_encode_data,
    content_type='application/json'
    )

def historical_write_to_bucket(input_json):
    bucket_historical = const.destination_gcs_bucket_historical
    my_prefix = f'{datetime.now().strftime("%Y%m%d%H%M%S")}_'
    write_to_bucket(input_bucket=bucket_historical, dict_to_write=input_json, filename_prefix=my_prefix)

def now_write_to_bucket(input_json):
    bucket_now = const.destination_gcs_bucket_now
    write_to_bucket(input_bucket=bucket_now, dict_to_write=input_json)

def ps5_stock_check(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    try: 
        # we do nothing with the request param. It's just a way to make cloud functions not fall over
        print("looking for ps5s...")
        my_json = build_json()
        # print(my_json)
        historical_write_to_bucket(my_json)
        now_write_to_bucket(my_json)
        print("bucket writes completed")

        # print("telling everyone about it...")
        # messaging_service.message_services(my_json)
        return 'ok', 200
    except Exception as e:
        print(e)
        return 'error', 500

    

ps5_stock_check('Looking for ps5s...')
