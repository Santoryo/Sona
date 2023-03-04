import lockfile
import requests
import asyncio


async def lcuCall(method, endpoint, arg=None):
    _lockfile = await lockfile.getCredentials()

    status = 405
    response = ""
    
    if(_lockfile):
        url = f"https://127.0.0.1:{_lockfile[2]}"
        passwd = _lockfile[3]

        if method == "GET":
            try:
                r = requests.get(f'{url}{endpoint}', auth=('riot', passwd) ,verify="riotgames.pem")
                response = r.json()
                status = r.status_code
                response = response['statusMessage']
            except requests.exceptions.RequestException as e:
                print(e)
        elif method == "PUT":
            try:
                r = requests.put(f'{url}{endpoint}', auth=('riot', passwd) ,verify="riotgames.pem", json={'statusMessage': arg})
                status = r.status_code
                response = r.json()
            except requests.exceptions.RequestException as e:
                print(e)


    return status, response

