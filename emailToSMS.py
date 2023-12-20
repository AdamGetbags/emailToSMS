# -*- coding: utf-8 -*-
"""
Email to SMS Gateway - send SMS
@author: adam getbags
"""

import smtplib
from email.message import EmailMessage
from emailToSMSConfig import senderEmail, gatewayAddress, appKey

msg = EmailMessage()
msg.set_content('lets get a bag.')

msg['From'] = senderEmail # 'email@address.com'
msg['To'] = gatewayAddress  # '1112223333@vmobl.com'
msg['Subject'] = 'Finance Family'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(senderEmail, appKey)

server.send_message(msg)
server.quit()
