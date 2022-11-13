
SMTPserver = 'smtp.gmail.com:587'
sender =     'gestordedocumentospessoais@gmail.com'
destination = ['edilsonclaudinosilva@gmail.com']

USERNAME = "gestordedocumentospessoais@gmail.com"
PASSWORD = "@Gestor2021"

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'


content="""\
Test message
"""

subject="Sent from Python"

import sys
import os
import re

from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

# old version
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText

try:
    msg = MIMEText(content, text_subtype)
    msg['Subject']=       subject
    msg['From']   = sender # some SMTP servers will do this automatically, not all

    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)
    conn.login(USERNAME, PASSWORD)
    try:
        conn.sendmail(sender, destination, msg.as_string())
    finally:
        conn.quit()

except:
    sys.exit( "mail failed; %s" % "CUSTOM_ERROR" ) # give an error message



'''

import smtplib
import email.message

def enviar_email(): 
    corpo_email = 
    <p>Parágrafo1</p>
    <p>Parágrafo2</p>
  

    msg = email.message.Message()
    msg['Subject'] = 'Assunto'
    msg['From'] = 'gestordedocumentospessoais@gmail.com'
    msg['To'] = 'edilsonclaudinosilva@gmail.com'
    password = '@Gestor2021'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
'''