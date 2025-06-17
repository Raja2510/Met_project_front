import requests

def login(username,password):
    responce=requests.post(f'http://127.0.0.1:8000/login?username={username}&password={password}')
    if responce.status_code==200:
        return responce.json()
    
def register(name,username,age,password):
            res=requests.post(f"http://127.0.0.1:8000/create?name={name}&username={username}&age={age}&password={password}")
            return res.json()