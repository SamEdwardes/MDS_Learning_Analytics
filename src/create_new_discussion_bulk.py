import dotenv
import os
import pandas as pd
import requests
import json

"""
For the script to work you must create a .evn file that contains:
CANVAS_API_TOKEN=...
In ... paste your token there
"""

"""
Tracker of what I have posted:
askscience:
    index 0:4
    index 5:200
"""

verbose = False
post = False

# API TOKEN
dotenv.load_dotenv(dotenv.find_dotenv())
TOKEN = os.environ.get('CANVAS_API_TOKEN')

# API CALL
# https://<canvas>/api/v1/courses/<course_id>/discussion_topics
url_base = 'https://ubc.instructure.com'
url_1 = '/api/v1/courses/'
course_id = 46341  # 46341 canvas hackathon
url_2 = '/discussion_topics'
url = url_base + url_1 + str(course_id) + url_2
headers = {'Authorization': 'Bearer ' + TOKEN}

# LOOP THROUGH AND POST
df = pd.read_csv("data/2019-11-02_reddit-data-askscience.csv")

for i in range(5, 201):
    title_to_post = df["discussion_topic_title"][i]
    message_to_post = df["discussion_topic_message"][i]

    if verbose:
        print("#"*50)
        print(title_to_post)
        print("#"*50)
        print(message_to_post)

    data = {
        'title': title_to_post,
        'message': message_to_post,
        }
        
    # post to canvas
    if post:
        requests.post(url, headers=headers, data=data)
        print("#"*25)
        print(f"Posted #{i + 1}: {title_to_post}")

