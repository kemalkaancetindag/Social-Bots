from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time


def scrape_twitch(twitch_username):


    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=r'C:\Users\Kaan\Desktop\geckodriver.exe')
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)
    driver.get(f"https://www.twitch.tv/{twitch_username}/videos") 
    time.sleep(2)
    recent_broadcasts_viewall_link = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div[2]/div[1]/div/a")
    recent_broadcasts_viewall_link.click()
    time.sleep(2)


    influencer_object = dict()
    recent_broadcast_stat_list = list()

    all_recent_broadcasts = driver.find_elements(by=By.XPATH, value="//div[contains(@class,'Layout-sc-nxg1ff-0') and contains(@class, 'kMghud')]")



    if len(all_recent_broadcasts) < 11:
        last_chapter_length = 0
        for i in range(1,len(all_recent_broadcasts)):
            duration = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div[{i}]/article/div[2]/div/div[5]/a/div/div[2]/div").get_attribute("innerHTML")    
            views = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div[{i}]/article/div[2]/div/div[5]/a/div/div[3]/div").get_attribute("innerHTML")
            title = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div[{i}]/article/div[1]/div/div[1]/div[1]/div/a/h3").get_attribute("innerHTML")
            thumb_image = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div[{i}]/article/div[2]/div/div[5]/a/div/div[1]/div[2]/div/div/div[2]/img").get_attribute("src")                
            
            try:
                chapter_button = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div[{i}]/article/div[1]/div/div[1]/div[3]/div/div[1]/button")
                chapter_button.click()
                time.sleep(0.5)
                
                all_chapters = driver.find_elements(by=By.XPATH, value="//div[contains(@class,'Layout-sc-nxg1ff-0') and contains(@class, 'media-row') and contains(@class, 'kTkZWx')]")
                
                
                chapter_length = -1*(last_chapter_length-len(all_chapters))
                last_chapter_length = len(all_chapters)
                
                
                
            except:
                chapter_length = 1
            
            recent_broadcast_stat_list.append({"duration":duration,"views":views.split(" ")[0],"title":title,"chapter_length":chapter_length,"thumb_image":thumb_image})
                                                                                    
        
    else:
        last_chapter_length = 0
        for i in range(1,len(all_recent_broadcasts[:11])):
            duration = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div[{i}]/article/div[2]/div/div[5]/a/div/div[2]/div").get_attribute("innerHTML")                                                                                                                            
            views = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div[{i}]/article/div[2]/div/div[5]/a/div/div[3]/div").get_attribute("innerHTML")
            title = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div[{i}]/article/div[1]/div/div[1]/div[1]/div/a/h3").get_attribute("innerHTML")
            thumb_image = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div[{i}]/article/div[2]/div/div[5]/a/div/div[1]/div[2]/div/div/div[2]/img").get_attribute("src")                
            try:
                chapter_button = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div[{i}]/article/div[1]/div/div[1]/div[3]/div/div[1]/button")
                chapter_button.click()
                time.sleep(0.5)
                
                all_chapters = driver.find_elements(by=By.XPATH, value="//div[contains(@class,'Layout-sc-nxg1ff-0') and contains(@class, 'media-row') and contains(@class, 'kTkZWx')]")
                
                
                chapter_length = -1*(last_chapter_length-len(all_chapters))
                last_chapter_length = len(all_chapters)
                
                
                
            except:
                chapter_length = 1

            recent_broadcast_stat_list.append({"duration":duration,"views":views.split(" ")[0],"title":title,"chapter_length":chapter_length, "thumb_image":thumb_image})
            
            
    #POPULAR CLIPS


    driver.get(f"https://www.twitch.tv/{twitch_username}/videos")
    time.sleep(2)
    clip_viewall_link = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div[3]/div[1]/div/a")
    clip_viewall_link.click()
    time.sleep(2)

    all_popular_clips = driver.find_elements(by=By.XPATH, value="//div[contains(@class,'Layout-sc-nxg1ff-0') and contains(@class, 'kMghud')]")


    popular_clips_stat_list = []





    if len(all_popular_clips) < 11:
        for i in range(1,len(all_popular_clips)):
            duration = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[{i}]/article/div[2]/div[5]/a/div/div[2]/div").get_attribute("innerHTML")
            views = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[{i}]/article/div[2]/div[5]/a/div/div[3]/div").get_attribute("innerHTML")
            title = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[{i}]/article/div[1]/div/div[1]/div[1]/div/a/h3").get_attribute("innerHTML")
            thumb_image = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[{i}]/article/div[2]/div[5]/a/div/div[1]/img").get_attribute("src")

            popular_clips_stat_list.append({"duration":duration,"views":views.split(" ")[0],"title":title,"thumb_image":thumb_image})


    else:
        for i in range(1,len(all_recent_broadcasts[:11])):
            duration = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[{i}]/article/div[2]/div[5]/a/div/div[2]/div").get_attribute("innerHTML")
            views = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[{i}]/article/div[2]/div[5]/a/div/div[3]/div").get_attribute("innerHTML")
            title = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[{i}]/article/div[1]/div/div[1]/div[1]/div/a/h3").get_attribute("innerHTML")
            thumb_image = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[{i}]/article/div[2]/div[5]/a/div/div[1]/img").get_attribute("src")

            popular_clips_stat_list.append({"duration":duration,"views":views.split(" ")[0],"title":title,"thumb_image":thumb_image})




    driver.get(f"https://www.twitch.tv/{twitch_username}")
    time.sleep(3)
    try:
        username = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[2]/a/div/h1").get_attribute("innerHTML")
        user_image = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/a/div/figure/img").get_attribute("src")
        followers = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[2]/p").get_attribute("innerHTML").split(" ")[0]
    except:
        username = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/h1").get_attribute("innerHTML")
        user_image = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/a/div[1]/figure/img").get_attribute("src")
        followers = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/span/div/div/span").get_attribute("innerHTML").split(" ")[0]


    recent_category_list = list()

    try:
        is_live = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/a/div[2]/div/div")
        user_link = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a")
        user_link.click()
        time.sleep(1.5) 
        recent_categories_parent = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/div[2]")            
        recent_categories = recent_categories_parent.find_elements(by=By.XPATH, value="./div[contains(@class, 'ftYHa-d') and contains(@class, 'InjectLayout-sc-588ddc-0')]")

        for category in recent_categories:
            recent_category_list.append(category.find_element(by=By.XPATH, value="./div/div/div/div/div/div/span/a/h2").get_attribute("innerHTML"))
                
                
        
    except:
        recent_categories_parent = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/div[2]")    
        
        recent_categories = recent_categories_parent.find_elements(by=By.XPATH, value="./div[contains(@class, 'ftYHa-d') and contains(@class, 'InjectLayout-sc-588ddc-0')]")
        for category in recent_categories:
            recent_category_list.append(category.find_element(by=By.XPATH, value="./div/div/div/div/div/div/span/a/h2").get_attribute("innerHTML"))

    
    influencer_object["username"] = username
    influencer_object["user_image"] = user_image
    influencer_object["followers"] = followers
    influencer_object["recent_broadcasts"] = recent_broadcast_stat_list
    influencer_object["popular_clips"] = popular_clips_stat_list
    influencer_object["recent_categories"] = recent_category_list

                    
    print(influencer_object)    


    driver.quit()





scrape_twitch("wtcn")