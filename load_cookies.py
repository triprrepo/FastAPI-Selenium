from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
import pickle
from csv import DictReader
import time
from time import sleep
import os.path


### using regular browser (and not the undetected chromedriver)
#login 

# # Setup chrome options
# chrome_options = Options()

# # chrome_options.add_argument("--headless") # Ensure GUI is off
# chrome_options.add_argument("--no-sandbox")

# # Set path to chromedriver as per your configuration
# homedir = os.path.expanduser("~")
# print("loading chrome")
# webdriver_service = Service(r'./chrome2/stable/chromedriver')

# # Choose Chrome Browser
# #uc.TARGET_VERSION = 109
# browser = webdriver.Chrome(service= webdriver_service, options=chrome_options)
# print("browser opened")


####
####

# may need to setup something to disable notification: https://www.youtube.com/watch?v=rDBho83SUrw&list=WL&index=3&ab_channel=AutomationForMarketers

####
####

# Opening with Undetected_chromedriver

def loading_cookies():
    options = uc.ChromeOptions()
    options.headless = True
    options.add_argument( '--headless' )
    options.add_argument('--no-sandbox')     
    options.add_argument('--disable-dev-shm-usage')   
    options.add_argument("--disable-setuid-sandbox")
    browser = uc.Chrome(version_main=100, options = options)
    # browser = uc.Chrome(version_main=109)


    # Log in to Facebook in the browser
    print("loading fb page")
    browser.get("https://www.facebook.com")
    print("went to fb")

    # Loading Cookies
    print("I am loading the cookies file")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    print("loaded")


    ## command only to commit
    # # Adding the Facebook cookies to the new browser instance
    # n = 0
    # for cookie in cookies:
    #     cookie["domain"] = ".facebook.com"
    #     try:
    #         browser.add_cookie(cookie)
    #         print(f"added {n + 1} cookies")
    #         n += 1
    #     except Exception as e:
    #         print(e.message)

    # # Load Facebook's website using the cookies
    # browser.refresh()
    # # browser.get("https://www.facebook.com")
    # print("I am loading fb page and it should be logged!")
    # sleep(2)
    return cookies 


def adding_cookies_browser(cookies):
    # Adding the Facebook cookies to the new browser instance
    options = uc.ChromeOptions()
    # options.headless = True
    options.add_argument('--headless' )
    options.add_argument('--no-sandbox')     
    options.add_argument('--disable-dev-shm-usage')   
    options.add_argument("--disable-setuid-sandbox")
    browser = uc.Chrome(version_main=100, options = options)
    browser.get("https://www.facebook.com")
    n = 0
    for cookie in cookies:
        cookie["domain"] = ".facebook.com"
        try:
            browser.add_cookie(cookie)
            print(f"added {n + 1} cookies")
            n += 1
        except Exception as e:
            print(e)
    return browser


## Not to use as it doesn't work
# for cookie in cookies:
#     if cookie['domain'] in browser.current_url:
#         browser.add_cookie(cookie)
#     else:
#         print(f"Cookie with domain {cookie['domain']} not added. The current domain is {browser.current_url}")
        
if __name__ == "__main__":
    print("loaded  load cookies")