import re #Імпортуємо потрібний модуль

def subscribe(): #Створюємо ункцію для подальшого виклику
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+') #Створюємо вираз для перевірки правильності введення email
    a='y'
    while True:

        emailfile = open('emails.txt', 'r+' ) #Відкривваємо файл для читання та запису в кінець

        if a == 'y': #Якщо так, то
            email = input('Enter your email address: ') #Просимо користувача ввести пароль
            print(email) #Виводимо введений пароль в консоль

            if re.fullmatch(regex, email): #Перевіряємо правильність введення
                if email not in emailfile.read(): #Перевіряємо чи знаходиться email в БД(файлі), якщо ні, то
                    emailfile.write(email + '\n') #Записуємо email в файл
                    emailfile.close()  #Закриваємо файл

                else:  #Якщо email є в файлі
                    print("Your email address is already in the database.") #Виводимо повідомлення про помилку

            else: 
                print('Invalid email address') #Виводимо, якщо неправильно введений email

        elif a == 'n': #При натисканні n, 
            break #Виводимо з циклу
        
        else: #При натисненні будь-якої іншої кнопки
            print('Invalid input, try again.') #Виводимо повідомлення помилки та просимо ввести знову

        a = input("Do you want to continue entering your email address? (y/n): ") #Перевіряємо потрібно вводити email чи ні

if __name__ == '__main__': #Перевіряємо чи наш додаток запускається саме з цього файлу, в інших випадках буде запущений під час виклику
    subscribe()