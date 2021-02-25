#!/usr/bin/python3
from argparse import ArgumentParser
from termcolor import colored

from lib.Globals import sql_dict, ColorObj
from lib.PathFunctions import urler, ender
from lib.Functions import starter, connector

parser = ArgumentParser(description=colored("Store and update passwords!",color='yellow'))
group = parser.add_mutually_exclusive_group()
parser.add_argument('-H', '--host', type=str, help="Host")
parser.add_argument('-U', '--username', type=str, help="Username")
parser.add_argument('-E', '--email', type=str, help="Email")
parser.add_argument('-P', '--password', type=str, help="Password")
parser.add_argument('-A', '--two-factor', type=str, help="2FA keys")
parser.add_argument('-B', '--backup', type=str, help="Backup data")
parser.add_argument('-O', '--other', type=str, help="Other")
group.add_argument('-c', '--config', action="store_true", help="Fetch from config file (optional, not implemented)")
group.add_argument('-a', '--argv', action="store_true", help="Fetch from command line (optional, not implemented)")
group.add_argument('-i', '--input', action="store_true", help="Fetch from input (optional, not implemented)")
argv = parser.parse_args()

mode = starter(argv)

if mode == 'argv':
    sql_dict['HOST'] = ender(urler(argv.host).replace('http://', 'https://'), "/")
    sql_dict['USERNAME'] = argv.username
    sql_dict['EMAIL'] = argv.email
    sql_dict['PASSWORD'] = argv.password
    sql_dict['2FA'] = argv.two_factor
    sql_dict['BACKUP'] = argv.backup
    sql_dict['OTHER'] = argv.other
elif mode == 'input':
    sql_dict['HOST'] = ender((urler(input(f"{ColorObj.information} Enter Host: "))).replace('http://', 'https://'), "/")
    sql_dict['USERNAME'] = input(f"{ColorObj.information} Enter Username: ")
    sql_dict['EMAIL'] = input(f"{ColorObj.information} Enter Email: ")
    sql_dict['PASSWORD'] = input(f"{ColorObj.information} Enter Password: ")
    sql_dict['2FA'] = input(f"{ColorObj.information} Enter 2FA: ")
    sql_dict['BACKUP'] = input(f"{ColorObj.information} Enter Backup: ")
    sql_dict['OTHER'] = input(f"{ColorObj.information} Enter other data: ")
try:
    conn, cursor = connector()
except Exception as E:
    print(E)

def insert_mysql():
    statement = "INSERT INTO password (HOST, USERNAME, EMAIL, PASSWORD, 2FA, BACKUP, OTHER) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (
            ender(urler(sql_dict['HOST']).replace('http://', 'https://'), "/"),
            sql_dict['USERNAME'],
            sql_dict['EMAIL'],
            sql_dict['PASSWORD'],
            sql_dict['2FA'],
            sql_dict['BACKUP'],
            sql_dict['OTHER']
    )
    cursor.execute(statement, values)
    conn.commit()

def fetch_mysql():
    statement = "SELECT * from password"
    cursor.execute(statement)
    data = cursor.fetchall()
    return data

def update_mysql(host):
    data = fetch_mysql()
    where = ""
    for i in data:
        if i[1] == host:
            where = i[0]
            data = i[1:]
            break

    statement = "UPDATE password SET HOST = %s, USERNAME = %s, EMAIL = %s, PASSWORD = %s, 2FA = %s, BACKUP = %s, OTHER = %s WHERE ID = %s"
    values = (
            ender(urler(sql_dict['HOST']).replace('http://', 'https://'), "/"),
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
    sql_dict['HOST'] = ender(urler(sql_dict['HOST']), "/")
    const = input(f"{ColorObj.information} Fetch data or edit (F/E)? ")
    if const == 'F':
        print(f"{ColorObj.good} Fetching data ..")
        query_res = fetch_mysql()
        for i in query_res:
            print(i)
        print(f"{ColorObj.good} Fetched!")
        main();exit()
    for keys,values in sql_dict.items():
        print("{} ::: {}".format(keys, colored(values, color='green')))
    print("")
    cont = input(f"{ColorObj.information} Continue with above value (Y/N) or update value (U): ")
    if cont.upper() == 'Y':
        try:
            insert_mysql()
        except Exception as E:
            print(f"Error {E,E.__class__} occured while inserting data")
            exit(0)
    elif cont.upper() == 'U':
        up = input(f"{ColorObj.information} Enter hostname to update: ")
        update_mysql(up)
    else:
        main()

if __name__ == '__main__':
    main()
