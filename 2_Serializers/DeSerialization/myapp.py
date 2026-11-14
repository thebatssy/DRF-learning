# this is a client file which will send request to the server and get response from the server
import requests, json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name': 'Ravi',
    'roll': 104,
    'city': 'Dhanbad'
}

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data) 
