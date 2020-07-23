import MySQLdb
import mysql.connector
from os import system as sys
from Globals import sql_dict
from argparse import ArgumentParser
from PathFunctions import PathFunction

parser = ArgumentParser(description="Store and update passwords!")
parser.add_argument('-H', '--host', type=str, help="Host")
parser.add_argument('-U', '--username', type=str, help="Username")
parser.add_argument('-E', '--email', type=str, help="Email")
parser.add_argument('-P', '--password', type=str, help="Password")
parser.add_argument('-A', '--two-factor', type=str, help="2FA keys")
parser.add_argument('-B', '--backup', type=str, help="Backup data")
parser.add_argument('-O', '--other', type=str, help="Other")
parser.add_argument('--fetch', type=str, help="Fetch from config file(optional)")
argv = parser.parse_args()
P = PathFunction()

if not argv.fetch:
    if not argv.host or not argv.username or not argv.email or not argv.password:
        print("Use --help")
        exit()
    sql_dict['HOST'] = P.urler(argv.host)
    sql_dict['USERNAME'] = argv.username
    sql_dict['EMAIL'] = argv.email
    sql_dict['PASSWORD'] = argv.password
    sql_dict['2FA'] = argv.two_factor
    sql_dict['BACKUP'] = argv.backup
    sql_dict['OTHER'] = argv.other

try:
    conn = mysql.connector.connect (
        host = "localhost",
        user = "root",
        database = "passwords",
        passwd = str(input("Enter password: "))
    )
    cursor = conn.cursor()
    sys('clear')
except Exception as E:
    print(f"Exception {E} occured")
    exit(0)

def insert_mysql():
    statement = "INSERT INTO password (HOST,USERNAME,EMAIL,PASSWORD,2FA,BACKUP,OTHER) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (
            P.urler(sql_dict['HOST']),
            sql_dict['USERNAME'],
            sql_dict['EMAIL'],
            sql_dict['PASSWORD'],
            sql_dict['2FA'],
            sql_dict['BACKUP'],
            sql_dict['OTHER']
    )
    cursor.execute(statement, values)
    conn.commit()

def check_mysql():
    statement = "SELECT * from password"
    cursor.execute(statement)
    data = cursor.fetchall()
    return data

def update_mysql(up):
    data = check_mysql()
    where = ""
    for i in data:
        if i[1] == up:
            where = i[0]
            data = i[1:]
            break
    print(where)
    sql_dict['HOST'] = P.urler(data[0])
    sql_dict['USERNAME'] = data[1] 
    sql_dict['EMAIL'] = data[2] 
    sql_dict['PASSWORD'] = data[3] 
    sql_dict['2FA'] = data[4]
    sql_dict['BACKUP'] = data[5]
    sql_dict['OTHER'] = data[6]
    print(sql_dict)
    sql_dict['HOST'] = P.urler(input("Enter Host: "))
    sql_dict['USERNAME'] = input("Enter Username: ")
    sql_dict['EMAIL'] = input("Enter Email: ")
    sql_dict['PASSWORD'] = input("Enter Password: ")
    sql_dict['2FA'] = input("Enter 2FA: ")
    sql_dict['BACKUP'] = input("Enter Backup: ")
    sql_dict['OTHER'] = input("Enter Other: ")

    statement = "UPDATE password SET HOST = %s, USERNAME = %s, EMAIL = %s, PASSWORD = %s, 2FA = %s, BACKUP = %s, OTHER = %s WHERE ID = %s"
    values = (
            P.urler(sql_dict['HOST']),
            sql_dict['USERNAME'],
            sql_dict['EMAIL'],
            sql_dict['PASSWORD'],
            sql_dict['2FA'],
            sql_dict['BACKUP'],
            sql_dict['OTHER'],
            int(where)) 
    cursor.execute(statement, values)
    conn.commit()

def main():    
    sql_dict['HOST'] = P.urler(sql_dict['HOST'])
    for keys,values in sql_dict.items():
        print("{} ::: {}".format(keys, values))
    print("")
    cont = input("Is the data correct (Y/N) or press (C) to check and (U) to update existing records: ")
    if cont.upper() == 'Y':
        try:
            insert_mysql()
        except:
            print("Error Inserting Data")
            exit(0)
    elif cont.upper() == 'C':
        query_res = check_mysql()
        for i in query_res:
            print(i)
    elif cont.upper() == 'U':
        up = input("Enter name to update")
        update_mysql(up)
    else:
        main()
main()
