from datetime import datetime
import settings
import os

now = datetime.now()
fileCredentials = f'{settings.fileName}.{settings.fileExtension}'
filePath = f'data/{fileCredentials}'

if os.path.exists(filePath):
    with open(filePath, 'r') as file:
        print(file.read())
        file.close()

while True:
    message = input()
    
    if settings.indentCommand in message:
        messageText = message[3:]
        logMessage = f'{now:%D %H:%M } - {messageText}'

        with open(filePath, 'a') as file:
            print(logMessage, file=file)
            file.close()
    else:
        logMessage = f'{now:%D %H:%M }{message}'
    
        with open(filePath, 'a') as file:
            print(logMessage, file=file)
            file.close()


    if settings.changeFileNameCommand in message:                        #CHANGE FILE NAME
        command, newName = message.split()
    

       

    
