#Підключаємо потрібні для роботи бібліотеки(функції)
import subscribe
import main
import smtplib
from datetime import datetime, date
from email.mime.text import MIMEText

def email_sending():
    emailfile = open('emails.txt', 'r' )#Відкриваємо файл для читання

    emails = emailfile.read() #Зчитуємо дані, записуємо в змінну
    to_email = emails.replace('\n', ' ').split(' ') #Переведення отриманих даних в список
    if not to_email[-1]: #Якщо останній рядок в списку пустий, то
        to_email.pop() #Видаляємо його
    emailfile.close() #Закриваємо файл
    
    l = [] #Створюємо список для невдалих emails

    for i in to_email: #Проходимось по всіх email у файлі
        try: #Пробуємо відправити повідомлення
            server.sendmail('kosovanchik1208@gmail.com',i ,msg.as_string() ) #Відправляємо повідомлення
            print(f'Successfully sent mail to {i}') #Виведення повідомлення у разі вдалої відправки повідомлення на email
        except: #У разі невдачі, 
            l.append(i+'\n') #записуємо email в список
            print(f'Unable to send to "{i}" email.') #Повідомлення про помилку

    emailfile = open('emails.txt', 'w' ) #Відкриваємо файл для запису

    emailfile.writelines(l) #Записуємо невдалі emails

    emailfile.close() #Закриваємо файл
            
    server.quit() #Завершаємо роботу з сервером, виходимо з нього

#Записуємо поточну дату та час
now = datetime.now()
today = date.today()

#Конвертуємо в потрібний нам формат дати та часу
current_time = now.strftime("%H:%M:%S")
d = today.strftime("%B %d, %Y")

message = f"Time: {current_time}, {d}. 1 BTC = {main.UAH} UAH." #Повідомлення, яке буде відправлено

server = smtplib.SMTP('smtp.gmail.com: 587') #Підключаємо сервер gmail.com

server.starttls() #Починаємо роботу з ним
server.login('kosovanchik1208@gmail.com', 'ygbsvictksxctrif') #Email з якого буде відправлено повідомлення

msg = MIMEText(message) #Конвертація повідомлення в об'єкт MIME
msg['Subject'] = 'BTC exchange rate in UAH' #Тема повідомлення

while True:
    a = input("Do you want to enter your email address? (y/n): ") #Перевірка необхідності введення email адреси

    if a== 'y': 
        subscribe.subscribe() #Викликаємо функцію з файлу subscribe 
        email_sending()
        break #Виходимо з циклу

    elif a  == 'n':
        email_sending()
        break #Виходимо з циклу

    else: 
        print('Invalid input.') #Повідомлення про помилку