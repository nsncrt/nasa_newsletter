from send_newsletter import DaylyFile, Email, ServerMail
import json
import csv


### configuration
with open('config.json') as json_file:
    config = json.load(json_file)
smtp_server = config['smtp_server']
smtp_port = config['smtp_port']
sender = config['email']


### image stuff
img = DaylyFile()
img.showBody()
img.getMetadata()
img.save_img()


### server stuff
server=ServerMail(smtp_server,smtp_port)
server.initiate(sender,config['pwd'])

### mailing list gestion
with open('mailing_list.csv', newline='') as csvfile:
    receivers = csv.DictReader(csvfile, delimiter=',')
    for receiver in receivers: #receiver est le dico json de la ligne itérée
        mail = Email(sender, receiver)
        message = mail.writeMsg(img)
        server.sendEmail(message,sender,receiver)

### end server
server.quit()