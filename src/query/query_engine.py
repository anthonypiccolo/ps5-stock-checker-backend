import requests
from bs4 import BeautifulSoup



def stock_check(url, text_string, div_id=None, div_class=None):
    """  This function will conduct the scrape on a page
    look for: 
    - url
    - div id or div class or both
    - text
    """


    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Referer': 'https://www.ozbargain.com.au/'
        }
    
    if div_id == None and div_class == None:
        raise Exception("no divid or classid specified") 
    
    res = requests.get(url, verify=True, headers=headers, timeout=60)
    soup = BeautifulSoup(res.text, "html.parser")
    #output_txt(str(soup))
    if div_id != None:
        match = soup.find("div", {"id": f"{div_id}"})
    elif div_class != None:
        match = soup.find("div", {"class": f"{div_class}"})
    return match
    