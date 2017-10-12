import requests
from os import environ 


api = environ.get("API_KEY")

url = "https://vision.googleapis.com/v1/images:annotate?key=" + api

headers = {
    "content-type": "application/json"
}

json = {
  "requests":[
    {
      "image":{
          "source": {
            "imageUri": "https://scontent.cdninstagram.com/t51.2885-15/e35/11380987_1445181789138848_233601423_n.jpg"
          }
      },
      "features":[
        {
          "type":"LABEL_DETECTION",
          "maxResults": 10
        }
      ]
    }
  ]
}


r = requests.post(url, json=json, headers=headers)
print(r.json())