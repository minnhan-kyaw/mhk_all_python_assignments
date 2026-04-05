from datetime import datetime
import os

def clear_default():
    os.system("cls")
    print()
    print("      PERSONAL INFORMATION COLLECTOR")
    print()

clear_default()
def get_input(message,error_message):
    while True:
        value = input(message)
        clear_default()
        if value == "":
            print(error_message)
        else:
            return value

name = get_input("What is your name?: ","Name cannot be empty!")
gender = get_input("What is your gender[male or female]?: ","Gender cannot be empty!")
address = get_input("What is your address?: ","Address cannot be empty!")
hometown = get_input("Where are you from?: ","Native place cannot be empty!")
job = get_input("What is your career?: ","Career cannot be empty!")
ph = get_input("What is your phone number?: ","Phone number cannot be empty!")
email = get_input("What is your gamil address?: ","Email cannot be empty!")
hobby = get_input("What do you do in your free time?: ","Hobby cannnot be empty!")
edu = get_input("What is your education background?: ","Education cannot be empty!")

def ask_birthday():
    while True:
        birthday = input("What is your birthday? [dd/mm/yyyy]: ")
        clear_default()
        if birthday == "":
            print("Birthday cannot be empty!")
        else:
            return birthday

clear_default()

birthday = ask_birthday()
birthday_date = datetime.strptime(birthday,"%d/%m/%Y")
age = datetime.now().year - birthday_date.year
weight = float(input("Enter your weight [kg]: "))
height_cm = float(input("Enter your height [cm]: "))
height_m = height_cm / 100
bmi = weight / (height_m ** 2)
clear_default()
body_mass_index = bmi

personal_info = f"""
Name                     : {name}
Gender                   : {gender}
Address                  : {address}
Native place             : {hometown}
Career                   : {job}
Mobile phone number      : {ph}
Email address            : {email}
Hobby                    : {hobby}
Education background     : {edu}
Birthday                 : {birthday_date} (Now you are {age} years old)
Your BMI is              : {body_mass_index}
"""

print(personal_info)
print("                 END")