import requests
from datetime import datetime

def dateValidity(uuid):
    date=datetime.now().replace(microsecond=0)
    r=requests.get("https://valorant-api.com/v1/seasons")
    data=r.json()
    #print(datetime.strptime(data['data'][0]['startTime'], "%Y-%m-%dT%H:%M:%SZ"))
    #print(date)
    for i in data['data']:
        start=datetime.strptime(i['startTime'],"%Y-%m-%dT%H:%M:%SZ")
        end=datetime.strptime(i['endTime'],"%Y-%m-%dT%H:%M:%SZ")
        if i['uuid']==uuid and start<date<end:
            return True
    return False        

'''
if __name__=="__main__":
    print(dateValidity(""))
'''

ranks={
    1:'iron',
    2:'bronze',
    3:'silver',
    4:'gold',
    5:'platinum',
    6:'diamond',
    7:'immortal',
    8:'radiant'
}

currencies={
    "VP":"85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
    "RP":"e59aa87c-4cbf-517a-5983-6e81511be9b7"
}