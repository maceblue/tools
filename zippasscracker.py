import zipfile
import itertools
import string
from threading import Thread
import hashlib

zipFile = zipfile.ZipFile("/home/morpheus/Tuts/Python/Python.jpg.zip")

def bruteforce():
    myLetters = string.ascii_letters + string.digits + string.punctuation
    for i in range(3,10):
        for j in map(''.join, itertools.product(myLetters, repeat=i)):
            t = Thread(target=crack, args=(zipFile, j))
            t.start()

def dictionary():
    passwords = open("passwordlist.txt")
    for line in passwords.readlines():
        pwd = line.strip('\n')
        t = Thread(target=crack, args=(zipFile, pwd))
        t.start()

def crack(zip, pwd):
    try:
        zip.extractall(pwd=str.encode(pwd))
        print('Success: Password is ' + pwd)
    except:
        pass

dictionary()