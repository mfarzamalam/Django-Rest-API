import json
import requests

URL = "http://127.0.0.1:8000/student/"

def post_data():
    data = {
        'name':'Aslam',
        'city':'krachi',
        'age':24,
    }

    json_data = json.dumps(data)
    r  = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


post_data()