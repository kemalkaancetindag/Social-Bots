import requests


def get_user_id(screen_name):
    headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAKAMdAEAAAAAydUJyT8uFaFEUxvvWGXm76T1ltY%3DQuPvsmPR5eQtLmULFg6j5BhERn1Es1PDYt1UtR8vfDuGh7ihWz'}
    response = requests.get(f"https://api.twitter.com/1.1/users/show.json?screen_name={screen_name}", headers=headers)    
    if response.status_code == 200:
        user_id = response.json()["id"]
        followers = response.json()["followers_count"]
        banner_image = response.json()["profile_banner_url"]
        profile_image = response.json()["profile_image_url"]
        name = response.json()["name"]

        influencer_object = {"user_id":user_id,"name":name,"followers":followers, "banner_image":banner_image, "profile_image":profile_image}

        return influencer_object



def get_user_tweets(user_id):
    
    headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAKAMdAEAAAAAydUJyT8uFaFEUxvvWGXm76T1ltY%3DQuPvsmPR5eQtLmULFg6j5BhERn1Es1PDYt1UtR8vfDuGh7ihWz'}
    response = requests.get(f"https://api.twitter.com/2/users/{user_id}/tweets?tweet.fields=public_metrics", headers=headers)
    
    if response.status_code == 200:
        tweet_data = response.json()["data"]        
        return tweet_data


def calculate_engagement_score(tweet_data, total_followers):
    total_replies = 0
    total_likes = 0
    for data in tweet_data:
        total_replies += data["public_metrics"]["reply_count"]
        total_likes += data["public_metrics"]["like_count"]

    engagement_score = (((total_replies+total_likes)/total_followers)*100)
    return engagement_score



def final_influencer_object(screen_name):
    influencer_object = get_user_id(screen_name)

    tweet_data = get_user_tweets(influencer_object["user_id"])


    engagement_score = calculate_engagement_score(tweet_data, influencer_object["followers"])

    influencer_object["last_tweets"] = tweet_data
    influencer_object["engagement_score"] = engagement_score

    return influencer_object

inf_object = final_influencer_object("grahamlicc")
print(inf_object)

