import os

product_list = []

def menu_show(menu_name):
    os.system("cls")
    print(f"\n[ {menu_name} ]\n")

def create_product():
    menu_show("Creat Product")
    name = input("Name: ")
    if name == "":
        return "Creation failed.Name cannot be empty!"
    price = int(input("Price: "))
    if price == "":
        return "Creation failed.Price cannot be empty(Price must be integer)."
    product = {
        "Name" : name,
        "Price" : price
    }
    product_list.append(product)
    return "\nSystem message:You created a product.\n"

def retrieve_product():
    menu_show("Retrieve Product")
    if len(product_list) == 0:
        print("No product found!")
    index = 0
    for product in product_list:
        for key,value in product.items():
            print(f"{index}:{key} = {value}")
        index +=1

    return "\nSystem message:Products retrieved.\n"

def update_product():
    menu_show("Update product.")
    if len(product_list) == 0:
        return "No product found!"
    index = int(input("Index: "))
    if index < 0 or index >= len(product_list):
        return "No product found.Try again!"
    name = input("Name: ")
    price = int(input("Price: "))
    product = product_list[index]
    product["Name"] = name 
    product["Price"] = price
    return "\nystem message:You updated a product.\n"

def delete_product():
    menu_show("Delete Product")
    if len(product_list) == 0:
        return "There's nothing to delete."
    index = int(input("Index: "))
    if index < 0 or index >= len(product_list):
        return "No product found.Try again!"
    product_list.pop(index)
    return "\nSystem message:You deleted a product.\n"
    

while True:
    print("\nStore front!")
    print("""
[1] Create
[2] Retrieve
[3] Update
[4] Delete
[5] Exit

""")
    menu = input("\nMenu: ")
    if menu == "1":
        print(create_product())
    elif menu == "2":
        print(retrieve_product())
    elif menu == "3":
        print(update_product())
    elif menu == "4":
        print(delete_product())
    elif menu == "5":
        os.system("cls")
        print("Bye Bye.")
        break
    else:
        os.system("cls")
        print("\nSystem message: Invalid menu.")
    