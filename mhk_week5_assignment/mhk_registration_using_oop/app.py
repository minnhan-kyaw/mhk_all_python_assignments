import os
from info import Info
from login import Login

info = Info()
login = Login()

if info.get_data():
    if login.checking(info.email, info.password):
        os.system("cls")
        print(f"Welcome {info.fullname}.")
        print("Congratulation.Now you haave an email account.")
        
your_acc = f"""
Full name    : {info.fullname}
User name    : {info.username}
Email address : {info.email}
Password : {info.password}(Don't show your password to other)
"""
print(your_acc)