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

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.execute_script("window.scrollTo(0, 50);")


reply_count = 0
tweet_count = 1
while True:
    try:
        tweet = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[{tweet_count}]")        
        try:
            reply = tweet.find_element(by=By.XPATH, value=f"./div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/div/div[2]/span/span/span").get_attribute("innerHTML")
            retweet = tweet.find_element(by=By.XPATH, value=f"./div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[2]/span/span/span").get_attribute("innerHTML")                                                                    
            print(reply)
            print(retweet)
            print("----------")
            reply_count += 1
        except:
            try:
                try:
                    reply = tweet.find_element(by=By.XPATH, value=f"./div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/span/span/span").get_attribute("innetHTML")
                    retweet = tweet.find_element(by=By.XPATH, value=f"./div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/span/span/span").get_attribute("innerHTML")                                
                except:
                    driver.execute_script("window.scrollTo(0, (document.body.scrollHeight/15));")
                    

                print(reply)
                print(retweet)
                print("----------")
                reply_count += 1    
            except:
                print("hata")
                print(tweet_count)
                print("----------")
    except:
        print("tweet not found")
            
        

        
    
    
    
    tweet_count += 1

    if tweet_count == 5:
        
        time.sleep(2)
    if reply_count == 10:
        break

print(tweet_count)
    
    
    
    
    
    
    
        
    
    











