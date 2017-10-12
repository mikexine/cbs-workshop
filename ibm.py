import requests
from os import environ 


api = environ.get("IBM")
url = "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?version=2016-05-20&api_key=" + api
image_url = "https://scontent.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/13531824_254634018249272_610079245_n.jpg"

url += "&url=" + image_url
r = requests.get(url)
print(r.json())