import os
import hashlib

def md5(fname):
    ''' Creates md5sum of a file

    fname: File Name
    '''
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def findAllFilesWithSuffix(suffix):
    ''' Will look for all files with suffix 'suffix' and creates a dictionairy with md5sum to file name + file path mapping

    suffix: suffix to look for
    '''
    d = dict()
    for root, dirs, files in os.walk(r".", topdown = True):
        for name in files:
            if name[-len(suffix):] == suffix:
                hashValue = md5(os.path.join(root, name))
                if hashValue not in d:
                    d[hashValue] = [(name, os.path.join(root))]
                else:
                    d[hashValue].append([(name, os.path.join(root))])
    return d

def findDuplicateFiles(suffix):
    d = findAllFilesWithSuffix(suffix)
    for key, value in d.items():
        if len(value) > 1:
            print(value)

findDuplicateFiles('py')