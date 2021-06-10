import base64
import json
import requests
import os


def sendFile(filePath):
    api = 'http://127.0.0.1:5000/login'

    status = 'not send'

    files = {'upload_file': open(filePath, 'rb')}

    uslessPath = ''
    fullPath = ''

    index = 0

    while True:

        uslessPath += filePath[index]

        index += 1

        if uslessPath == '../assets/clientDisc/':
            fullPath = filePath[index:]
            break

    response = requests.post(api, files=files, data={
                             'path': fullPath})

    try:
        status = 'success'
        return ('success', response)
    except:
        status = 'error'
        return ('error', response)

    sendFile('../assets/clientDisc/jhony.png')
