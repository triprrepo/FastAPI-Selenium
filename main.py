from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
import os
import load_cookies
import only_autoposter
import random 


SECRET = os.getenv("SECRET")

#
app = FastAPI()

class Msg(BaseModel):
    msg: str
    secret: str

@app.get("/")

async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}

@app.get("/homepage")
async def demo_get():
    browser=createDriver()
    homepage = getGoogleHomepage(browser)
    browser.close()
    return homepage

@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}
    

@app.get("/facebook")
async def getting_to_facebook():
    print("got here")
    cookies = load_cookies.loading_cookies()
    print("loaded cookies")
    load_cookies.adding_cookies_browser(cookies)
    print("cookies added to the browser")
    return "i got here"


@app.get("/post_facebook")
async def posting_to_facebook():
    
    # Unmoderated groups
    groups_links_list = [
        "https://www.facebook.com/groups/1494117617557521", \
        "https://www.facebook.com/groups/viagem.jmjtur", \
        "https://www.facebook.com/groups/361530938056499/"  
    ]
    
    # Moderated
    moderated_links_list = [
        "https://www.facebook.com/groups/133422387092305", \
        "https://www.facebook.com/groups/361530938056499/"  
    ]


    # Set up text content to post
    message = [
        "Veja no Tripr centenas de excursões de diversas agências, saindo de SP em Março e outros meses! https://tripr.com.br/search_trips", \
        "Encontre mais de 100 viagens de diversas agências, saindo de SP & Região em Março e outros meses no Tripr! https://tripr.com.br/search_trips"
        ]
    
    #pick one of the two phrases above
    randonmized_group_list = random.sample(groups_links_list, len(groups_links_list))

    # Set up paths of images to post
    # images_list = ['C:/Users/OEM/Pictures/sample1.jpg','C:/Users/OEM/Pictures/sample2.jpg'] 
    images_list = [] 
    
    #setting up undectetable Chrome
    cookies = load_cookies.loading_cookies()
    browser = load_cookies.adding_cookies_browser(cookies)
    "print(loaded)"

    # Get page
    print("getting to fb")
    browser.get("https://www.facebook.com")
    
    # Post on each group
    
    n = 1
    for group in randonmized_group_list:
        try:
            f"going to the {n} site"
            random_message = random.choice(message)
            browser.get(group)
            time.sleep(3)
            browser.find_element(By.XPATH,'//span[text()="Write something..."]').click()
            print("photo cliked")
            time.sleep(random.randint(2,4))
            #photo_element = browser.find_element(By.XPATH,'//input[@type="file" and @accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]')
            #photo_element.send_keys(photo)
            time.sleep(random.randint(8,12))
            browser.find_element(By.XPATH,'//*[@class="_1mf _1mj"]').send_keys(random_message)
            time.sleep(10)
            post_button = browser.find_element(By.XPATH,'//div/span/span[text()="Post"]')
            post_button.click()
            print(f"posted on group {n}")
            time.sleep(random.randint(10,22))
            n += 1
        except:
            print("group failed")
            
    return {"message": f"posted in {n} groups"}