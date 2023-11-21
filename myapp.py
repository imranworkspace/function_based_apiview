import requests
import json

_URL='http://127.0.0.1:8000/api/'

def get_api(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r = requests.get(url=_URL,data=json_data)
    data=r.json()
    print('data',data)


def post_api():
    data={
        "name":"imran",
        "mobile":7710881086
    }
    # 
    headers = {"content-Type":"application/json"}
    json_data=json.dumps(data)
    r = requests.post(url=_URL,headers=headers,data=json_data)
    data=r.json()
    print('data',data)

def put_api(id=None):
    if id is not None:
        data={'id':id}
    data={
        "name":"imran",
        "mobile":7710881086
    }
    # 
    headers = {"content-Type":"application/json"}
    json_data=json.dumps(data)
    r = requests.put(url=_URL,headers=headers,data=json_data)
    data=r.json()
    print('data',data)

def delete_api(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r = requests.get(url=_URL,data=json_data)
    data=r.json()
    print('data',data)


# calling fun
get_api()
post_api()
put_api()
delete_api()