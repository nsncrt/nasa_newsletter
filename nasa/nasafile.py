import datetime
import requests
import json



class NasaFile:
    
    def __init__(self, url_api_nasa: str, api_key: str):
        # --- Everytime ---
        r = requests.get(url=url_api_nasa, params={"api_key": api_key}).json()
        self.body = r
        self.title = r["title"]
        self.text = r["explanation"]
        self.media_type = r["media_type"]
        # --- To compute ---
        self.url = None
        self.copyright = None
        self.date = None
        self.strdate = None

    # --- Methods to compute all metadata ---
    def Url(self):
        if "hdurl" in self.body.keys():
            self.url = self.body["hdurl"]
        else:
            self.url = self.body["url"]

    def Copyright(self):
        if "copyright" in self.body.keys():
            self.copyright = self.body["copyright"]

    def Date(self):
        d = self.body["date"].split('-')
        self.date = datetime.date(int(d[0]),int(d[1]),int(d[2]))

    def StrDate(self):
        self.strdate = self.date.strftime("%A %d %B %Y") #Thursday 4 January 2025

    def computeMetadata(self):
        self.Url()
        self.Copyright()
        self.Date()
        self.StrDate()

    # --- Methods to use data of the object ---
    def ShowBody(self):
        print(json.dumps(self.body,indent=4))
    
    def SaveImgLocally(self):
        if self.media_type == "image":
            img_data = requests.get(self.url).content
            img_name = self.date.strftime("%Y%m%d") + "_" + self.title
            with open(f"img/{img_name}.jpg", 'wb') as f:
                f.write(img_data)
            print("L'image a bien été sauvegardée !")
        else:
            print("Le média n'est pas une image !\nLa sauvegarde n'a pas eu lieu.")