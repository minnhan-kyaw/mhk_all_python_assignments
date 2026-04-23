from product import Product

class Data:
    def __init__(self):
        self.product_list = []
    def creat(self, name, price):
        product = Product(name, price)
        self.product_list.append(product)
        return("\nSystem message:Product created.")
    
    def retrieve(self):
        if len(self.product_list) == 0:
            return ("\nSystem message:No product found!")
        
        result = ""
        for i, p in enumerate(self.product_list):
            result += f"{i}:Name = {p.name}\n"
            result += f"{i}:Price = {p.price}\n"
        return result
        
    def update(self, index, name, price):
        if index < 0 or index >= len(self.product_list):
            return ("\nSystem message:Invalid index!")
        self.product_list[index].update(name,price)
        return ("\nSystem message:Product updated.")
    
    def delete(self,index):
        if index < 0 or index >= len(self.product_list):
            return ("\nSystem message:Invalid index!")
        self.product_list.pop(index)
        return ("\nSystem message:Product deleted.")