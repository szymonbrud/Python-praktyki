import json
import os
import hashlib

import sendFile as sendFileToBackend

fileStatus = ['nosend', 'sending', 'sended']
[nosend, sending, sended] = fileStatus

allFilesPath = []


def fileSave():
    print("file save!")


def sendFile(arrayOfFilePathsToSend, path):
    fileExistInFileStatus = []
    filesNew = []

    a_file = open(path + '/fileStatuses.json', "r")
    json_object = json.load(a_file)
    a_file.close()

    for index, pathFile in enumerate(arrayOfFilePathsToSend):

        isInside = False

        for fileStatusFromJson in json_object['lastFileChange']:
            if fileStatusFromJson['path'] == pathFile:
                isInside = True

        if isInside:
            fileExistInFileStatus.append((pathFile, index))
        else:
            filesNew.append(pathFile)

    for filePathExisedElement, index in fileExistInFileStatus:
        fileName = os.path.basename(filePathExisedElement)
        fileTime = os.stat(path + '/' + filePathExisedElement).st_mtime

        json_object['lastFileChange'][index] = {'name': fileName, 'path': filePathExisedElement,
                                                'lastChange': fileTime, 'status': sending}

        with open(path + '/fileStatuses.json', 'w') as f:

            json.dump(json_object, f,  indent=2)

        res = sendFileToBackend.sendFile(path + '/' + filePathExisedElement)

        print(fileName + ': ' + res[0])

    for filePathNewElement in filesNew:
        fileName = os.path.basename(filePathNewElement)
        fileTime = os.stat(path + '/' + filePathNewElement).st_mtime

        json_object['lastFileChange'] = json_object['lastFileChange'] + \
            [{'name': fileName, 'path': filePathNewElement,
              'lastChange': fileTime, 'status': sending}]

        with open(path + '/fileStatuses.json', 'w') as f:

            json.dump(json_object, f,  indent=2)

        res = sendFileToBackend.sendFile(path + '/' + filePathNewElement)

        print(fileName + ': ' + res[0])


def getAllFilesPaths(path, mainPath, isFirst=False):

    global allFilesPath

    if isFirst:
        allFilesPath = []

    filesName = os.listdir(mainPath if isFirst else mainPath + '/' + path)

    filesPath = []

    for fileName in filesName:
        isFoler = True
        for fileLetter in fileName:
            if fileLetter == ".":
                isFoler = False

        if isFoler == False:
            allFilesPath.append(fileName if isFirst else path + '/' + fileName)
            filesPath.append(fileName if isFirst else path + '/' + fileName)

        elif len(os.listdir(mainPath + '/' + fileName if isFirst else mainPath + '/' + path + '/' + fileName)) == 0 and path != '../assets/clientDisc':
            allFilesPath.append(path)

        else:
            filesPath.append(getAllFilesPaths(
                fileName if isFirst else path + '/' + fileName, mainPath)[0])

    return allFilesPath


def getArrayOfNewAndUpdatedFiles(fileChanges, allFilesPaths, path):

    resolut = []

    for pathFile in allFilesPath:
        isFileUpToDate = False

        for fileChange in fileChanges:
            if pathFile == fileChange['path']:
                fileTime = os.stat(path + '/' + pathFile).st_mtime
                if fileTime == fileChange['lastChange']:
                    isFileUpToDate = True

        if isFileUpToDate == False:
            resolut.append(pathFile)

    return resolut


def filterByBlackList(arrayToFilter, filter):
    resoult = []

    for filteredElement in arrayToFilter:
        isBlackElement = False
        for filterE in filter:
            if filteredElement == filterE:
                isBlackElement = True

        if isBlackElement == False:
            resoult.append(filteredElement)

    return resoult


def checkFileStatus(path):

    allFilesPath = []
    allFilesPaths = getAllFilesPaths(path, path, True)

    try:
        fileSettings = open(path + '/fileStatuses.json', 'r')
        fileSettingsJson = json.load(fileSettings)

        fileChanges = fileSettingsJson['lastFileChange']

        newAndUpdatedFilesPaths = getArrayOfNewAndUpdatedFiles(
            fileChanges, allFilesPaths, path)

        newAndUpdatedFilesPaths = filterByBlackList(
            newAndUpdatedFilesPaths, ['fileStatuses.json'])

        sendFile(newAndUpdatedFilesPaths, path)

    except(EOFError):
        print('During read file settings got err!')
        print(EOFError)
