import os

print()

def ask_row():
    return int(input("Please enter the number of rows you want to make: "))
os.system("cls")

rows = ask_row()
space_icon = " "
star_icon = "*"

display = ""
for row in range(1,rows+1):
    for star in range(row):
        display += "*"
    display += "\n"
print(display)

display = ""
print()

for row in range(1,rows+1):
    for space in range(rows - row):
        display += space_icon
    for star in range(row):
        display += star_icon
    display += ("\n")
print(display)

display = ""
print()

for row in range(1,rows+1):
    for space in range(rows - row):
        display += space_icon
    for star in range(row):
        display += space_icon
        display += star_icon
    display += ("\n")
print(display)

display = ""
print()

for row in range(1,rows + 1):
    for space in range(rows - row):
        display += space_icon
    for star in range(1,row * 2):
        display += star_icon
    display += "\n"
print(display)