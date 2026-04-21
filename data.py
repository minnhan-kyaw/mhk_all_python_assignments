from product import Product

class Data:
    def __init__(self):
        self.file_name = "products.txt"
        self.product_list = self.load_data()

    def load_data(self):
        products = []
        try:
            with open(self.file_name, "r") as f:
                for line in f:
                    clean_line = line.strip()
                    if clean_line and ":" in clean_line:
                        name, price = clean_line.split(":", 1)
                        products.append(Product(name, int(price)))

            return products
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.file_name, "w") as f:
            for p in self.product_list:
                f.write(f"{p.name}:{p.price}\n")

    def create(self, name, price):
        try:
            price = int(price)
        except:
            return "Invalid price!"
        
        product = Product(name, price)
        self.product_list.append(product)
        self.save_data()
        return "\nSystem message: Product created."

    def retrieve(self):
        if not self.product_list:
            return "\nSystem message: No product found!"
        
        result = ""
        for i, p in enumerate(self.product_list):
            result += f"{i}: Name = {p.name}\n"
            result += f"   Price = {p.price}\n"
        return result

    def update(self, index, name, price):
        if index < 0 or index >= len(self.product_list):
            return "\nSystem message: Invalid index!"
        
        self.product_list[index].update(name, price)
        self.save_data()
        return "\nSystem message: Product updated."

    def delete(self, index):
        if index < 0 or index >= len(self.product_list):
            return "\nSystem message: Invalid index!"
        
        self.product_list.pop(index)
        self.save_data()
        return "\nSystem message: Product deleted."
    

