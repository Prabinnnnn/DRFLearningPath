import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"
def get_data(id = None): #id no id is given then default id is none
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)
#get_data()
def post_data():
    data = {
        'name': 'John Doe',
        'roll': 123,
        'city': 'New York'
    }
    json_data = json.dumps(data) #convert the python dictionary into json format
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)
#post_data()

def update_data():
    data = {
        'id': 1, #this is the id of the student we want to update
        'name': 'Jane Doe',
        'roll': 456,
        'city': 'Los Angeles'
    }
    json_data = json.dumps(data) #convert the python dictionary into json format
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

#update_data()

def delete_data():
    data = {
        'id': 1 #this is the id of the student we want to delete
    }
    json_data = json.dumps(data) #convert the python dictionary into json format
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)
delete_data()

