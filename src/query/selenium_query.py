from os import curdir
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from chromedriver_py import binary_path
# import chromedriver_binary
import time
import pathlib
import math, random

# def random_time(start=0,end=500):
#     """ return a random number so we can look more organic for requests """
#     rand_number_ms = random.randrange(start,end)
#     rand_number_secs = rand_number_ms/100
#     return rand_number_secs


def set_chrome_settings():
    """ set up the chrome settings """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1200")
    
    return chrome_options

def stock_check(url, text_string=None, div_id=None, div_class=None):
    """ use headless browser"""

    #pip install selenium==2.53.0 
    #pip install chromedriver-binary==2.37.0
    #match_reponse = request_with_selenium(url="https://www.xxxxxxx.com.au/p/irobot-roomba-6-6-robot-vacuum-cleaner-r6-6/63387858", div_class="AddCart" ).text
    
    # chrome_options = webdriver.ChromeOptions()
    print(f"looking at website {url}...")
    driver = webdriver.Chrome(chrome_options=set_chrome_settings())
    driver.get(url)
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
    time.sleep(5)
    driver.quit()
    return match


# stock_check('https://www.google.com')
