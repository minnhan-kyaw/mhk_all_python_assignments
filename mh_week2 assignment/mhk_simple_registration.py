import os

print()
print("[GMAIL REGISTRATION]".upper())

fullname = input("Enter your full name: ")
if fullname == "" :
     print("Full name cannot be empty. Try again.")
     fullname = input("Enter your full name: ")
if fullname == "" :
     print("Full name cannot be empty. Last attempt.")
     fullname = input("Enter your full name: ")
if fullname == "" :
     print("Resstart registration later.")
     exit()
     
username = input("Enter your user name: ")
if username == "":
    print("User name cannot be empty. Try again.")
    username = input("Enter your user name: ")
if username == "":
    print("User name cannot be empty. Last attempt.")
    username = input("Enter your user name: ")
if username == "":
    print("Restart registration later.")
    exit()
    
email = input("Enter email address: ")

if "@" not in email or "." not in email:
  print("Email must contain '@' and '.'.Try Again.")
  email = input ("Enter your Email Address :")
if "@" not in email or "." not in email:
  print("Email must contain '@' and '.'.Try Again(Last attempt)")
  email = input ("Enter your Email Address :")
if "@" not in email or "." not in email:
  print("Email must contain '@' and '.'.Try Again Later.")
  exit()

password = input("Enter your password: ")

if password == "" or len(password) < 6:
    print("Password must be at least 6 characters. Try again.")
    password = input("Enter your password: ")
if password == "" or len(password) < 6:
    print("Password must me at least 6 characters.Try again(Last attempt)")
    password = input("Enter your password: ")
if password == "" or len(password) < 6:
    print("Restart registration later.")
    exit()

confirm_1 = input("Enter confirm password: ")

if confirm_1 == password:
    print("Your registration successful.")
else:
    print("Password do not match. Try again.")
    confirm_2 = input("Enter confirm password: ")

    if confirm_2 == password:
        print("Your registration successful on second attempt.")
    else:
        print("Password do not match. Last attempt.")
        confirm_3 = input("Enter confirm password: ")

        if confirm_3 == password:
            print("Your registration successful on third attempt.")
        else:
            print("Restart registration later.")
            exit()

print("[gmail login]".upper())

login_email = input("Enter your email address: ")
login_password = input("Enter your password: ")

if login_email == email and login_password == password:
    print("Login successful.")
else:
    print("Login failed. Try again.")

    login_email = input("Enter your email address: ")
    login_password = input("Enter your password: ")

    if login_email == email and login_password == password:
        print("Login successful on second attempt.")
    else:
        print("Login failed. Last attempt.")

        login_email = input("Enter your email address: ")
        login_password = input("Enter your password: ")

        if login_email == email and login_password == password:
            print("Login successful on third attempt.")
        else:
            print("Too many attempts. Restart later.")

os.system("cls")
print( )
print(f"Welcome {fullname}")
print("You now have a Gmail account.")
your_acc = f"""
Full Name : {fullname}
User Name : {username}
Email address: {email}
Password : {password}
"""
print(your_acc)
