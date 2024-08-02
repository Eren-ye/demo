import os 

if not os.path.exists("users.txt"):
  handle = open("users.txt", "w")
  handle.close()

def register():
  print("===========Register User===========")
  username = input("Enter username: ").strip()
  if username in open("users.txt", "r").read():
    print("Username already exists")
    exit()
  password = input("Enter password: ").strip()
  confirm_password = input("Confirm password: ").strip()
  if password != confirm_password:
        print("Passwords do not match")
        exit()
  with open("users.txt", "a") as file:
    file.write(f"username:{username},password:{password}\n")
    print("User registered successfully")

register()


def login():
   print("===========Login User===========")
   username = input("Enter username: ").strip()
   password = input("Enter password: ").strip()
   with open("users.txt", "r") as file:
      users = file.readlines()
      is_login = False
      for user in users:
         user = user.strip().split(",")
         uname = user[0].split(":")[1]
         upass = user[1].split(":")[1]
         if username == uname and password == upass:
            is_login = True
      if is_login:
        print("Login successful")
      else:   
        print("Invalid credentials")
        exit()
login()
