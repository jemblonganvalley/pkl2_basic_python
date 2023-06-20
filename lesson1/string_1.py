import os
from time import sleep

# clear layar terlebih dahulu
os.system("clear")  # cls

# tampilkan Judul aplikasi
title = """
================================
A P L I K A S I - K A M P R E T
================================
"""

print(title)

# tunggu 3 detik
sleep(3)

username = input("Masukan username : ")
address = input("Masukan alamat : ")
phone = input("Masukan Phone : ")
email = input("Masukan email : ")

text = f"""
--------------------------------------------
    nama        : { username }
--------------------------------------------
    alamat      : { address }
--------------------------------------------
    phone       : { phone }
--------------------------------------------
    email       : { email }
--------------------------------------------
"""

os.system("clear")

print(text)
