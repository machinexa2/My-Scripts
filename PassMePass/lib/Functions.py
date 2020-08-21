import mysql.connector
from os import system

def starter(argv):
    if not argv.config and not argv.input and not argv.argv:
        print("Use --help")
        exit()
    if argv.argv:
        if not argv.host or not argv.username or not argv.email or not argv.password:
            print("Use --help")
            exit()
        return "argv"
    if argv.config:
        print("Not implemented")
        exit()
        return "config"
    if argv.input:
        return "input"

def connector():
    try:
        conn = mysql.connector.connect (
            host = "localhost",
            user = "root",
            database = "passwords",
            passwd = str(input("Enter password: "))
        )
        cursor = conn.cursor()
        system('clear')
    except Exception as E:
        print(f"Exception {E} occured")
        exit(0)
    return conn, cursor
