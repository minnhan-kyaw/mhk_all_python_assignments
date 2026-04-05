from datetime import datetime
print( )
print("      personal information collector"  .upper())
name = input("What is your name?: ")
gender = input("What is your gemder? [male or female] : ")
address = input("Where are you living now?: ")
home_town = input("Where are you from?: ")
job = input("What is your career?: ")
ph = int(input("What is moblie phone number?: "))
email = input("What is your email address?: ")
hobby = input("What do you do in your free time?: ")
education = input("What is your education background?: ")
birthday = input("What is you birthday?: [dd/mm/yyyy]")
birthday_date = datetime.strptime(birthday, "%d/%m/%Y")
age = datetime.now().year - birthday_date.year
weight = float(input("Enter your weight?[kg] : "))
height_cm = int(input("Enter your height?[cm] : "))
height_m = height_cm / 100
bmi = weight / (height_m ** 2)
personal_information_collection = f"""
Name : {name}
Gender : {gender}
Address : {address}
Native place : {home_town}
Career : {job}
Mobile phone number : {ph}
Email address : {email}
Hobby : {hobby}
Education background = {education}
Birthday : {birthday} ({age} year old)
Your body mass index(BMI) is {bmi}
"""
print(personal_information_collection)
print(    "end" .upper())