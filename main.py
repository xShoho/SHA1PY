import sys
import os
from utilities.Hash import hashFile
from utilities.Files import filesFromDir, filenamesFromDir

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

try:
    if len(sys.argv) != 2:
        raise Exception("You have to put only one argument which is path to directory")

    dirPath = os.path.dirname(sys.argv[1])
    shaKeys = []
    filenames = filenamesFromDir(dirPath)
    linesToWrite = []

    for file in filesFromDir(dirPath):
        shaKeys.append(hashFile(file))
        
    for i in range(0, len(shaKeys)):
        print(f'{ colored(0, 255, 0, f"filename: { filenames[0] }") } { colored(200, 200, 200, f"sha-1: { shaKeys[i] }") }')
        linesToWrite.append(f'{ filenames[i] }.com;{shaKeys[i]}\n')
        
    resFile = open("results.txt", "a+")
    
    for line in linesToWrite:
        resFile.write(line)
        
    print(colored(0, 100, 255, f"Wrote to file: { os.path.realpath(resFile.name) }"))    
    
    resFile.close()
    
except Exception as e:
    print(colored(255, 0, 0, f"Error: { e }"))
