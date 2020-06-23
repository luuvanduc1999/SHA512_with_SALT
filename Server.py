import pyodbc
import random
import string
import os
from SHA512 import *
from colorama import Fore, Back, Style
from colorama import init

def randomString(stringLength=32):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


class Server:

    def __init__(self):
        init(autoreset=True)
        server = '****.database.windows.net'
        database = '****'
        dusername = '******'
        dpassword = '******'
        driver_names = [x for x in pyodbc.drivers() if x.endswith(' for SQL Server')]
        driver= driver_names[0]
        self.cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+dusername+';PWD='+ dpassword)
        self.cnxn.timeout = 0
        self.cnxn.autocommit = True
        self.cursor = self.cnxn.cursor()
        # Database format: db[username] = ( salt, hashed )

    # store raw user data
    def add_user(self, username, password, name):
        salt = randomString(32)
        hash_digest=SHA512(salt[0:16]+password+salt[16:32])
        try:
            self.cursor.execute('EXEC _insertAccount \''+username+'\', \''+hash_digest+'\', \''+name+'\', \''+salt+'\'  ')
            print(Fore.GREEN+'\nTao moi thanh cong!')
        except:
            print(Fore.RED+"\nTen tai khoan da ton tai! Vui long chon ten khac")
        input("Nhan Enter de tiep tuc...")


    def authenticate(self, username, password):
        salt='';
        self.cursor.execute('EXEC _getSalt \''+username+'\'')
        row=self.cursor.fetchone()
        if row:
            salt=row.Salt
        else:
            print(Fore.RED+"\nTai khoan khong co trong he thong")
            input("Nhan Enter de tiep tuc...")
            return

        hash_digest=SHA512(salt[0:16]+password+salt[16:32])
        
        self.cursor.execute('EXEC _checkLogin \''+username+'\', \''+hash_digest+'\'')
        row=self.cursor.fetchone()
        if row:
            name=row.Name
            print(Fore.GREEN+"\nXac thuc thanh cong! Xin chao "+name+"." )
        else:
            print(Fore.RED+"\nMat khau sai")
        input("Nhan Enter de tiep tuc...")


