import os

def listUndangan():
    os.system("clear")
    print("""
==========================
U N D A N G A N - S A Y A
==========================
    """)
    fileData = open("database.txt", "a")
    nama = input("Masukan Nama : ")
    alamat = input("Masukan Alamat : ")
    phone = input("Masukan No Wa : ")

    formatText = f"{nama},{alamat},{phone}\n"

    fileData.write(formatText)

def readUndangan():
    fileData = open("database.txt", "r")
    result = fileData.read()
    os.system("clear")
    print(result)

listUndangan()
readUndangan()
