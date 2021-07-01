from auth import run
import requests
import json
class ValoApi:
    
    def __init__(self, username, password, region):
        self.username = username
        self.password = password
        self.region = region

        self.header,self.userID=self.login()
        self.gname,self.tag=self.name()

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
        return gname,tag
    
    def match(self):
        head2 = {'Content-Type': 'application/json',}
        head2.update(self.header)
        start=0
        r=requests.get(f"https://pd.{self.region}.a.pvp.net/mmr/v1/players/{self.userID}/competitiveupdates?startIndex={start}&endIndex={start+20}", headers=head2)
        data=r.json()
        print(json.dumps(data,indent=2))
        '''
        tier=""
        rr=""
        while(start<=100):
            r=requests.get(f"https://pd.{self.region}.a.pvp.net/mmr/v1/players/{self.userID}/competitiveupdates?startIndex={start}&endIndex={start+20}", headers=head2)
            data=r.json()
            for i in data['Matches']:
                if i['RankedRatingEarned']!=0:
                    tier=i['TierAfterUpdate']
                    rr=i['RankedRatingAfterUpdate']
                    start=101
                    break
                else:
                    start=start+20
        
        print(tier,rr)'''
    
    def store(self):
         r = requests.get(f'https://pd.{self.region}.a.pvp.net/store/v2/storefront/{self.userID}', headers=self.header)
         data=r.json()
         single_skins = data["SkinsPanelLayout"]["SingleItemOffers"]
         for skin in single_skins:
             res= requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{skin}")
             data=res.json()
             print(data['data']['displayName'])
    
    '''def mmr(self):
         r = requests.get(f'https://pd.{self.region}.a.pvp.net/mmr/v1/players/{self.userID}', headers=self.header)
         print(r.json())'''