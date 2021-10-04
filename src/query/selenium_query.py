from os import curdir
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
# from chromedriver_py import binary_path
# import chromedriver_binary
import time
import pathlib
import math, random
import logging

# def random_time(start=0,end=500):
#     """ return a random number so we can look more organic for requests """
#     rand_number_ms = random.randrange(start,end)
#     rand_number_secs = rand_number_ms/100
#     return rand_number_secs

options = {
    'proxy': {
        'http': 'http://username:password@host:port', 
        'https': 'https://username:password@host:port',
        'no_proxy': 'localhost,127.0.0.1' # excludes
    }
}

def set_chrome_settings():
    """ set up the chrome settings """
    #interesting thread here https://intoli.com/blog/making-chrome-headless-undetectable/
    chrome_options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1200")
    
    return chrome_options


def stock_check(url, text_string=None, div_id=None, div_class=None, store=None):
    """ use headless browser"""

    #pip install selenium==2.53.0 
    #pip install chromedriver-binary==2.37.0
    #match_reponse = request_with_selenium(url="https://www.xxxxxxx.com.au/p/irobot-roomba-6-6-robot-vacuum-cleaner-r6-6/63387858", div_class="AddCart" ).text
    
    # chrome_options = webdriver.ChromeOptions()
    print(f"looking at website {url}...")
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",chrome_options=set_chrome_settings(), seleniumwire_options=options)
    driver.get(url)
    logging.info(f"store: {store}: {driver.page_source[75]}") #log out top 75 chars of page
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


# stock_check('https://www.google.com')
