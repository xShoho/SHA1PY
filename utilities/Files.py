import os

def filesFromDir(path):
    files = []
    
    for (dirpath, dirnames, filenames) in os.walk(path):
        for file in filenames:
            files.append(os.path.join(os.sep, path, file))
        break
    
    return files

def filenamesFromDir(path):
    files = []
    
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break
    
    return files


def dirsFromDir(path):
    dirs = []
    
    for (dirpath, dirnames, filenames) in os.walk(path):
        for dir in dirnames:
            dirs.append(os.path.join(os.sep, path, dir))
        break
    
    return dirs