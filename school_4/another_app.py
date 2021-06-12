import requests
import json

URL = 'http://127.0.0.1:8000/studentApi/'

def get_student(id=None):
    data = {}
    if id is not None:
        data = {'id':id}

    json_data  = json.dumps(data)
    r          = requests.get(url=URL, data=json_data)
    data       = r.json()
    print(data)

# get_student()



def post_student():
    data = {
        'name':'another',
        'age': 26,
        'city':'La-whore'
    }

    json_data  = json.dumps(data)
    r          = requests.post(url=URL, data=json_data)
    data       = r.json()
    print(data)

post_student()