import datetime
import requests
import json
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




URL='https://api.nasa.gov/planetary/apod'

headers = {
    'api_key' : key,
}

class DaylyFile:

    def __init__(self):
        self.body = None
        self.title = None
        self.url = None
        self.hdurl = None
        self.copyright = None
        self.date = None
        self.text = None
        self.fulldate = None
        self.media_type = None


    ### Methods to get data

    def getBody(self):
        r = requests.get(URL,headers).json()
        self.body = r
        return r

    def getTitle(self):
        self.title = self.body["title"]
    
    def getUrl(self):
        self.url = self.body["url"]
    
    def getHdurl(self):
        self.url = self.body["hdurl"]
    
    def getCopyright(self):
        self.copyright = self.body["copyright"]

    def getDate(self):
        self.date = self.body["date"]
        date = self.date.split('-')
        d = datetime.date(int(date[0]),int(date[1]),int(date[2]))
        self.fulldate = d.strftime("%A %w %B %Y") #Jour NumeroDuJour Mois NumeroDelAnnee

    def getText(self):
        self.text = self.body["explanation"]
    
    def getMediaType(self):
        self.media_type = self.body["media_type"]
    
    def getMetadata(self):
        self.getBody()
        self.getTitle()
        self.getUrl()
        self.getDate()
        self.getText()
        self.getMediaType()
        if "copyright" in self.body.keys():
            self.getCopyright()
        if "hdurl" in self.body.keys():
            self.getHdurl()


    ##### Method to use data

    def showBody(self):
        print(json.dumps(self.getBody(),indent=4))
        #print(json.dumps(self.body,indent=4))
    
    
    def save_img(self):
        if self.media_type == "image":
            img_data = requests.get(self.url).content
            date = self.date.split('-')
            date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
            date = date.strftime("%B-%d")
            img_name = date + "_" + self.title
            with open(f"/Users/nathan/Pictures/NASA/{img_name}.jpg", 'wb') as f:
                f.write(img_data)
        else:
            print("Le média n'est pas une image !")
            print("\nLa sauvegarde n'a pas eu lieu.")
        return


class Email:
    
    def __init__(self,sender,receiver):
        self.sender = sender
        self.receiver = receiver
        self.html_text = None
        self.plain_text = None



    def writeMsg(self,img: DaylyFile):
        message = MIMEMultipart("alternative")
        message["Subject"] = f"[Space\'s Picture] Enjoy your day {self.receiver['name']} !"
        message["From"] = self.sender
        message["To"] = self.receiver['email']
        
        # plain text is the same for all medi types
        self.plain_text = f'''
        {img.title}
        {img.fulldate}
        The file can't be shown. Sorry !
        {img.text}
        '''

        if img.media_type == "image":
            if img.copyright != None:
                self.html_text = f'''
                <html>
                <body>
                <p><strong><span style="font-family: helvetica; font-size: x-large;">{img.title}</span></strong></p>
                <p><span style="font-family: &quot;book antiqua&quot;, palatino;">{img.fulldate}</span></p>
                <p>&nbsp;</p>
                <p style="text-align: justify;"><span style="font-family: verdana, geneva;">{img.text}</span></p>
                <p>&nbsp;</p>
                <p><img style="vertical-align: middle; horizontal-align: middle;" src={img.url} alt="Image description" width="720" height="500" /></span></p>
                <p><em>&copy;{img.copyright}</em></p>
                <p>&nbsp;</p>
                </body>
                </html>
                '''
            else:
                self.html_text = f'''
                <html>
                <body>
                <p><strong><span style="font-family: helvetica; font-size: x-large;">{img.title}</span></strong></p>
                <p><span style="font-family: &quot;book antiqua&quot;, palatino;">{img.fulldate}</span></p>
                <p>&nbsp;</p>
                <p style="text-align: justify;"><span style="font-family: verdana, geneva;">{img.text}</span></p>
                <p>&nbsp;</p>
                <p><img style="vertical-align: middle; horizontal-align: middle;" src={img.url} alt="Image description" width="720" height="500" /></span></p>
                <p>&nbsp;</p>
                </body>
                </html>
                '''
        
        if img.media_type != "image":
            self.html_text = f'''
            <html>
            <body>
            <p><strong><span style="font-family: helvetica; font-size: x-large;">{img.title}</span></strong></p>
            <p><span style="font-family: &quot;book antiqua&quot;, palatino;">{img.fulldate}</span></p>
            <p>&nbsp;</p>
            <p style="text-align: justify;"><span style="font-family: verdana, geneva;">{img.text}</span></p>
            <p>&nbsp;</p>
            <p><a href={img.url}> Link of today's media </a></p>
            <p>&nbsp;</p>
            </body>
            </html>
            '''

        message.attach(MIMEText(self.plain_text, 'plain'))
        message.attach(MIMEText(self.html_text, 'html'))

        return message



class ServerMail:


    def __init__(self, smtp_server, smtp_port):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.context = ssl.create_default_context()
        self.server = None
    

    def initiate(self,email, pwd):
        self.server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port,context=self.context)
        self.server.connect(self.smtp_server,self.smtp_port)
        self.server.login(email,pwd)


    def sendEmail(self, message: MIMEMultipart, sender, receiver):
        self.server.sendmail(sender, receiver['email'], message.as_string())
        print(f"Message send to {receiver['name']}!")
    

    def quit(self):
        self.server.quit()


