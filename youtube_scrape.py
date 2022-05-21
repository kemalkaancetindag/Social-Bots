import requests


def get_channel_id(channel_name):
    response = requests.get(f"https://www.googleapis.com/youtube/v3/channels?part=id&forUsername={channel_name}&key=AIzaSyAAURNtiniht-v-_2QK3s8IahFtonX1joo")
    if response.status_code == 200:        
        if len(response.json()["items"]) > 0:
            return response.json()["items"][0]["id"]

def get_channel_stats(channel_id):
    response = requests.get(f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={channel_id}&key=AIzaSyAAURNtiniht-v-_2QK3s8IahFtonX1joo")

    if response.status_code == 200:
        if len(response.json()["items"]) > 0:
            channel_stats = response.json()["items"][0]["statistics"]
            title = response.json()["items"][0]["snippet"]["title"]                        
            return channel_stats, title

def get_last_10_videos(channel_id):    
    video_ids = []
    response = requests.get(f"https://www.googleapis.com/youtube/v3/search?key=AIzaSyAAURNtiniht-v-_2QK3s8IahFtonX1joo&channelId={channel_id}&part=snippet,id&order=date&maxResults=10")    
    if response.status_code == 200:   
        if  len(response.json()["items"]) > 0:
            for item in response.json()["items"]:
                video_ids.append(item["id"]["videoId"])
    return video_ids                



def get_last_videos_stats(video_ids):
    video_stats = []
    
    for vid in video_ids:        
        response = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={vid}&key=AIzaSyAAURNtiniht-v-_2QK3s8IahFtonX1joo")
        print(response.status_code)
        if response.status_code == 200:
            if len(response.json()["items"]) > 0:
                
                video_statistics = response.json()["items"][0]["statistics"]
                video_statistics["video_url"] = f"https://www.youtube.com/watch?v={vid}"
                video_statistics["video_id"] = vid
                video_stats.append(video_statistics)
    return video_stats


def calculate_engagement_followers(video_stats, total_subs):
    total_likes = 0
    for stat in video_stats:
        total_likes += int(stat["likeCount"])

    follower_engagement = (total_likes/int(total_subs))*100
    return follower_engagement

def calculate_popularity(video_stats,total_impression):
    total_likes = 0
    total_comments = 0
    for stat in video_stats:
        total_likes += int(stat["likeCount"])
        total_comments += int(stat["commentCount"])

    total_engagement = total_likes + total_comments
    popularity_score = (total_engagement/int(total_impression))*100

    return popularity_score

        

channel_id = get_channel_id("newdaynewgame")

video_ids = get_last_10_videos(channel_id)

channel_stats, title = get_channel_stats(channel_id)

video_stats = get_last_videos_stats(video_ids)

engagement_score = calculate_engagement_followers(video_stats, channel_stats["subscriberCount"])
popularity_score = calculate_popularity(video_stats,channel_stats["viewCount"])

influencer_object = {}

influencer_object["title"] = title
influencer_object["channel_id"] = channel_id
influencer_object["interraction_result"] = engagement_score
influencer_object["popularity_result"] = popularity_score
influencer_object["channel_stats"] = channel_stats
influencer_object["last_videos"] = video_stats

print(influencer_object)




