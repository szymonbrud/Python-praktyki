from flask import Flask, jsonify, request
import os
import base64
from PIL import Image
import io
import numpy as np


app = Flask(__name__)

mainPathToSaveFolder = './disc'


@app.route('/hello')
def hello():
    return "Hello Client!"


@app.route('/upload', methods=["POST"])
def upload():
    print(request)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        f = request.files['upload_file']

        path = request.form['path']

        splitedPath = path.split('/')

        currentPath = ''

        for index, splitedPathElement in enumerate(splitedPath):
            if index == len(splitedPath) - 1:
                if currentPath == '':
                    f.save(os.path.join(
                        mainPathToSaveFolder, f.filename))
                else:
                    print('TUTAJ')
                    print(currentPath)
                    f.save(
                        mainPathToSaveFolder + '/' + currentPath + '/' + f.filename)
            else:
                if currentPath == '':
                    currentPath += splitedPathElement
                else:
                    currentPath += '/'
                    currentPath += splitedPathElement
                print('here')
                print(currentPath)
                print(splitedPathElement)
                if os.path.exists(mainPathToSaveFolder + '/' + currentPath) == False:
                    os.mkdir(mainPathToSaveFolder + '/' + currentPath)

        print(splitedPath)

        return "passed"
    else:
        return "not passed"


if __name__ == "__main__":
    app.run(debug=True)
