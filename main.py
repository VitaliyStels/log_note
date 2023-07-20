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
    
    if settings.changeFileNameCommand in message:                        #CHANGE FILE NAME
        command, newName = message.split()
    

    logMessage = f'{now:%D %H:%M }{message}'

    with open(filePath, 'a') as file:
        print(logMessage, file=file)
        file.close()

    
