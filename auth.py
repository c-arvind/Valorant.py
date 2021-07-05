import aiohttp
import requests
import json
import urllib
import re


def run(username, password):
    client = requests.session()
    data = {
        'client_id': 'play-valorant-web-prod',
        'nonce': '1',
        'redirect_uri': 'https://playvalorant.com/opt_in',
        'response_type': 'token id_token',
    }
    client.post('https://auth.riotgames.com/api/v1/authorization', json=data)

    data = {
        'type': 'auth',
        'username': username,
        'password': password
    }
    r = client.put('https://auth.riotgames.com/api/v1/authorization',json=data)
    data = r.json()
    #print(json.dumps(uri, indent = 3))
    
    pattern = re.compile('access_token=((?:[a-zA-Z]|\d|\.|-|_)*).*id_token=((?:[a-zA-Z]|\d|\.|-|_)*).*expires_in=(\d*)')
    data = pattern.findall(data['response']['parameters']['uri'])[0]
    access_token = data[0]
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    r= client.post('https://entitlements.auth.riotgames.com/api/token/v1', headers=headers, json={})
    data =  r.json()
    entitlements_token = data['entitlements_token']
    #print('Entitlements Token: ' + entitlements_token)

    r=client.post('https://auth.riotgames.com/userinfo', headers=headers, json={})
    data = r.json()
    user_id = data['sub']
    #print('User ID: ' + user_id)
    

    r=client.get('https://valorant-api.com/v1/version')
    data=r.json()
    headers['X-Riot-ClientVersion'] =data['data']['riotClientVersion']
    headers['X-Riot-Entitlements-JWT'] = entitlements_token
    headers['X-Riot-ClientPlatform'] = 'ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9'
    #print(data) 
    return headers,user_id

'''
if __name__ == '__main__':
    run('', '')
'''