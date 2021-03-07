from fp.fp import FreeProxy
import requests
import time
import pickle

key = "<API_KEY>"
#-----------------------------------------------------------------
def get_info(string):
    name, url, subs = [a.strip() for a in string.split(";")]
    url = url.split("/")[-1]
    return (name, url, subs)

def get_channels(path="top_1k_youtube.txt"):
    return [get_info(a) for a in open(path,'r',encoding='utf-8').readlines()]


def get_all_videos(list_of_channels):
    all_videos = {a[0]:[] for a in list_of_channels}

    for name, channel_id, subs in list_of_channels:
        print(f'getting videos for channel:{name}')
        proxy = FreeProxy(anonym=True).get()
        proxy = FreeProxy(country_id=['DE', 'PL','RU']).get()

        proxies = None

        if proxy:
            proxies = {
                "http": f"{proxy}",
                "https": f"{proxy}"
            }

            url = f"https://www.youtube.com/c/{channel_id}/videos"

            try:
                page = requests.get(url, proxies=proxies)

                if page.status_code==200:
                    page = page.content
                    #data = str(page).split(' ')
                    all_videos[channel_id] = page
                    print('Success on ', channel_id, len(page))
                    time.sleep(0.1)
                else:
                    print(page.status_code)
                    print("failed on ",channel_id)
            except Exception as ee:
                print(ee)
        else:
            print("Proxy Error!")

    pickle.dump(all_videos, 'all_videos.pickle')

if __name__ == "__main__":
    # channels = get_channels()
    # get_all_videos(channels)
