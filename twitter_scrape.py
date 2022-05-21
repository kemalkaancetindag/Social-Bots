from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time




options = Options()
options.headless = False
fp = webdriver.FirefoxProfile("C:/Users/Kaan/AppData/Roaming/Mozilla/Firefox/Profiles/lk2eo77a.Test Profile")
driver = webdriver.Firefox(options=options, executable_path=r'C:\Users\Kaan\Desktop\geckodriver.exe',firefox_profile=fp)
driver.set_window_position(0, 0)
driver.set_window_size(1920, 1080)
driver.get(f"https://twitter.com/grahamlicc") 
time.sleep(5)

influencer_object = {}

banner_image = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/a/div/div[2]/div/img").get_attribute("src")
profile_image = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div/div[2]/div/a/div[3]/div/div[2]/div/img").get_attribute("src")
username = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div/span[1]/span").get_attribute("innerHTML")
bio = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[1]/span").get_attribute("innerHTML")
total_tweets = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div/div").get_attribute("innerHTML")

try:
    location = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[4]/div/span[1]/span/span").get_attribute("innerHTML")
except:
    location = None

try:
    joined = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[4]/div/span[3]/span").get_attribute("innerHTML")
except:
    joined = None

following = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[1]/a/span[1]/span").get_attribute("innerHTML")
followers = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[2]/a/span[1]/span").get_attribute("innerHTML")




counter = 1
tweet_counter = 0
last_tweet_stats = []
while True:   

    try:
            replies = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[{counter}]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/span/span/span").get_attribute("innerHTML")                
    except:
        replies = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[{counter+1}]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/div/div[2]/span/span/span").get_attribute("innerHTML")


    try:
        retweets = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[{counter}]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/span/span/span").get_attribute("innerHTML")
    except:
        retweets = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[{counter}]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[2]/span/span/span").get_attribute("innerHTML")

    print(retweets)
    
    
    
    
    
    
    
   
    try:
        try:
            replies = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[{counter}]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/span/span/span").get_attribute("innerHTML")                
        except:
            replies = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[{counter+1}]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/div/div[2]/span/span/span").get_attribute("innerHTML")
        retweets = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[{counter}]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/span/span/span").get_attribute("innerHTML")
        likes = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[{counter}]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/span/span/span").get_attribute("innerHTML")
        try:
            content = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[{counter}]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span").get_attribute("innerHTML")
        except:
            content = None                                    
        tweet_counter += 1                        
        last_tweet_stats.append({"replies":replies,"retweets":retweets,"likes":likes,"content":content})
    except:        
        print("Who To Follow")        
    
    counter += 1    
    if tweet_counter == 10:
        break


influencer_object["banner_image"] = banner_image
influencer_object["profile_image"] = profile_image
influencer_object["username"] = username
influencer_object["bio"] = bio
influencer_object["location"] = location
influencer_object["joined"] = joined
influencer_object["following"] = following
influencer_object["followers"] = followers
influencer_object["total_tweets"] = total_tweets.split(" ")[0]
influencer_object["last_tweets"] = last_tweet_stats

print(influencer_object)











