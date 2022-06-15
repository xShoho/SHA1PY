import hashlib
import os

def hashFile(filename):
    if not os.path.exists(filename):
        raise Exception(f'Either the file is missing or not readable: "{ filename }"')
    
    sha = hashlib.sha1()
    
    with open(filename, 'rb') as file:
        chunk = 0
        
        while chunk != b'':
            chunk = file.read(1024)
            sha.update(chunk)
            
    return sha.hexdigest()