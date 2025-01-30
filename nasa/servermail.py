import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from dotmap import DotMap



class ServerMail:

    def __init__(self, smtp_server, smtp_port):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.context = ssl.create_default_context()

    def sendEmail(self, message: MIMEMultipart, sender_info: DotMap, receiver_email: str):
        try :
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=self.context) as server:
                server.connect(self.smtp_server,self.smtp_port)
                server.login(sender_info.email, sender_info.pwd)
                server.sendmail(sender_info.email, receiver_email, message.as_string())
            print(f"Message successfully send to {receiver_email}!")
        except Exception as e:
            print(f"Error__: {e}")