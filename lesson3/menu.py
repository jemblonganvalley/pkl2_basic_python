
def menu():

    print("""
                                                                          
   ,---,                                     .--.--.                                      
  '  .' \      ,-.----.  ,-.----.           /  /    '.                                    
 /  ;    '.    \    /  \ \    /  \         |  :  /`. /                                    
:  :       \   |   :    ||   :    |        ;  |  |--`                                     
:  |   /\   \  |   | .\ :|   | .\ :        |  :  ;_      ,--.--.        .--,   ,--.--.    
|  :  ' ;.   : .   : |: |.   : |: |         \  \    `.  /       \     /_ ./|  /       \   
|  |  ;/  \   \|   |  \ :|   |  \ :          `----.   \.--.  .-. | , ' , ' : .--.  .-. |  
'  :  | \  \ ,'|   : .  ||   : .  |          __ \  \  | \__\/: . ./___/ \: |  \__\/: . .  
|  |  '  '--'  :     |`-':     |`-'         /  /`--'  / ," .--.; | .  \  ' |  ," .--.; |  
|  :  :        :   : :   :   : :           '--'.     / /  /  ,.  |  \  ;   : /  /  ,.  |  
|  | ,'        |   | :   |   | :             `--'---' ;  :   .'   \  \  \  ;;  :   .'   \ 
`--''          `---'.|   `---'.|                      |  ,     .-./   :  \  \  ,     .-./ 
                 `---`     `---`                       `--`---'        \  ' ;`--`---'     
                                                                        `--`              
    """)

    print("""
==========================================================================================
                MENU :      1. Login        2. Register     3. Exit
==========================================================================================
    """)

    menu = input("Masukan Menu : ")

    if menu == "1" :
        print("Login")
        return
    
    if menu == "2":
        print("Register")
        return
    
    exit()


menu()
