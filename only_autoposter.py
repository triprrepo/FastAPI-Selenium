# SCRAPPER IMPORTERS
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc
import pickle
from csv import DictReader
import time
from time import sleep
import os.path

#APP IMPORTS
import load_cookies

#API IMPORTS
from fastapi import FastAPI
from fastapi import FastAPI, Body, File, Form, UploadFile, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8005",
    "http://localhost:800",
    "https://localhost",
    "https://localhost:8000",
    "https://localhost:800",
    #actual url in production,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/autoposter")
def autoposter(cookies):

    # Set up Facebook groups to post, you must be a member of the group
    groups_links_list = [
        "https://www.facebook.com/groups/1494117617557521", \
        "https://www.facebook.com/groups/133422387092305", \
        "https://www.facebook.com/groups/viagem.jmjtur", \
        "https://www.facebook.com/groups/361530938056499/"  
    ]

    # Set up text content to post
    message = "Veja no Tripr centenas de excursões de diversas agências, saindo de SP em Fevereiro e Março! https://tripr.com.br"

    # Set up paths of images to post
    # images_list = ['C:/Users/OEM/Pictures/sample1.jpg','C:/Users/OEM/Pictures/sample2.jpg'] 
    images_list = [] 
    
    #setting up undectetable Chrome
    browser = load_cookies.adding_cookies_browser(cookies)
    "print(loaded)"

    # Get page
    print("getting to fb")
    browser.get("https://www.facebook.com")
    
    # Post on each group
    
    n = 1
    for group in groups_links_list:
        try:
            f"going to the {n} site"
            browser.get(group)
            time.sleep(3)
            browser.find_element(By.XPATH,'//span[text()="Write something..."]').click()
            print("photo cliked")
            time.sleep(2)
            #photo_element = browser.find_element(By.XPATH,'//input[@type="file" and @accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]')
            #photo_element.send_keys(photo)
            time.sleep(3)
            browser.find_element(By.XPATH,'//*[@class="_1mf _1mj"]').send_keys(message)
            time.sleep(10)
            post_button = browser.find_element(By.XPATH,'//div/span/span[text()="Post"]')
            post_button.click()
            print(f"posted on group {n}")
            time.sleep(10)
            n += 1
        except:
            print("group failed")
        
        # time.sleep(2)
        # try:
        #     browser.find_element(By.XPATH,'//*[@label="Start Discussion"]').click()
        #     post_box=browser.find_element(By.CSS_SELECTOR, "[name='xhpc_message_text']")
        # except:
        #     post_box=browser.find_element(By.CSS_SELECTOR, "[name='xhpc_message_text']")
        # post_box.send_keys(message)
        # time.sleep(1)
        # for photo in images_list:
        #     photo_element = browser.find_element(By.XPATH,'//input[@type="file"]')
        #     photo_element.send_keys(photo)
        #     time.sleep(1)
        # time.sleep(6)
        # post_button = browser.find_element(By.XPATH, "//*[@data-testid='react-composer-post-button']")
        # clickable = False
        # while not clickable:
        #     cursor = post_button.find_element(By.TAG_NAME, 'span').value_of_css_property("cursor")
        #     if cursor == "pointer":
        #         clickable = True
        #     break
        # post_button.click()
        # time.sleep(5)

    # Close driver
    browser.close()
    return {"posted?": f"posted in {len(groups_links_list)} groups"}

#getting cookies
# cookies = load_cookies.loading_cookies()
# #ruNning the function
# autoposter(cookies)

# if __name__ == "__main__":
#     print("loaded  autoposter")