#
# filename    : lab-135-send-email-smtp.py
# Description :
# Docs        :
#               * https://docs.python.org/3/library/string.html
#               * https://docs.python.org/3/library/datetime.html
# Requirements:
#               *
#

from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('file-14-template-html.html', 'r') as html:
    template = Template(html.read())
    dt_now = datetime.now().strftime('%d/%m/%Y')
    content = template.safe_substitute(name='Josemar F. A. Silva', data=dt_now)

    msg = MIMEMultipart()
    msg['from'] = 'Josemar Furegatti de Abreu Silva'
    msg['to'] = 'josemarsilva@yahoo.com.br'
    msg['subject'] = 'Este email foi enviado pelo sendmail do python'

    body = MIMEText(content, 'html')
    msg.attach(body)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        str_email_login = 'my_gmail_account@gmail.com'
        str_email_password = 'my_gmail_password'
        smtp.login(str_email_login, str_email_password)
        smtp.send_message(msg)
        print('Email enviado com sucesso!')
