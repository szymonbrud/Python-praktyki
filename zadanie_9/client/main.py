import filecmp
import os
import md5hash
import hashlib
import json
import time

from fileMenage import fileSave, checkFileStatus


discPath = '../assets/clientDisc'
fakeDiscPath = '../assets/clientFakeVirtualDisc'


while(True):
    print('Check files')
    checkFileStatus(discPath)
    time.sleep(3)
