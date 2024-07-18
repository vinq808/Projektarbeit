import datetime
import time
import os
import sys
import re
import json
import csv
import pickle
import getpass
import random
import secrets
import string
import hashlib
import requests
import unittest
import base64
import csv

#storing passwords in csv
users = {}
csv_file = "csv_file.csv"
with open(csv_file, mode='r', newline='') as file:
    leser = csv.DictReader(file)
    for row in leser:
        name = row["name"]
        user_pw = row["password"]
        url = row["url"]
        old_password = row["old_password"]
        old_password_2 = row["old_password_2"]
        notes = row["notes"]
        categories = row["categories"]
        user_date = row["user_date"]
        user_time = row["user_time"]
        users[name] = {"password": user_pw, "url": url, "old_password": old_password, "old_password_2": old_password_2, "notes": notes, "categories": categories, "user_date": user_date, "user_time": user_time}


#userinput
def ask_user(prompt):
    while True:
        response = input(prompt).strip().upper()
        if response == "Y":
            return True
        elif response == "N":
            return False
        else:
            print("Please answer with Y or N.")



#passwordgenerator
def generate_password():
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = lowercase.upper()
    digits = "0123456789"
    symbols = "!§$%&/()=?\\{[]}#+-.,;:_*'"

    lower, upper, nums, symb = True, True, True, True

    lower = ask_user("should your password contain lowercase letters? (Y/N)")
    upper = ask_user("Should your password contain uppercase letters (Y/N)")
    nums = ask_user("Should your password contain digits? (Y/N)")
    symb = ask_user("Sould your password contain symbols? (Y/N)")

    generated_pw = ""

    if lower:
        generated_pw += lowercase
    if upper:
        generated_pw += uppercase
    if nums:
        generated_pw += digits
    if symb:
        generated_pw += symbols
    
    pw_length = int(input("chose the length of your password \n"))

    generated_pw = "".join(random.sample(generated_pw, pw_length))

    print("Your password is: ", generated_pw)

    return generated_pw

def add_password():
    generate_self = ask_user("Do you want to generate your password? (Y/N)")
    if generate_self:
        generated_pw = generate_password()
        add_user_pw = generated_pw
    else:
        add_user_pw = input("what password do you want to safe?")
    add_name = input("enter username?")
    add_url = input("to which URL should the passowrd be safed?")
    add_user_pw_old = add_user_pw
    add_user_pw_old_2 = add_user_pw
    notes,categories = True, True
    notes = ask_user("Do you want to add notes to your password? (Y/N)")
    categories = ask_user("Do you want to add categories to your password? (Y/N)")

    if notes:
        add_notes = input("type in your notes")
    else:
        add_notes = ""
    if categories:
        add_categories = input("type in your category/categories")
    else:
        add_categories = ""
    current_datetime = datetime.datetime.now()
    add_user_date = current_datetime.strftime("%Y-%m-%d")
    add_user_time = current_datetime.strftime("%H:%M:%S")

    users[add_name] = {
        "password": add_user_pw,
        "url": add_url,
        "old_password": add_user_pw_old,
        "old_password_2": add_user_pw_old_2,
        "notes": add_notes,
        "categories": add_categories,
        "user_date": add_user_date,
        "user_time": add_user_time
    }
    
    print("You added the password", add_user_pw, " to the URL", add_url)

def show_passwords():
    input_url = input("Which URL does your password belong to? ")
    for name, data in users.items():
        if data["url"] == input_url:
            print(f"Name: {data['url']}, Password: {data['password']}")
            return
    print("URL not found.")


def safe_password():
    fieldnames = ["name", "password", "url", "old_password", "old_password_2", "notes", "categories", "user_date", "user_time"]
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for name, data in users.items():
            writer.writerow({"name": name,
                            "password": data["password"],
                            "url": data["url"],
                            "old_password": data["old_password"],
                            "old_password_2": data["old_password_2"],
                            "notes": data["notes"],
                            "categories": data["categories"],
                            "user_date": data["user_date"],
                            "user_time": data["user_time"]})
            
    print(f"You're passwords have been saved in '{csv_file}'")


while True:
    print("\n 1. Generate password\n", "2. Show passwords\n", "3. Add your own password\n", "6. Save and Quit")
    choice = input("Was möchten sie tun?\n")
    if choice == "1":
        generate_password()
    if choice == "2":
        show_passwords()
    if choice == "3":
        add_password()
    if choice == "4":
        print(users)
    if choice == "6":
        safe_password()
        break