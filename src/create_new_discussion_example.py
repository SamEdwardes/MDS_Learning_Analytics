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

title_to_post = "This is a test posting"
message_to_post = "Test from Sam Edwardes"

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
data = {
    'title': title_to_post,
    'message': message_to_post,
    }

# SEND DATA
requests.post(url, headers=headers, data=data)
# data = r.json()  # returns a list of dictionaries containg post information
