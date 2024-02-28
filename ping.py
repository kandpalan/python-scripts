#!/usr/bin/python3
import os

def check_ping():
       response = os.system(f'ping -c {n} {hostname} > /dev/null')
       if response == 0:  # "0" is code of os.system() == echo$?
         pingstatus = "Network Active"
       else:
         pingstatus = "Network Error"
       print (f"{pingstatus}:- ",f"{hostname}",f":- Number of pings : {n}")
check_ping()
