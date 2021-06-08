import requests

r = requests.get('http://127.0.0.1:8000/json-all/')

json_data = r.json()
headers   = r.headers['content-type']
encoding  = r.encoding
text      = r.text



print(json_data)
print(headers)
print(encoding)
print(text)