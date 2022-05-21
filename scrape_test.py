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


texts = driver.find_elements(by=By.XPATH, value="//span[contains(@class,'r-qvutc0') and contains(@class, 'r-bcqeeo') and contains(@class,'r-poiln3') and contains(@class, 'css-16my406') and contains(@class, 'css-901oao')]")
aria_labels = driver.find_elements(by=By.XPATH, value="//div[contains(@class,'r-1mdbhws') and contains(@class, 'r-1s2bzr4') and contains(@class,'r-1wtj0ep') and contains(@class, 'r-18u37iz') and contains(@class, 'r-1ta3fxp') and contains(@class, 'css-1dbjc4n')]")
  
aria_labels2 = driver.find_elements(by=By.XPATH, value="//div[contains(@class,'css-1dbjc4n') and contains(@class, 'r-1mdbhws') and contains(@class,'r-1s2bzr4') and contains(@class, 'r-1wtj0ep') and contains(@class, 'r-18u37iz') and contains(@class, 'r-1ta3fxp') and contains(@class, 'r-18u37iz')]")



  
tweets = driver.find_elements(by=By.XPATH, value="//div[contains(@class,'r-1ny4l3l') and contains(@class,'r-1adg3ll') and contains(@class, 'r-qklmqi') and contains(@class, 'r-1igl3o0') and contains(@class, 'css-1dbjc4n')]")
all_tweets = driver.find_elements(by=By.XPATH, value="//div[contains(@class, 'r-1ny4l3l') and contains(@class, 'css-1dbjc4n') and contains(@class, 'r-1adg3ll')]")
find_elem
 
print(len(tweets))
for tweet in all_tweets:
    print(tweet.find_element(by=By.XPATH, value="//div[contains(@class,'css-1dbjc4n') and contains(@class, 'r-1mdbhws') and contains(@class,'r-1s2bzr4') and contains(@class, 'r-1wtj0ep') and contains(@class, 'r-18u37iz') and contains(@class, 'r-1ta3fxp') and contains(@class, 'r-18u37iz')]").get_attribute("aria-label"))
    


driver.quit()