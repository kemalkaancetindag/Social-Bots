from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time



def scrape_tiktok(tiktok_username):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=r'C:\Users\Kaan\Desktop\geckodriver.exe')
    driver.set_window_position(0, 0)
    driver.set_window_size(1024, 768)
    driver.get(f"https://www.tiktok.com/@{tiktok_username}")        



    influencer_object = dict()
    last_content_stats = []

    username = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/h2").get_attribute("innerHTML")
    total_likes = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div/div[1]/h2[1]/div[3]/strong").get_attribute("innerHTML")
    followers = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div/div[1]/h2[1]/div[2]/strong").get_attribute("innerHTML")
    following = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div/div[1]/h2[1]/div[1]/strong").get_attribute("innerHTML")

    influencer_object["username"] = f"@{tiktok_username}"
    influencer_object["total_likes"] = total_likes
    influencer_object["followers"] = followers
    influencer_object["following"] = following

    SCROLL_PAUSE_TIME = 1.7

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:                
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(SCROLL_PAUSE_TIME)

        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


    soup = BeautifulSoup(driver.page_source)
    all_content = soup.find_all("div", class_="tiktok-x6y88p-DivItemContainerV2")
    total_content = len(all_content)
    




    if total_content < 11:
        for i in range(1,total_content):
        
            try:
                warning = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[{i}]/div/div/div/a/div/div[2]/div/div[2]")        
                times_watched = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[{i}]/div/div/div/a/div/div[3]/strong").get_attribute("innerHTML")
                video_link = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[{i}]/div[1]/div/div/a").get_attribute("href")
                driver.get(video_link) 
                time.sleep(3)
                try:
                    driver.find_element(by=By.XPATH, value="//p[contains(text(), 'Something went wrong')]") 
                    likes = None
                    comments = None                    
                except:
                    try:
                        driver.find_element(by=By.XPATH, value="//p[contains(text(), 'Video currently unavailable')]") 
                        likes = None
                        comments = None                                                            
                    except:
                        try:
                            likes = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[1]/strong").get_attribute("innerHTML")            
                        except:          
                            try:  
                                likes = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[3]/button[1]/strong").get_attribute("innerHTML")
                            except:
                                try:
                                    likes = driver.find_element_by_xpath('//strong[@data-e2e="browse-like-count"]')
                                except:
                                    likes = driver.find_element_by_xpath('//strong[@data-e2e="like-count"]')
                                

                        try:
                            comments = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[2]/strong").get_attribute("innerHTML")
                        except:
                            try:
                                comments = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/button[2]/strong").get_attribute("innerHTML")
                            except:
                                try:                            
                                    comments = driver.find_element_by_xpath('//strong[@data-e2e="browse-comment-count"]')
                                except:
                                    comments = driver.find_element_by_xpath('//strong[@data-e2e="comment-count"]')


                
                new_stat_object = {"video_link":video_link,"times_watched":times_watched,"likes":likes,"comments":comments}
                last_content_stats.append(new_stat_object)
                
                


                driver.execute_script("window.history.go(-1)")       
                time.sleep(3)        
            except:
                times_watched = driver.find_element(by=By.XPATH, value = f"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[{i}]/div[1]/div/div/a/div/div[2]/strong").get_attribute("innerHTML")
                video_link = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[{i}]/div[1]/div/div/a").get_attribute("href")
                driver.get(video_link)   
                time.sleep(3)
                try:
                    driver.find_element(by=By.XPATH, value="//p[contains(text(), 'Something went wrong')]") 
                    likes = None
                    comments = None                    
                except:
                    try:
                        driver.find_element(by=By.XPATH, value="//p[contains(text(), 'Video currently unavailable')]") 
                        likes = None
                        comments = None                                                            
                    except:
                        try:
                            likes = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[1]/strong").get_attribute("innerHTML")            
                        except:          
                            try:  
                                likes = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[3]/button[1]/strong").get_attribute("innerHTML")
                            except:
                                try:
                                    likes = driver.find_element_by_xpath('//strong[@data-e2e="browse-like-count"]')
                                except:
                                    likes = driver.find_element_by_xpath('//strong[@data-e2e="like-count"]')
                                

                        try:
                            comments = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[2]/strong").get_attribute("innerHTML")
                        except:
                            try:
                                comments = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/button[2]/strong").get_attribute("innerHTML")
                            except:
                                try:                            
                                    comments = driver.find_element_by_xpath('//strong[@data-e2e="browse-comment-count"]')
                                except:
                                    comments = driver.find_element_by_xpath('//strong[@data-e2e="comment-count"]')

                new_stat_object = {"video_link":video_link,"times_watched":times_watched,"likes":likes,"comments":comments}
                last_content_stats.append(new_stat_object)

            


                driver.execute_script("window.history.go(-1)")  
                time.sleep(3)
    else:
        for i in range(1,10):
        
            try:
                warning = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[{i}]/div/div/div/a/div/div[2]/div/div[2]")        
                times_watched = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[{i}]/div/div/div/a/div/div[3]/strong").get_attribute("innerHTML")
                video_link = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[{i}]/div[1]/div/div/a").get_attribute("href")
                driver.get(video_link) 
                time.sleep(3)
                try:
                    driver.find_element(by=By.XPATH, value="//p[contains(text(), 'Something went wrong')]") 
                    likes = None
                    comments = None                    
                except:
                    try:
                        driver.find_element(by=By.XPATH, value="//p[contains(text(), 'Video currently unavailable')]") 
                        likes = None
                        comments = None                                                            
                    except:
                        try:
                            likes = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[1]/strong").get_attribute("innerHTML")            
                        except:          
                            try:  
                                likes = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[3]/button[1]/strong").get_attribute("innerHTML")
                            except:
                                try:
                                    likes = driver.find_element(by=By.XPATH, value='//strong[@data-e2e="browse-like-count"]').get_attribute("innerHTML")
                                except:
                                    likes = driver.find_element(by=By.XPATH, value='//strong[@data-e2e="like-count"]').get_attribute("innerHTML")
                                

                        try:
                            comments = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[2]/strong").get_attribute("innerHTML")
                        except:
                            try:
                                comments = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/button[2]/strong").get_attribute("innerHTML")
                            except:
                                try:                            
                                    comments = driver.find_element(by=By.XPATH, value='//strong[@data-e2e="browse-comment-count"]').get_attribute("innerHTML")
                                except:
                                    comments = driver.find_element(by=By.XPATH, value='//strong[@data-e2e="comment-count"]').get_attribute("innerHTML")
                
                new_stat_object = {"video_link":video_link,"times_watched":times_watched,"likes":likes,"comments":comments}
                last_content_stats.append(new_stat_object)
                
                


                driver.execute_script("window.history.go(-1)")       
                time.sleep(3)        
            except:
                print(i)
                times_watched = driver.find_element(by=By.XPATH, value = f"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[{i}]/div[1]/div/div/a/div/div[2]/strong").get_attribute("innerHTML")
                video_link = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[{i}]/div[1]/div/div/a").get_attribute("href")
                driver.get(video_link)   
                time.sleep(3)
                try:
                    
                    print(driver.find_element(by=By.XPATH, value="//p[contains(text(), 'Something went wrong')]").get_attribute("innerHTML"))
                    likes = None
                    comments = None                    
                except:
                    print("hata yok")
                    try:
                        driver.find_element(by=By.XPATH, value="//p[contains(text(), 'Video currently unavailable')]") 
                        likes = None
                        comments = None                                                            
                    except:
                        try:
                            print("geldi")
                            likes = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[1]/strong").get_attribute("innerHTML")            
                        except:          
                            try:  
                                likes = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[3]/button[1]/strong").get_attribute("innerHTML")
                            except:
                                try:
                                    likes = driver.find_element(by=By.XPATH, value='//strong[@data-e2e="browse-like-count"]').get_attribute("innerHTML")
                                except:
                                    likes = driver.find_element(by=By.XPATH, value='//strong[@data-e2e="like-count"]').get_attribute("innerHTML")
                                

                        try:
                            comments = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[2]/strong").get_attribute("innerHTML")
                        except:
                            try:
                                comments = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/button[2]/strong").get_attribute("innerHTML")
                            except:
                                try:                            
                                    comments = driver.find_element(by=By.XPATH, value='//strong[@data-e2e="browse-comment-count"]').get_attribute("innerHTML")
                                except:
                                    comments = driver.find_element(by=By.XPATH, value='//strong[@data-e2e="comment-count"]').get_attribute("innerHTML")

                new_stat_object = {"video_link":video_link,"times_watched":times_watched,"likes":likes,"comments":comments}
                last_content_stats.append(new_stat_object)

            


                driver.execute_script("window.history.go(-1)")  
                time.sleep(3)

                                                            
    influencer_object["total_content"] = total_content    
    influencer_object["last_contents"] = last_content_stats                    
    print(influencer_object)

    driver.quit()



scrape_tiktok("sudealkis")