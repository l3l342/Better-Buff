from scripts.api_calls import *
from scripts.frames import *
import customtkinter
import os
from PIL import Image
import asyncio


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        #Window
        self.title("  Better Buff  ")
        self.minsize(1280, 720)
        self.maxsize(1280, 720)
        
        #images
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/")
        
        #Sidebar
        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0, height=720)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(9, weight=1)
        
        self.sidebar_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "banner3.png")), light_image=Image.open(os.path.join(image_path, "banner4.png")), size=(200, 63))  
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, image=self.sidebar_image, text="", fg_color="transparent", hover_color="#2FA572", command=self.home, width=200)
        self.sidebar_button_1.grid(row=0, column=0, padx=20, pady=20)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="tabview", hover_color="#2FA572", command=self.tabview)
        self.sidebar_button_2.grid(row=4, column=0, padx=20, pady=5)

        self.searchbar = customtkinter.CTkEntry(self.sidebar_frame, width=200, placeholder_text="Suche")
        self.searchbar.grid(row=1, column=0, padx=20, pady=(10, 15))
        self.search = customtkinter.CTkButton(self.sidebar_frame, text="Login", command=self.search)
        self.search.grid(row=3, column=0, padx=20, pady=(0, 15))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=10, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                         command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=11, column=0, padx=20, pady=(10, 20))

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        #Tabs
        self.tab_frame = self.tabview = customtkinter.CTkTabview(self, width=1000, height=700)
        self.tabview.grid(row=0, column=1, padx=(12, 10), pady=(10, 10), sticky="nsew")
        self.tabview.add("        Im Trend        ")
        self.tabview.add("        Pistols         ")
        self.tabview.add("        Mid-Tier        ")
        self.tabview.add("        Rifles          ")
        self.tabview.add("        Knives          ")
        self.tabview.add("        Gloves          ")
        self.tabview.add("        Sticker         ")
        self.tabview.tab("        Im Trend        ").grid_columnconfigure(0, weight=1)
        self.tabview.tab("        Pistols         ").grid_columnconfigure(0, weight=1)
        self.tabview.tab("        Mid-Tier        ").grid_columnconfigure(0, weight=1)
        self.tabview.tab("        Rifles          ").grid_columnconfigure(0, weight=1)
        self.tabview.tab("        Knives          ").grid_columnconfigure(0, weight=1)
        self.tabview.tab("        Gloves          ").grid_columnconfigure(0, weight=1)
        self.tabview.tab("        Sticker         ").grid_columnconfigure(0, weight=1)
        

        # create item frame
        self.home_frame = customtkinter.CTkFrame(self.tabview.tab("        Im Trend        "), width=1000, height=700)
        self.home_frame.grid(row=0, column=1, padx=(12, 10), pady=(10, 10), sticky="nsew")
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        frame = Frame(database = "All", home_frame=self.home_frame)
        #pistol tab
        self.home_frame = customtkinter.CTkFrame(self.tabview.tab("        Pistols         "), width=1000, height=700)
        self.home_frame.grid(row=0, column=1, padx=(12, 10), pady=(10, 10), sticky="nsew")
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        frame1 = Frame(database = "Pistols", home_frame=self.home_frame)

        self.home_frame = customtkinter.CTkFrame(self.tabview.tab("        Mid-Tier        "), width=1000, height=700)
        self.home_frame.grid(row=0, column=1, padx=(12, 10), pady=(10, 10), sticky="nsew")
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        frame2 = Frame(database = "Mid-Tier", home_frame=self.home_frame)

        self.home_frame = customtkinter.CTkFrame(self.tabview.tab("        Rifles          "), width=1000, height=700)
        self.home_frame.grid(row=0, column=1, padx=(12, 10), pady=(10, 10), sticky="nsew")
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        frame3 = Frame(database = "Rifles", home_frame=self.home_frame)

        self.home_frame = customtkinter.CTkFrame(self.tabview.tab("        Knives          "), width=1000, height=700)
        self.home_frame.grid(row=0, column=1, padx=(12, 10), pady=(10, 10), sticky="nsew")
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        frame4 = Frame(database = "Knives", home_frame=self.home_frame)

        self.home_frame = customtkinter.CTkFrame(self.tabview.tab("        Gloves          "), width=1000, height=700)
        self.home_frame.grid(row=0, column=1, padx=(12, 10), pady=(10, 10), sticky="nsew")
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        frame5 = Frame(database = "Gloves", home_frame=self.home_frame)

        self.home_frame = customtkinter.CTkFrame(self.tabview.tab("        Sticker         "), width=1000, height=700)
        self.home_frame.grid(row=0, column=1, padx=(12, 10), pady=(10, 10), sticky="nsew")
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        frame6 = Frame(database = "Sticker", home_frame=self.home_frame)


        #Optionen
        self.search.configure(text="Search")
        self.appearance_mode_optionemenu.set("Dark")

   
    #funktionen
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def search_name(self):
        name = self.searchbar.get()
        return print(name)
    
    def search(self):

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/")
        name = self.searchbar.get()
        print("+"+name+"+")

        #customize frame
        skin_name_item=name
        skin_image_item=Frame('All', home_frame=self.home_frame).bild(name,size=( 350, 350))
        graphic_image_item="grafik.jpg" #hier schauenwoher grafik
        pricebuff = Api_call(name).buff()
        print(pricebuff)
        priceskinport = Api_call(name).skinport()
        print(priceskinport)
        pricesteam = Api_call(name).steam()

        self.image_item_frame = customtkinter.CTkFrame(self, width=500, height=700)
        self.image_item_frame.grid(row=0, column=2, padx=(12, 0), pady=(10, 10), sticky="nsew") 
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.skin_image = skin_image_item
        self.skin_image = customtkinter.CTkLabel(self.image_item_frame, text=skin_name_item, font=("tuple", 25), compound="bottom", image=self.skin_image)
        self.skin_image.grid(row=1, column=0, padx=50, pady=(25, 3), sticky="")
        self.grafik_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, graphic_image_item)))
        self.grafik_image = customtkinter.CTkLabel(self.image_item_frame, text="Buff.163 Price History", compound="top", image=self.grafik_image)
        self.grafik_image.grid(row=2, column=0, padx=50, pady=(2, 25), sticky="")
        #item page (right)
        self.data_item_frame = customtkinter.CTkFrame(self, width=500, height=700)
        self.data_item_frame.grid(row=0, column=3, padx=(0, 12), pady=(10, 10), sticky="nsew") 
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.Buff163_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "Buff163logo.png")), size=( 77, 21))
        self.Buff163_image = customtkinter.CTkLabel(self.data_item_frame, text="", image=self.Buff163_image)
        self.Buff163_image.grid(row=0, column=0, padx=100, pady=(135, 5), sticky="nsew")
        self.price_buff163 = customtkinter.CTkButton(self.data_item_frame, text= str(pricebuff) + " €")
        self.price_buff163.grid(row=1, column=0, padx=100, pady=5, sticky="nsew")       
        self.Buff163_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "skinportlogo.png")), size=( 134, 16))
        self.Buff163_image = customtkinter.CTkLabel(self.data_item_frame, text="", image=self.Buff163_image)
        self.Buff163_image.grid(row=2, column=0, padx=100, pady=(100, 5), sticky="nsew")
        self.price_buff163 = customtkinter.CTkButton(self.data_item_frame, text= str(priceskinport) + " €")
        self.price_buff163.grid(row=3, column=0, padx=100, pady=5, sticky="nsew")       
        self.Buff163_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "steamlogo2.png")), size=( 100, 32))
        self.Buff163_image = customtkinter.CTkLabel(self.data_item_frame, text="", image=self.Buff163_image)
        self.Buff163_image.grid(row=4, column=0, padx=100, pady=(100, 5), sticky="nsew")
        self.price_buff163 = customtkinter.CTkButton(self.data_item_frame, text= str(pricesteam) + " €")
        self.price_buff163.grid(row=5, column=0, padx=100, pady=5, sticky="nsew")

        #change frame
        if name == "":
            print("leer")
            #hier message box
        else: 
            self.tab_frame.grid_forget()
            self.home_frame.grid_forget()
            self.image_item_frame.grid(row=0, column=2, padx=(12, 0), pady=(10, 10), sticky="nsew") 
            self.data_item_frame.grid(row=0, column=3, padx=(0, 12), pady=(10, 10), sticky="nsew")

    def tabview(self):
        self.tab_frame.grid_forget()
        self.home_frame.grid_forget()
        self.image_item_frame.grid(row=0, column=2, padx=(12, 0), pady=(10, 10), sticky="nsew") 
        self.data_item_frame.grid(row=0, column=3, padx=(0, 12), pady=(10, 10), sticky="nsew")

    def home(self):
        self.image_item_frame.grid_forget()
        self.data_item_frame.grid_forget()
        self.tabview.grid(row=0, column=1, padx=(12, 10), pady=(10, 10), sticky="nsew")
        self.tabview.set("        Im Trend        ")


if __name__ == "__main__":
    app = App()
    app.mainloop()
