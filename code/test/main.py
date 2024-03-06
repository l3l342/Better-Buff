import tkinter
import customtkinter
import os
from PIL import Image
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #Window
        self.title("  Better Buff  ")
        self.minsize(1200, 720)
        self.maxsize(1200, 720)

        #Sidebar
        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0, height=720)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text=" Better Buff ", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.home)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.tabview)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.home_image = customtkinter.CTkImage(dark_image=Image.open(("/Users/ben/Developer/projekt.betobe/code/data/logo_klein.png")), size=(20, 20))



        #Tabs
        self.tabview = customtkinter.CTkTabview(self, width=980, height=690)
        self.tabview.grid(row=0, column=14, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("        Im Trend        ")
        self.tabview.add("        Mid-Tier        ")
        self.tabview.add("        Rifles          ")
        self.tabview.add("        Knives          ")
        self.tabview.add("        Gloves          ")
        self.tabview.add("        Cases           ")
        self.tabview.add("        Collections     ")
        self.tabview.add("        Sticker         ")
        self.tabview.add("        Other           ")

        self.tabview.tab("        Im Trend        ").grid_columnconfigure(0, weight=1)
        self.tabview.tab("        Mid-Tier        ").grid_columnconfigure(0, weight=1)
        self.tabview.tab("        Rifles          ").grid_columnconfigure(0, weight=1)
        self.tabview.tab("        Knives          ").grid_columnconfigure(0, weight=1)
        self.tabview.tab("        Gloves          ").grid_columnconfigure(0, weight=1)
        self.tabview.tab("        Cases           ").grid_columnconfigure(0, weight=1)
        self.tabview.tab("        Collections     ").grid_columnconfigure(0, weight=1)
        self.tabview.tab("        Sticker         ").grid_columnconfigure(0, weight=1)
        self.tabview.tab("        Other           ").grid_columnconfigure(0, weight=1)

        #lol
        self.label_tab_1 = customtkinter.CTkLabel(self.tabview.tab("        Im Trend        "), text="Pistols")
        self.label_tab_1.grid(row=0, column=0, padx=20, pady=20)       
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("        Mid-Tier        "), text="Mid-Tier")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("        Rifles          "), text="Rifles")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("        Knives          "), text="Knives")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("        Gloves          "), text="Gloves")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("        Cases           "), text="Cases")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("        Collections     "), text="Collections")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("        Sticker         "), text="Sticker")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("        Other           "), text="Other")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

#item page (left)
        skin_name_item="AK-47 | Redline (Field-Tested)"
        skin_image_item="/Users/ben/Developer/projekt.betobe/code/data/akak.png"
        graphic_image_item="/Users/ben/Developer/projekt.betobe/code/data/grafik.jpg"
        pricebuff = "100.00"
        priceskinport = "119.99"
        pricesteam = "520.21"
        self.image_item_frame = customtkinter.CTkFrame(self, width=500, height=700)
        self.image_item_frame.grid(row=0, column=2, padx=(12, 0), pady=(10, 10), sticky="nsew") 
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.skin_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, skin_image_item)), size=( 350, 350))
        self.skin_image = customtkinter.CTkLabel(self.image_item_frame, text=skin_name_item, font=("tuple", 25), compound="bottom", image=self.skin_image)
        self.skin_image.grid(row=1, column=0, padx=50, pady=(25, 3), sticky="")
        self.grafik_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, graphic_image_item)), size=( 500, 250))
        self.grafik_image = customtkinter.CTkLabel(self.image_item_frame, text="Buff.163 Price History", compound="top", image=self.grafik_image)
        self.grafik_image.grid(row=2, column=0, padx=50, pady=(2, 25), sticky="")

        #item page (right)
        self.data_item_frame = customtkinter.CTkFrame(self, width=500, height=700)
        self.data_item_frame.grid(row=0, column=3, padx=(0, 12), pady=(10, 10), sticky="nsew") 
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.Buff163_image = customtkinter.CTkImage(dark_image=Image.open( "/Users/ben/Developer/projekt.betobe/code/data/Buff163logo.png"), size=( 77, 21))
        self.Buff163_image = customtkinter.CTkLabel(self.data_item_frame, text="", image=self.Buff163_image)
        self.Buff163_image.grid(row=0, column=0, padx=100, pady=(135, 5), sticky="nsew")
        self.price_buff163 = customtkinter.CTkButton(self.data_item_frame, text= pricebuff + " ¥")
        self.price_buff163.grid(row=1, column=0, padx=100, pady=5, sticky="nsew")       
        self.Buff163_image = customtkinter.CTkImage(dark_image=Image.open( "/Users/ben/Developer/projekt.betobe/code/data/Buff163logo.png"), size=( 134, 16))
        self.Buff163_image = customtkinter.CTkLabel(self.data_item_frame, text="", image=self.Buff163_image)
        self.Buff163_image.grid(row=2, column=0, padx=100, pady=(100, 5), sticky="nsew")
        self.price_buff163 = customtkinter.CTkButton(self.data_item_frame, text= priceskinport + " €")
        self.price_buff163.grid(row=3, column=0, padx=100, pady=5, sticky="nsew")       
        self.Buff163_image = customtkinter.CTkImage(dark_image=Image.open("/Users/ben/Developer/projekt.betobe/code/data/steamlogo2.png"), size=( 100, 32))
        self.Buff163_image = customtkinter.CTkLabel(self.data_item_frame, text="", image=self.Buff163_image)
        self.Buff163_image.grid(row=4, column=0, padx=100, pady=(100, 5), sticky="nsew")
        self.price_buff163 = customtkinter.CTkButton(self.data_item_frame, text= pricesteam + " €")
        self.price_buff163.grid(row=5, column=0, padx=100, pady=5, sticky="nsew")

        #Optionen
        self.appearance_mode_optionemenu.set("Dark")
        self.image_item_frame.grid_forget()
        self.data_item_frame.grid_forget()
   
    #funktionen
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

        

    def search(self):
        search = self.searchbar.get()
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

