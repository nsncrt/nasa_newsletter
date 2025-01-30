from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotmap import DotMap

from .nasafile import NasaFile



class Email:
    
    def __init__(self, sender_email: str, receiver_info: DotMap) :
        self.sender_email = sender_email
        self.receiver_info = receiver_info
        self.html_text = None
        self.plain_text = None
        self.content = None

    def writeMsg(self, img: NasaFile):
        message = MIMEMultipart("alternative")
        message["Subject"] = f"[Space\'s Picture] Enjoy your day {self.receiver_info['name']} !"
        message["From"] = self.sender_email
        message["To"] = self.receiver_info['email']
        # -- Plain text for every cases --
        self.plain_text = f'''
        {img.title}
        {img.strdate}
        The file can't be shown. Sorry !
        {img.text}
        '''
        # -- If the media is an image --
        if img.media_type == "image":
            # -- If there is a copyright --
            if img.copyright != None:
                self.html_text = f'''
                <html>
                <body>
                <p><strong><span style="font-family: helvetica; font-size: x-large;">{img.title}</span></strong></p>
                <p><span style="font-family: &quot;book antiqua&quot;, palatino;">{img.strdate}</span></p>
                <p>&nbsp;</p>
                <p style="text-align: justify;"><span style="font-family: verdana, geneva;">{img.text}</span></p>
                <p>&nbsp;</p>
                <p><img style="vertical-align: middle; horizontal-align: middle;" src={img.url} alt="Image description" width="720" height="500" /></span></p>
                <p><em>&copy;{img.copyright}</em></p>
                <p>&nbsp;</p>
                </body>
                </html>
                '''
            # -- If there is no copyright --
            else:
                self.html_text = f'''
                <html>
                <body>
                <p><strong><span style="font-family: helvetica; font-size: x-large;">{img.title}</span></strong></p>
                <p><span style="font-family: &quot;book antiqua&quot;, palatino;">{img.strdate}</span></p>
                <p>&nbsp;</p>
                <p style="text-align: justify;"><span style="font-family: verdana, geneva;">{img.text}</span></p>
                <p>&nbsp;</p>
                <p><img style="vertical-align: middle; horizontal-align: middle;" src={img.url} alt="Image description" width="720" height="500" /></span></p>
                <p>&nbsp;</p>
                </body>
                </html>
                '''
        # -- If the media is not an image --
        if img.media_type != "image":
            self.html_text = f'''
            <html>
            <body>
            <p><strong><span style="font-family: helvetica; font-size: x-large;">{img.title}</span></strong></p>
            <p><span style="font-family: &quot;book antiqua&quot;, palatino;">{img.strdate}</span></p>
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
        self.content = message
