import json
import datetime
import time
import requests

#Subreddits to analyze
subreddits = ["Android", "androidapps", "SideProject", "opendirectories", "Piracy", "megalinks", "lifehacks"]
url_prefix = "https://www.reddit.com/r/"
url_postfix = "/about.json"

while True :
	current_time = datetime.datetime.now()
	print current_time

	for subreddit in subreddits :
		url = url_prefix + subreddit + url_postfix
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		# response = urllib.urlopen(url)
		response = requests.request("GET", url, headers = headers)
		jsonResponse = response.text
		index = jsonResponse.index("accounts_active")
		length = len("accounts_active")
		splitjsonResponse = jsonResponse[index+length+3:]
		commaindex = splitjsonResponse.index(",")

		active_users = splitjsonResponse[0:commaindex]
		print "Active users of "+subreddit+" = "+active_users
	time.sleep(900)