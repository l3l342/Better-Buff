import requests
import csv
from PIL import Image
import customtkinter


class Api_call:
    def __init__(self, weapon_name):
        self.weapon_name = weapon_name


    def buff(self):
        try:
            #umformen von id zu namen
            with open(f'code/data/databases/All.csv',encoding="utf-8") as data:         #WICHTIG: Realtiven pfad beachten
                reader = csv.reader(data, delimiter=';')                                    #Besserer Suchalgorithmu --> effizienz????
                for row in reader:
                    if self.weapon_name.lower() in row[1].lower():
                        weapon_id = row[0]
                        break
                        
            #api abfrage mit id
            res= requests.get(f'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id={weapon_id}&page_num=1&_=1657808768032').json()
            price = float((res['data']['items'][0]['price']))
            return round((price * 0.13), 2)
        except:
            return "Fehler"

    def steam(self):
        try:
            res = requests.get(f'https://steamcommunity.com/market/priceoverview/?country=DE&currency=3&appid=730&market_hash_name={self.weapon_name}').json()
            return res['lowest_price']
        except:
            return("Fehler")
    
    #TODO:skinport richtiger preis ??????
    def skinport(self):
        try:
            res = requests.get("https://api.skinport.com/v1/sales/history", params={
                "app_id": 730,
                "currency": "EUR",
                "market_hash_name": self.weapon_name }).json()
            
            price = res[0]['last_30_days']['median']  
            return price
        except:
            return ("Fehler")


    def graphic(self):
        
        with open('code/data/databases/all.csv',encoding="utf-8") as data:         #WICHTIG: Realtiven pfad beachten
            reader = csv.reader(data, delimiter=';')                                    #Besserer Suchalgorithmu --> effizienz????
            for row in reader:
                if self.weapon_name.lower() in row[1].lower():
                    weapon_id = row[0]
                    break
                    
        res= requests.get(f'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id={weapon_id}&page_num=1&_=1657808768032').json()
            
        url = res['data']['goods_infos'][f'{weapon_id}']['icon_url']
        image = Image.open(requests.get(url, stream=True).raw)

        photo = customtkinter.CTkImage(image, size=( 500, 250))

        return photo

print(Api_call("AK-47 | Safari Mesh (Well-Worn)").buff())