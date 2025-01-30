import json
import csv

from dotmap import DotMap

from nasa.nasafile import NasaFile
from nasa.emailwriting import Email
from nasa.servermail import ServerMail



# -- Config --
with open('config.json') as json_file:
    config = DotMap(json.load(json_file))

# -- Image initialisation --
img = NasaFile(config.api.url, config.api.key)
img.computeMetadata()
img.ShowBody()
# img.SaveImgLocally()

# -- Server initialisation --
server = ServerMail(config.smtp.server,config.smtp.port)

# -- Mailing list gestion and send email --
with open('data/mailing_list.csv', newline='') as csvfile:
    receivers = csv.DictReader(csvfile, delimiter=',')
    for receiver_info in receivers:
        mail = Email(config.sender.email, receiver_info)
        mail.writeMsg(img)
        server.sendEmail(mail.content, config.sender, receiver_info["email"])