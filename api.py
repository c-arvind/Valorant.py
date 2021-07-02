from auth import run
import requests
import json
from utils import *
class ValoApi:
    
    def __init__(self, username, password, region):
        self.username = username
        self.password = password
        self.region = region

        self.header,self.userID=self.login()

    def login(self):
        header,userID=run(self.username, self.password)
        #print("ur user id "+userID)
        #print(header)
        return header,userID
    
    def name(self):
        bod='["'+self.userID+'"]'
        r=requests.put(f"https://pd.{self.region}.a.pvp.net/name-service/v2/players",data=bod, headers=self.header)
        details=r.json()
        gname=details[0]['GameName']
        tag="#"+details[0]['TagLine']
        print(f"WELCOME {gname} {tag}")
    
    def match(self):
        head2 = {'Content-Type': 'application/json',}
        head2.update(self.header)
        start=0
        r=requests.get(f"https://pd.{self.region}.a.pvp.net/mmr/v1/players/{self.userID}/competitiveupdates?startIndex={start}&endIndex={start+20}", headers=head2)
        data=r.json()
        print(json.dumps(data,indent=2))
       
    def curRank(self):    
        start=0
        while(start<=100):
            if start==100:
                print("unranked")
                break
            r=requests.get(f"https://pd.{self.region}.a.pvp.net/mmr/v1/players/{self.userID}/competitiveupdates?startIndex={start}&endIndex={start+20}", headers=self.header)
            data=r.json()
            for i in data['Matches']:
                if i['TierAfterUpdate']!=0 and dateValidity(i['SeasonID']):
                    print(f"Tier: {ranks[i['TierAfterUpdate']//3]} {i['TierAfterUpdate']%3 +1}")
                    print("Ranked Rating:",i['RankedRatingAfterUpdate'])
                    start=101
                    break  
                else:
                    start=start+20
                    break
        
        
    
    def store(self):
         r = requests.get(f'https://pd.{self.region}.a.pvp.net/store/v2/storefront/{self.userID}', headers=self.header)
         data=r.json()
         single_skins = data["SkinsPanelLayout"]["SingleItemOffers"]
         print("Today's items:")
         for skin in single_skins:
             res= requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{skin}")
             data=res.json()
             print(data['data']['displayName'])
    
    def wallet(self):
        r = requests.get(f'https://pd.{self.region}.a.pvp.net/store/v1/wallet/{self.userID}', headers=self.header)
        data=r.json()
        print("Valorant Points (VP) :",data['Balances'][currencies['VP']])
        print("Radianite Points (RP) :",data['Balances'][currencies['RP']])
             
    '''
    def mmr(self):
         r = requests.get(f'https://shared.ap.a.pvp.net/content-service/v2/content', headers=self.header)
         print(r.json()) 
    '''