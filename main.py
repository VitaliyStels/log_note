from datetime import datetime
import os

now = datetime.now()
filename = 'db.md'
if os.path.exists(filename):
    with open(filename, 'r') as file:
        print(file.read())

while True:
    message = input()
    logMessage = f'{now:%D %H:%M }{message}'

    with open(filename, 'a') as file:
        print(logMessage, file=file)
