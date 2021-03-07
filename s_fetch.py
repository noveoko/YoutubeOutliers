from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from fp.fp import FreeProxy
import random

#---->PROXY CODE -----------------------------------------------------------------------
def setProxy():
    print("Getting new proxy!")
    proxy = FreeProxy(anonym=True).get()
    proxy = FreeProxy(country_id=['DE', 'PL','RU']).get()
    if proxy:
        return proxy
    else:
        print("No proxy available!")

#----> OTHER CODE -----------------------------------------------------------------------

def get_info(string):
    name, url, subs = [a.strip() for a in string.split(";")]
    url = url.split("/")[-1]
    return (name, url, subs)

def get_channels(path="top_1k_youtube.txt"):
    return [get_info(a) for a in open(path,'r',encoding='utf-8').readlines()]

#---->SELENIUM------------------------------------------------------------------------
driverPath = ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--proxy-server=%s' % setProxy())
driver = webdriver.Chrome(executable_path=r'C:\Users\Marcin\Documents\software\chromedriver\chromedriver.exe',chrome_options=chrome_options)
#driver = webdriver.Chrome(driverPath)

for data in get_channels():
    name, channel_id, subs = data
    print("Gettings videos for:", name, channel_id,subs)
    time.sleep(random.choice([1.0,0.1,3.0,1.11,1.12,0.02,5.0]))
    url = f'https://www.youtube.com/channel/{channel_id}/videos'

    driver.get(url)

    height = driver.execute_script("return document.documentElement.scrollHeight")
    previousHeight = -1

    h_count = 0
    max_hCount = 2
    while previousHeight < height and h_count < max_hCount:
        h_count+=1
        previousHeight = height
        driver.execute_script(f'window.scrollTo(0,{height + 10000})')
        time.sleep(1)
        height = driver.execute_script("return document.documentElement.scrollHeight")

    vidElements = driver.find_elements_by_id('details')
    vid_urls = []
    for v in vidElements:
        link = v.find_elements_by_tag_name("a")
        v=v[0]
        link_href = v.get_attribute('href').strip()
        video_title = v.text.strip()
        vid_urls.append([link_href, video_title])
        print("Vid URLS collected", len(vid_urls),vid_urls[-1])
    with open(f"video_lists/{channel_id}.txt",'w',encoding='utf-8') as outfile:
        for vid_url in vid_urls:
            outfile.write(f"{vid_url[0]};{vid_url[1]}\n")
        print("saved videos for ", name, channel_id)

