import requests
from tkinter import *
from PIL import Image, ImageTk

res= requests.get('https://buff.163.com/api/market/goods/buy_order?game=csgo&goods_id=35650&page_num=1&_=1657808768032').json()

def api_call(res):
    for price in res['data']['items']:
        url = price['icon_url']
        return url  
    

root = Tk()

# laden bild + resize
image = Image.open(requests.get(api_call(res), stream=True).raw).resize((1000,1000))

photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.pack()

root.mainloop()