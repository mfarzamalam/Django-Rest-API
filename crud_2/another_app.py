import requests
import json


URL = "http://127.0.0.1:8000/studentApi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    
    headers = {'content-Type':'application/json'}
    json_data= json.dumps(data )
    r = requests.get(url = URL, data=json_data, headers=headers)
    data = r.json()
    print(data )

# get_data(2)


def post_data():
    data = {
        'name':'Api_Name',
        'roll':255,
        'city':'Api_City',
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data, headers=headers)
    data = r.json()
    print(data)

# post_data()


def update_data(id):
    data = {
        'id'  :id,
        'name':'Api_Name',
        'roll':255,
        # 'city':'Api_City',
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data, headers=headers)
    data = r.json()
    print(data)

update_data(1)


def delete_data(id):
    headers = {'content-Type':'application/json'}

    data = {'id':id }

    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data, headers=headers)
    data = r.json()
    print(data)

# delete_data(2)