# Flow 

def cekUsia(usia):

    # jika usia dibawah 20 maka jangan izinkan
    if usia < 20 :
        print("Kamu belum bisa masuk")
    else :
        print("Silakan Masuk")


def checkUsername():
    username = input("Masukan username : ")

    if username == "fadliselaz":
        print("Login berhasil")
    else : 
        print("Username tidak terdaftar !")


def login():
    username = input("Masukan Username : ")
    password = input("Masukan Password : ")

    if username == "fadliselaz" and password == "1234":
        print("Login berhasil")
    else :
        print("Login GAGAL !")



def login2():
    username = input("Masukan Username : ")
    password = input("Masukan Password : ")

    if username != "fadliselaz" or password != "1234" :
        print("Username atau password SALAH !")
        return
    
    print("Selamat Datang !")


def login3():
    dataUsername = ["fadliselaz", "evalia", "rahman", "alif"]
    dataPassword = ["1234", "2121", "1414", "4545"]

    username = input("Masukan Username : ")

    if username not in dataUsername:
        print("Username Tidak Ditemukan !")
        return
    
    password = input("Masukan Password : ")

    if password not in dataPassword:
        print("Password SALAH !")
        return
    
    print("""
============================
S E L A M A T - D A T A N G 
============================
    """)


login3()
