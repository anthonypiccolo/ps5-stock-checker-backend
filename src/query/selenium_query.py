from selenium import webdriver
import chromedriver_binary

def stock_check(url, text_string=None, div_id=None, div_class=None):
    """ use headless browser"""

    #pip install selenium==2.53.0 
    #pip install chromedriver-binary==2.37.0
    #match_reponse = request_with_selenium(url="https://www.xxxxxxx.com.au/p/irobot-roomba-6-6-robot-vacuum-cleaner-r6-6/63387858", div_class="AddCart" ).text
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size={}x{}'.format(1280, 1024))

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    
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
    # driver.quit()
    return match
