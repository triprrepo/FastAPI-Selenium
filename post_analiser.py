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
from webdriver_manager.chrome import ChromeDriverManager
import pickle
from csv import DictReader
import time
from time import sleep
import os.path
import only_autoposter
import load_cookies
import random 


def post_analyzer(cookies):
    
    # Set up Facebook groups to post, you must be a member of the group
    groups_links_list = [
        "https://www.facebook.com/groups/1494117617557521/", \
        "https://www.facebook.com/groups/133422387092305/", \
        "https://www.facebook.com/groups/viagem.jmjtur/", \
        "https://www.facebook.com/groups/361530938056499/"  
    ]
    
    #setting up undectetable Chrome
    browser = load_cookies.adding_cookies_browser(cookies)

    # Get page
    print("getting to fb")
    browser.get("https://www.facebook.com/groups/1494117617557521?sorting_setting=CHRONOLOGICAL")
    sleep(random.randint(4,6))
    
    #name I want to get
    last_member = ["Marlon Sonza", "https://www.facebook.com/groups/1494117617557521/user/100002128662699/?__cft__[0]=AZXxkUulafZx3DoZfhyV8RiEV-85jiJ9pmM8tar9U1KD1ARdE8e2UpkAAIty2CBUcSbCRMnobP2SqLAwPnghmMOSna4Y_5f7CttUCKtYhUTkRN10fPeB_hmofeH5hHPQ4mLKpvHFdRe6szSU8ip3kbuE3mE1IRMXcYSvhOZvA0_Le1icD9-Kkl-mhRC2--0IcoA&__tn__=-UC%2CP-R"]
    new_members = [ ]
    
    #scroll down until finding the last contact scrapped
    while True:
        #scroll down
        browser.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        print("scrolling down")
        try:
            #looking for the last name that it has scrapped on the previous time. If finds it, stop scrolling down
            
            ################################### NEEDS IMPROVEMENT (HERE ONLY SEARCH BY NAME, SO IT WON'T FIND EXCATLY THE LAST POST)  #######################
            
            text = WebDriverWait(browser, random.randint(3,5)).until(EC.presence_of_element_located((By.XPATH, f"//*[text()='{last_member[0]}']")))
            print(f"found {last_member[0]}")
            break
        except:
            pass
    
    
    
    # n = 1
    # all_posts = browser.find_elements(By.XPATH,'//*[@class="x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z"]')
    # for post in all_posts:
    #     print(f"post {n}")
    #     print(post.find_element(By.XPATH,'//*[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"]').text)
    #     # name = post.find_element(By.XPATH,'//*[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"]')
    #     # print(f"{name.text}")
    #     n += 1

    # Encontrar todos os posts no grupo
    group_posts = []
    posts = browser.find_elements(By.XPATH, "//div[contains(@class,'x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z')]")
    print(posts)
    print(len(posts))

    # Imprimir o texto de cada post
    for index, post in enumerate(posts):
        print(f"post{index}")
        print(post)
        #achar uma div aqui no meio ou fazer post[index] para capturar correto
        name_spans = post.find_elements(By.XPATH,".//a[contains(@class,'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f')]")
        # name_spans = post.find_elements(By.CLASS_NAME, "xt0psk2")
        # name_spans = post.find_elements(By.TAG_NAME, "span")
        for i, name in enumerate(name_spans):
            print(name.get_attribute("id"))
            print(f"post n{i}")
            print(name.text)


        # final_name = name_spans.find_element(By.CLASS_NAME, "xt0psk2")
        # print(f"post{index.text}")
        # print(post.text) 
        #post_texts = post.find_element(By.XPATH, "//div[contains(@class,'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xi81zsa x1yc453h')]")
        #print(post_texts)
        #print(len(post_texts))
        #print(post_texts.text)
        # for post_text in post_texts:
        #     group_posts.append({f"post{index}": post_text.text})
        #     print(f"post{index} = {group_posts[index]}")
        #     print(post_text.text)
        # for post_text in post_texts:
        #     group_posts.append({f"post{index}": post_text.text})
        #     print(f"post{index} = {group_posts[index]}")


#getting cookies
cookies = load_cookies.loading_cookies()
post_analyzer(cookies)
