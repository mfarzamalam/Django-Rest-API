import requests
import json


python_dict_data = {
    'name':'Farzam',
    'roll':101,
    'city':'Karachi',
}


convert_into_json = json.dumps(python_dict_data)
data              = convert_into_json
URL = "http://127.0.0.1:8000/create/"

r = requests.post(url=URL, data=data)

result = r.json()

print(result)