import os
import sys

if not os.path.exists("nex.txt"):
    with open('nex.txt', 'w') as create:
        create.close()

def register():
    print("=========== Register User ===========")
    username = input("Enter the username: ").strip()
    
    with open('nex.txt', 'r') as file:
        if any(username in line for line in file):
            print("Username already exists")
            sys.exit()
    
    password = input("Enter the password: ").strip()
    confirm_password = input("Confirm password: ").strip()
    
    if password != confirm_password:
        print("Passwords do not match!")
        sys.exit()
    
    with open('nex.txt', 'a') as file:
        file.write(f"username: {username}, password: {password}\n")
        print("User registered successfully")

register()

def login():
    print("=========== Login User ===========")
    username = input("Enter the username: ").strip()
    password = input("Enter the password: ").strip()
    
    with open('nex.txt', 'r') as file:
        users = file.readlines()
    
    is_login = False
    for user in users:
        user_details = user.strip().split(", ")
        if len(user_details) == 2:  # Check if the split resulted in two parts
            uname = user_details[0].split(": ")[1]
            upass = user_details[1].split(": ")[1]
            if username == uname and password == upass:
                is_login = True
                break
    
    if is_login:
        print("Login successful")
    else:
        print("Invalid credentials")

login()
