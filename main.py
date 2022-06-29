import sys
import os
from utilities.Hash import hashFile
from utilities.Files import dirsFromDir, filesFromDir, filenamesFromDir

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def main(dirPath):
    shaKeys = []
    filenames = filenamesFromDir(dirPath)
    linesToWrite = []

    for file in filesFromDir(dirPath):
        shaKeys.append(hashFile(file))
        
    for i in range(0, len(shaKeys)):
        print(f'{ colored(0, 255, 0, f"filename: { filenames[i] }") } { colored(200, 200, 200, f"sha-1: { shaKeys[i] }") }')
        linesToWrite.append(f'{ filenames[i] }.com;{shaKeys[i]}\n')

    return linesToWrite


def saveToFile(linesToWrite):
    resFile = open("results.txt", "a+")
        
    for line in linesToWrite:
        resFile.write(line)
        
    print(colored(0, 100, 255, f"Wrote to file: { os.path.realpath(resFile.name) }"))    
    
    resFile.close()


def recursive():
    try:
        dirPath = os.path.dirname(sys.argv[2])
        dirs = dirsFromDir(dirPath)
        linesToWrite = main(dirPath)
            
        for dir in dirs:
            linesToWrite += main(dir)
                
        saveToFile(linesToWrite)
        
    except Exception as e:
        print(colored(255, 0, 0, f"Error: { e }"))
    

def noRecursive():
    try:
        dirPath = os.path.dirname(sys.argv[1])
        
        linesToWrite = main(dirPath)
            
        saveToFile(linesToWrite)
        
    except Exception as e:
        print(colored(255, 0, 0, f"Error: { e }"))


def help():
    print("Usage of SHA1PY")
    print("\nDESCRIPTION")
    print("\tList sha1 checksum of files in given directory")
    print("\n\t-r")
    print("\t\tIf there are subdirectories it will also loop through them and return checksum of files within.")
    print("\t-h")
    print("\t\tDisplays this messsage")
    print("\nUSAGE")
    print("\tpython main.py -r /home")


options = { "-h": help, "-r": recursive }

if len(sys.argv) == 2:
    noRecursive()
else:
    options[sys.argv[1]]()