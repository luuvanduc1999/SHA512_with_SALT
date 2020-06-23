import pyodbc
import string
import os
from colorama import Fore, Back, Style
from colorama import init

class Server:

    def __init__(self):
        init(autoreset=True)
        server = 'password.database.windows.net'
        database = 'Password'
        dusername = 'luuvanduc'
        dpassword = 'Poiu.1234'
        driver_names = [x for x in pyodbc.drivers() if x.endswith(' for SQL Server')]
        driver= driver_names[0]
        self.cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+dusername+';PWD='+ dpassword)
        self.cnxn.timeout = 0
        self.cnxn.autocommit = True
        self.cursor = self.cnxn.cursor()
        # Database format: db[username] = ( salt, hashed )

    # store raw user data
    def add_user(self, username, password_digest, name, salt):
        try:
            self.cursor.execute('EXEC _insertAccount \''+username+'\', \''+password_digest+'\', \''+name+'\', \''+salt+'\'  ')
            print(Fore.GREEN+'\nTao moi thanh cong!')
        except:
            print(Fore.RED+"\nTen tai khoan da ton tai! Vui long chon ten khac")
        input("Nhan Enter de tiep tuc...")

    def getSalt(self, username):
        salt='';
        self.cursor.execute('EXEC _getSalt \''+username+'\'')
        row=self.cursor.fetchone()
        if row:
            salt=row.Salt
            return salt
        else:
            print(Fore.RED+"\nTai khoan khong co trong he thong")
            input("Nhan Enter de tiep tuc...")
            return ''

    def authenticate(self, username, password_digest):
        
        self.cursor.execute('EXEC _checkLogin \''+username+'\', \''+password_digest+'\'')
        row=self.cursor.fetchone()
        if row:
            name=row.Name
            print(Fore.GREEN+"\nXac thuc thanh cong! Xin chao "+name+"." )
        else:
            print(Fore.RED+"\nMat khau sai")
        input("Nhan Enter de tiep tuc...")


