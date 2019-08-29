import os
import smtplib
import email.mime.text
import time

import dotenv

dotenv.load_dotenv()

COUNTER = 0
DONE = False

def search_warning(line):
    data, level, filename, message = line.split('|')
    if 'WARNING' in level and 'Falha na autenticação' in message:
        return True
    return False

def clear_log(filename):
    with open(filename, 'w') as f:
        pass

def send_mail():
    smtp= smtplib.SMTP()
    
    server = 'smtp.gmail.com'
    port = 587

    user = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    smtp.connect(server, port)
    smtp.starttls()
    smtp.ehlo()
    smtp.login(user, password)

    message = 'Usuário bloqueado por tentativas de acesso inválidas'

    mail = email.mime.text.MIMEText(message, 'html')

    mail.set_charset('utf-8')

    mail['From'] = user
    mail['To'] = 'luuhricciardi@gmail.com'
    mail['Subject'] = 'Aviso ao Administrador'

    smtp.sendmail(
        user,
        'luuhricciardi@gmail.com',
        mail.as_string()
    )
     
while not DONE:

    with open('app.log', 'r') as f:
        for line in f.readlines():
            try:
                if search_warning(line.strip()):
                    COUNTER = COUNTER + 1
            except Exception:
                pass
            print(COUNTER)
            if COUNTER == 3:
                send_mail()
                COUNTER = 0

    clear_log('app.log')
    time.sleep(1.0)