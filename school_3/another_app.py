import json
import requests

URL = "http://127.0.0.1:8000/student/"

def post_data():
    data = {
        'name':'farzam',
        'city':'krachi',
        'age':26,
    }

    json_data = json.dumps(data)
    r  = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


post_data()