import asyncio
import websockets
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

async def hello(websocket, path):
    while True:
        data = await websocket.recv()
        if "Temperature high" in data or "Humidity high" in data or "PM2.5 high" in data:
            print('NOOOOOOOOOOOOOO\n')
            send_email(data)

async def send_email(message):
    email = "homatthew123456789@gmail.com"  # 你的 Gmail 郵箱地址
    password = "ggmm123456789"  # 你的 Gmail 密碼

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = "Arduino 警告"

    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(email, password)
    server.sendmail(email, email, msg.as_string())
    server.quit()

start_server = websockets.serve(hello, "127.0.0.1", 8888)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
