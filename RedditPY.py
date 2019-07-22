import praw
import urllib.request
client = 'Enter your client Id here'
client_Secret = "Enter your client secret here"
url = []
url_title = []
url_parsed = []
path = "path for downloading images"
reddit = praw.Reddit(client_id = client ,client_secret = client_Secret,username = "Enter your account name ",password = "Enter your account password",user_agent = "any name you want")
#print(reddit.user.me())	
for submission in reddit.subreddit('Name of the subreddit').hot(limit = 1000):
	url.append(submission.url)
	url_title.append(submission.title)
for title in url_title:
	url_parsed.append(''.join(s for s in title if s.isalnum()))
for index in range(len(url)):
	urllib.request.urlretrieve(url[index],path+url_parsed[index]+".jpg")
print("Success !")



