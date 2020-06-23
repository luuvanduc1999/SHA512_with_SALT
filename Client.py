from Server import *
import os
from colorama import Fore, Back, Style
from colorama import init
import random
from SHA512 import *

def randomString(stringLength=32):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def menu():

    keep_going = True
    while keep_going:
        print('\x1bc')
        print(Fore.GREEN+"---------MENU----------")
        print(Fore.CYAN+"1.) Tao tai khoan")
        print(Fore.BLUE+"2.) Xac thuc tai khoan")
        print(Fore.RED+"3.) Thoat")

        menu_choice = input("\nHay chon: ")

        if menu_choice is "1":
            print('\x1bc')
            print(Fore.GREEN+"-------TAO TAI KHOAN------")
            name=input("Ten cua ban: ")
            username = input("Nhap username: ")
            password = input("Nhap password: ")

            salt = randomString(32)
            password_digest=SHA512(salt[0:16]+password+salt[16:32])

            server.add_user(username, password_digest, name, salt )


        if menu_choice is "2":
            print('\x1bc')
            print(Fore.GREEN+"---------XAC THUC-------")
            username = input("Nhap username: ")
            password = input("Nhap password: ")

            salt = server.getSalt(username)
            
            if (salt!=""):
                password_digest=SHA512(salt[0:16]+password+salt[16:32])
                server.authenticate(username, password_digest)

        if menu_choice is "3":
            keep_going = False

if __name__ == '__main__':

    server = Server()
    menu()
