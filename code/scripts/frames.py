import customtkinter
from PIL import Image
import requests
import csv
import random
import os

class Frame:
    def __init__(self, database, home_frame):
        self.home_frame = home_frame
        self.database = database
        y=55
        x=20
        
        weapon0 = self.random_weapon()
        weapon1 = self.random_weapon()
        weapon2 = self.random_weapon()
        weapon3 = self.random_weapon()
        weapon4 = self.random_weapon()
        weapon5 = self.random_weapon()
        weapon6 = self.random_weapon()
        weapon7 = self.random_weapon()

        self.skin_image0 =  self.bild(weapon0,size= (  185, 163) )
        self.skin_image1 =  self.bild(weapon1,size= (  185, 163))
        self.skin_image2 =  self.bild(weapon2,size= (  185, 163))
        self.skin_image3 =  self.bild(weapon3,size= (  185, 163))
        self.skin_image4 =  self.bild(weapon4,size= (  185, 163))
        self.skin_image5 =  self.bild(weapon5,size= (  185, 163))
        self.skin_image6 =  self.bild(weapon6,size= (  185, 163))
        self.skin_image7 =  self.bild(weapon7,size= (  185, 163))

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, image=self.skin_image0, text=self.rename(weapon0), compound="top", fg_color="transparent", hover_color="#2FA572")
        self.home_frame_button_1.grid(row=0, column=0, padx=x, pady=y)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, image=self.skin_image1, text=self.rename(weapon1), compound="top", fg_color="transparent", hover_color="#2FA572")
        self.home_frame_button_2.grid(row=0, column=1, padx=x, pady=y)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, image=self.skin_image2, text=self.rename(weapon2), compound="top", fg_color="transparent", hover_color="#2FA572")
        self.home_frame_button_3.grid(row=0, column=2, padx=x, pady=y)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, image=self.skin_image3, text=self.rename(weapon3), compound="top", fg_color="transparent", hover_color="#2FA572")
        self.home_frame_button_4.grid(row=0, column=3, padx=x, pady=y)
        self.home_frame_button_5 = customtkinter.CTkButton(self.home_frame, image=self.skin_image4, text=self.rename(weapon4), compound="top" ,fg_color="transparent", hover_color="#2FA572")
        self.home_frame_button_5.grid(row=1, column=0, padx=x, pady=y)
        self.home_frame_button_6 = customtkinter.CTkButton(self.home_frame, image=self.skin_image5, text=self.rename(weapon5), compound="top", fg_color="transparent", hover_color="#2FA572")
        self.home_frame_button_6.grid(row=1, column=1, padx=x, pady=y)
        self.home_frame_button_6 = customtkinter.CTkButton(self.home_frame, image=self.skin_image6, text=self.rename(weapon6), compound="top", fg_color="transparent", hover_color="#2FA572")
        self.home_frame_button_6.grid(row=1, column=2, padx=x, pady=y)
        self.home_frame_button_6 = customtkinter.CTkButton(self.home_frame, image=self.skin_image7, text=self.rename(weapon7), compound="top", fg_color="transparent", hover_color="#2FA572")
        self.home_frame_button_6.grid(row=1, column=3, padx=x, pady=y)

    
    def random_weapon(self):
        with open(f'code/data/databases/{self.database}.csv',encoding="utf-8") as data: 
            reader = csv.reader(data, delimiter=';') 
            row = random.choice(list(reader))
            return row[1] 

    def bild(self, weapon_name, size):
        with open(f'code/data/databases/all.csv',encoding="utf-8") as data:         #WICHTIG: Realtiven pfad beachten
            reader = csv.reader(data, delimiter=';')                                    #Besserer Suchalgorithmu --> effizienz????
            for row in reader:
                if weapon_name.lower() in row[1].lower():
                    weapon_id = row[0]
                    break
        try:
            res= requests.get(f'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id={weapon_id}&page_num=1&_=1657808768032').json()

            url = res['data']['goods_infos'][f'{weapon_id}']['icon_url']
            
            image = Image.open(requests.get(url, stream=True).raw)

            photo = customtkinter.CTkImage(image, size = size)
        

            return photo
        except:
            image = Image.open(r"D:\Apps\Programmieren\Informatik_unterricht\projekt.betobe\code\data\x.png")
            photo = customtkinter.CTkImage(image, size = size)
            return photo

    def rename(self, name):
            if "StatTrak™" in name:
                rename = name.split("StatTrak™")[1].split("(")[0]
            elif "Souvenir" in name:
                rename = name.split("Souvenir")[1].split("(")[0]
            else:
                rename = name.split("(")[0]

            if len(rename) >= 22:
                rename = rename[:26]
                return rename
            else:
                return rename
