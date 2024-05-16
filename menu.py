import users
from pyfiglet import figlet_format
from platform import uname
from termcolor import colored
from os import system
from getpass import getpass
from hashpassword import hashing
from dbManager import dbManager
CLEAN_COMMAND = "cls" if (uname().system == "Windows") else "clear"
BANNER = colored(figlet_format("BANK"), "light_cyan")


def clean():
    system(CLEAN_COMMAND)
    print(BANNER)


def check_user(username, password):
    with dbManager() as db:
        db.execute("SELECT A.user_id,A.password,B.user_id FROM users AS A INNER JOIN etc AS B ON A.user_id = B.user_id WHERE A.username = '{}' AND A.password = '{}'".format(username, password))
        if db.fetchone():
            return True


def main():
    clean()
    username = input("USERNAME : ").lower()
    password = hashing(getpass("PASSWORD : "))
    if check_user(username, password):
        pass
    else:
        pass


if __name__ == "__main__":
    main()
