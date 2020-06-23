from Server import Server
import os
from colorama import Fore, Back, Style
from colorama import init

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
            server.add_user(username, password, name )


        if menu_choice is "2":
            print('\x1bc')
            print(Fore.GREEN+"---------XAC THUC-------")
            username = input("Nhap username: ")
            password = input("Nhap password: ")
            server.authenticate(username, password)

        if menu_choice is "3":
            keep_going = False

if __name__ == '__main__':

    server = Server()
    menu()
