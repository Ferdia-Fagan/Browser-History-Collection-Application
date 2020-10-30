# This is a sample Python script.
import os
import pathlib
import sqlite3
import csv

import sys
from datetime import datetime, timezone

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from cryptography.fernet import Fernet

pathlib.Path('./user_folder').mkdir(exist_ok=True)

# Data:
firefox_tables = [("moz_places","last_visit_date"),("moz_annos", "dateAdded"),("moz_historyvisits","visit_date"),("moz_bookmarks", "dateAdded")]
chrome_tables = [("downloads","start_time"),("visits", "visit_time"),("urls","last_visit_time")]

firefox_db_file = "/places.sqlite"
chrome_db_file = "/History"

sample_query = "SELECT * FROM %s where %s between %s and %s;"

# Commands:
EXIT = "exit"

LOAD_USER_DATA = "load_my_data"
FROM_TIME = "from_time"
until_TIME = "until_time"

CHROME = "chrome"
FIREFOX = "firefox"

FIREFOX_HISTORY_FOLDER_PATH = "firefox_history_folder_path"
CHROME_HISTORY_FOLDER_PATH = "chrome_history_folder_path"


def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    # with open(os.path.join(__location__, "./user_folder/user_key.key", "wb")) as key_file:
    with open("./user_folder/user_key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_the_asymetric_key():
    """
    Loads the key from the current directory named `key.key`
    """
    with open("./resources/publicKey.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key

class UserClient:

    def __init__(self):
        with open('./resources/settings.txt', 'r') as file:
            settings_file = file.read()
        user_settings = [setting.split(':') for setting in settings_file.split('\n')]

        if(user_settings != [[""]]):
            self.user_settings = {user_settings[i][0]: user_settings[i][1] for i in range(0,len(user_settings)-1)}
        else:
            print("\n REMEMBER TO SETUP firefox_history_folder_path AND/OR chrome_history_folder_path. \n")
            self.user_settings = {}

        # Make new key:
        self.users_key = write_key()

    def change_setting(self,setting_name, setting_value):
        if (setting_name == FIREFOX):
            db_file_name = firefox_db_file
        else:
            db_file_name = chrome_db_file
        self.user_settings[setting_name] = setting_value + db_file_name

    def save_settings(self):
        print(self.user_settings)
        # for k in self.user_settings:
        with open('./resources/settings.txt', 'w') as file:
            for k,v in self.user_settings.items():
                file.writelines(k + ":" + v + '\n')

    def access_sql_lite(self,browser_are_checking,from_time, until_time, history_meta_data):

        if(from_time > until_time):
            temp=from_time
            from_time=until_time
            until_time=temp

        f = Fernet(self.users_key)
        public_key=load_the_asymetric_key()

        if(browser_are_checking==FIREFOX):
            tables = firefox_tables

            end_date = until_time.timestamp() * 1000000
            start_date = from_time.timestamp() * 1000000

            meta_data = FIREFOX
        else:
            tables = chrome_tables

            end_date = (until_time.timestamp() + 11644473600)* 1000000
            start_date = (from_time.timestamp() + 11644473600)* 1000000

            meta_data = CHROME
        try:
            conn = sqlite3.connect(self.user_settings[browser_are_checking])

            cur = conn.cursor()
            dbs_columns = {}
            results = {}
            for (idx, (db, date_column)) in enumerate(tables):
                samle_query_complete = sample_query % (db,date_column, start_date, end_date)
                print(samle_query_complete)
                cur.execute(samle_query_complete)
                dbs_columns[db] = [description[0] for description in cur.description]
                results[db] = cur.fetchall()

            conn.close()

            for (db_name,result) in results.items():
                print(type(result))
                with open("./user_folder/"+db_name+".csv", 'w') as out:
                    file_writer = csv.writer(out)
                    file_writer.writerow(dbs_columns[db_name])
                    for row in result:
                        file_writer.writerow(row)

                #  Now to encrypt the file
                with open("./user_folder/"+db_name+".csv", "rb") as file:
                    # read all file data
                    file_data = file.read()

                encrypted_file = f.encrypt(file_data)
                encrypted_key = public_key.encrypt(
                    self.users_key,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )

                with open("./user_folder/"+db_name+".csv", "wb") as file:
                    file.write(encrypted_file)
                with open("./user_folder/user_key.key", "wb") as file:
                    file.write(encrypted_key)
                with open("./user_folder/meta_data.txt", "w") as file:
                    file.write(meta_data + "\n" + history_meta_data)
        except:
            print("\n--------------------------------------------------------------------------\n")
            print("\n CANT FIND BROWSERS.\n REMEMBER TO SETUP firefox_history_folder_path AND/OR chrome_history_folder_path. \n Please try again")
            print("\n--------------------------------------------------------------------------\n")
            return
        print("Completed collecting and encrypting data \n")

        print("\n Please email: ferdiafagan@outlook.com \n"
              "or \n"
              "submit to dropbox: https://www.dropbox.com/request/gKADUv9Yb9AUDLqrfrrT")
        print("\n \n REMEMBER: YOUR data has been encrypted. It is safe. The only reason to use dropbox is incase you want to be annonomous.\n"
              "Your data is safe!")


def give_user_prompts():
    print("\n--------------------------------------------------------------------------\n")
    print("Commands: \n"
          "1) To load your data into a folder: load_my_data "
          # "Then you will be prompted with:<from_time=\"dd/mm/yy hh:mm\"> <until_time=\"dd/mm/yy hh:mm\"> \n"
          "2) To exit: exit \n"
          "3) To add path to firefox browser history: firefox_history_folder_path=\"the path\" \n"
          "4) To add path to chrome browser history: chrome_history_folder_path=\"the path\" \n")

    print("Reminder \n"
          "1) Dont include '<' or '>' in commands. They are just there to be more specific on what to enter. \n"
          "2) Time is in 24 hr clock"
          "3) The data will be loaded within this applications folder, in a subfolder called \"user_folder\"")
    print("\n--------------------------------------------------------------------------\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome")

    keep_running=True
    client = UserClient()

    while(keep_running):
        give_user_prompts()
        user_command = input("Please enter your command (or 'exit')")
        if(user_command == EXIT):
            keep_running=False

        elif(user_command == LOAD_USER_DATA):
            from_time = input("From time (dd/mm/yyyy hh:mm in 24 hr clock):")
            until_time = input("Until time (dd/mm/yyyy hh:mm in 24 hr clock):")
            browser_checking = input("Enter the browser are checking (chrome or firefox")
            try:
                from_time_fin = datetime.strptime(from_time, '%d/%m/%Y %H:%M')
                until_time_fin = datetime.strptime(until_time, '%d/%m/%Y %H:%M')
                print("\n")
            except:
                print("Please check date and time format \n")

            history_meta_data = input("Please enter a short description of what you where researching during this time:")

            if(browser_checking == CHROME or browser_checking == FIREFOX):
                client.access_sql_lite(browser_checking,from_time_fin,until_time_fin,history_meta_data)
            else:
                print("Browser not compatible \n")

        elif(user_command == FIREFOX_HISTORY_FOLDER_PATH):
            firefox_history_path = input("Firefox browser history folder path:")
            client.change_setting(FIREFOX,firefox_history_path)

        elif(user_command == CHROME_HISTORY_FOLDER_PATH):
            chrome_history_path = input("Chrome browser history folder path:")
            client.change_setting(CHROME, chrome_history_path)
    # Save user details
    client.save_settings()

