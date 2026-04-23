import os
from data import Data
class Show_screen:
    def __init__(self):
        self.data = Data()
    def clear(self):
        os.system("cls")
    
    def show_menu(self,title):
        self.clear()
        print(f"\n[ {title} ]\n")

    def get_num(self,message):
        while True:
            val = input(message)
            if val.isdigit():
                return int(val)
            else:
                print("System message:Enter number only!\n")
    def get_name(self):
        while True:
            name = input("Name: ")
            if name != "":
                return name
            else:
                print("System message:Name cannot be empty!\n")

    def menu(self):
        print("\n[Stroe front]")
        print("""
[1] Create
[2] Retrieve
[3] Update
[4] Delete
[5] Exit
""")

    def run(self):
        while True:
            self.menu()
            write = input("Menu: ")

            if write == "1":
                self.show_menu("Create Product")
                name = self.get_name()
                price = self.get_num("Price: ")
                print(self.data.create(name, price))

            elif write == "2":
                self.show_menu("Retrieve Product")
                print(self.data.retrieve())

            elif write == "3":
                self.show_menu("Update Product")
                if len(self.data.product_list) == 0:
                    print("System message:No product found!\n")
                else:
                    print(self.data.retrieve())
                    index = self.get_num("Index: ")
                    if index < 0 or index >= len(self.data.product_list):
                        print("System message: Invalid index! Update cancled.\n ")
                    else:
                        name = self.get_name()
                        price = self.get_num("Price: ")
                        print(self.data.update(index,name,price))
            elif write == "4":
                self.show_menu("Delete Product")
                if len(self.data.product_list) == 0:
                    print("System message:No product found!\n")
                else:
                    print(self.data.retrieve())
                    index = self.get_num("Index: ")
                    print(self.data.delete(index))
            elif write == "5":
                self.clear()
                print("Byee!")
                break
            else:
                print("System message:Invalid menu!\n")