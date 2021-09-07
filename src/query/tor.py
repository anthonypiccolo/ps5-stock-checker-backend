
# not used

# import requests
# from bs4 import BeautifulSoup

# # from torpy.http.requests import tor_requests_session
# # from multiprocessing.pool import ThreadPool
# from fake_useragent import UserAgent
# from selenium import webdriver
# import chromedriver_binary

# # no matches found: torpy[requests]? use 
# # pip install 'torpy[requests]'
# # pip install beautifulsoup4
# # pip install requests
# # pip install fake-useragent
# #

# def request_with_tor(url=None, text_string=None, div_id=None, div_class=None):
#     """ use tor to request from a url """
    
#     headers = {
#         'Access-Control-Allow-Origin': '*',
#         'Access-Control-Allow-Methods': 'GET',
#         'Access-Control-Allow-Headers': 'Content-Type',
#         'Access-Control-Max-Age': '3600',
#         'Accept': 'application/json, text/javascript, */*; q=0.01',
#         'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'Referer': 'https://www.target.com.au/playstation-5',
#         'User_Agent': UserAgent().random
#         }
#     url = url
#     with tor_requests_session() as requests_session:  # returns requests.Session() object
       
#         # my_response = requests_session(my_links)
#         print(headers)
#         response = requests_session.get(url=url, verify=False, headers=headers, timeout=60)
#         print(response.status_code)
#     res = requests.get(url, verify=True, headers=headers, timeout=60)
#     print(res.status_code)

# # request_with_tor()

