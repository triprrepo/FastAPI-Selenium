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
import undetected_chromedriver as uc
from fastapi import FastAPI, Body, File, Form, UploadFile, Response
from fastapi.middleware.cors import CORSMiddleware


def createDriver():
    options = uc.ChromeOptions()
    options.headless = True
    options.add_argument( '--headless' )
    browser = uc.Chrome(version_main=100, options = options)
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    
    # prefs = {"profile.managed_default_content_settings.images":2}
    # chrome_options.headless = True


    # chrome_options.add_experimental_option("prefs", prefs)
    # myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return browser

def getGoogleHomepage(browser):
    browser.get("https://www.google.com")
    return browser.page_source

def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")