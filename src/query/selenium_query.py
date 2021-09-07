from selenium import webdriver
from chromedriver_py import binary_path
import time

def stock_check(url, text_string=None, div_id=None, div_class=None):
    """ use headless browser"""

    #pip install selenium==2.53.0 
    #pip install chromedriver-binary==2.37.0
    #match_reponse = request_with_selenium(url="https://www.xxxxxxx.com.au/p/irobot-roomba-6-6-robot-vacuum-cleaner-r6-6/63387858", div_class="AddCart" ).text
    
    # chrome_options = webdriver.ChromeOptions()
    
    # chrome_options.add_argument('--window-size={}x{}'.format(1280, 1024))
    # chrome_options.add_argument(f'--executable_path={binary_path}')

    
    driver = webdriver.Chrome(executable_path=binary_path)
    # driver = webdriver.Chrome(chrome_options=chrome_options)
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
    
    time.sleep(5)
    driver.quit()
    return match


stock_check('https://google.com')