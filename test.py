from api import ValoApi
'''
riotid=input("Enter riot username: ")
password=input("Enter riot password: ")
print("REGIONS:\nnorth america - na , asia - ap , europe - eu , korea - ko ")
region=input("Enter region: ")
'''
try:
    valo=ValoApi('RiotUsername','RiotPassword','Region')
except:
    print('A login error occurred. F')


#valo.wallet()
#valo.inventory()
#valo.mmr()
#valo.store()

