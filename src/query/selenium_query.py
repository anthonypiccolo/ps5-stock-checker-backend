from os import curdir
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
#import undetected_chromedriver.v2 as uc
#from seleniumwire.undetected_chromedriver.v2 import Chrome, ChromeOptions
#import undetected_chromedriver.v2 as uc
# from chromedriver_py import binary_path
# import chromedriver_binary
import time
import pathlib
import math, random
import logging
import requests
import os 


# def random_time(start=0,end=500):
#     """ return a random number so we can look more organic for requests """
#     rand_number_ms = random.randrange(start,end)
#     rand_number_secs = rand_number_ms/100
#     return rand_number_secs

# Below is if we want to use seleniumwire and leverage a proxy service

PROXY_CREDS = os.environ.get('PROXY_CREDS')

options = {
     'proxy': {
         'http': f'http://rqscrod5:goh7S9clIpGFqAQX@52.22.195.164:31112', 
         'https': f'https://rqscrod5:goh7S9clIpGFqAQX@52.22.195.164:31112',
         'no_proxy': 'localhost,127.0.0.1' # excludes
     }
}

def set_chrome_settings():
    """ set up the chrome settings """
    #interesting thread here https://intoli.com/blog/making-chrome-headless-undetectable/
    chrome_options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1200")

    return chrome_options

def notify(text_content):
    url = 'https://discord.com/api/webhooks/898508639319523328/Yrk-07ixQ09MW5gyAC0FFqxaXuG2l2lvn3wCMeMvCuYOP3GSNWht0MgAv401ggsmPoyx'
    myobj = {"content": f"{text_content}"}
    requests.post(url, data = myobj)


def stock_check(url, text_string=None, div_id=None, div_class=None, store=None):
    """ use headless browser"""

    #pip install selenium==2.53.0 
    #pip install chromedriver-binary==2.37.0
    #match_reponse = request_with_selenium(url="https://www.xxxxxxx.com.au/p/irobot-roomba-6-6-robot-vacuum-cleaner-r6-6/63387858", div_class="AddCart" ).text
    
    # chrome_options = webdriver.ChromeOptions()
    print(f"looking at website {url}...")
    #driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",chrome_options=set_chrome_settings()) #seleniumwire_options=options)
    driver = webdriver.Chrome(chrome_options=set_chrome_settings(), seleniumwire_options=options)
    driver.get(url)
    logging.info(f"store: {store}: {driver.page_source[0:75]}") #log out top 75 chars of page
    notify(f"store: {store}: {driver.page_source[0:75]}")
    match = None
    if div_id != None:
        try:
            match = driver.find_element_by_id(div_id).text
        except:
            match = None
    elif div_class != None:
        try:
            match = driver.find_element_by_class_name(div_class).text
        except:
            match = None
    
    print(f"finished with matches? {match != None}")
    logging.info(f"finished with matches? {match != None}")
    time.sleep(1)
    driver.quit()
    return match


#stock_check("https://whatismyip.com")
