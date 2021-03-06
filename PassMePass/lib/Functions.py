import mysql.connector
from os import system

from lib.Globals import ColorObj

def starter(argv):
    if not argv.config and not argv.input and not argv.argv:
        print(f"{ColorObj.bad} Use --help")
        exit()
    if argv.argv:
        if not argv.host or not argv.username or not argv.email or not argv.password:
            print(f"{ColorObj.bad} Use --help")
            exit()
        return "argv"
    if argv.config:
        print(f"{ColorObj.bad} Not implemented")
        exit()
        return "config"
    if argv.input:
        return "input"
    system('service mysql start')

def connector():
    try:
        conn = mysql.connector.connect (
            host = "localhost",
            user = "root",
            database = "passwords",
            passwd = str(input(f"{ColorObj.other} Enter password: "))
        )
        cursor = conn.cursor()
        system('clear')
    except Exception as E:
        print(f"{ColorObj.bad} Exception {E} occured")
        exit(0)
    return conn, cursor
