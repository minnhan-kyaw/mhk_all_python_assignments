import mhk_data_access

def get_all_products():
    return mhk_data_access.load_from_file()

def add_product(name, price):
    if not name or not price:
        return False
    
    products = mhk_data_access.load_from_file()
    products.append({"name": name, "price": price})
    mhk_data_access.save_to_file(products)
    return True

def delete_product(index):
    products = mhk_data_access.load_from_file()
    if 0 <= index < len(products):
        products.pop(index)
        mhk_data_access.save_to_file(products)
        return True
    
def get_product_by_index(index):
    products = mhk_data_access.load_from_file()
    if 0 <= index < len(products):
        return products[index]
    return None

def update_product(index, name, price):
    products = mhk_data_access.load_from_file()
    if 0 <= index < len(products):
        products[index] = {"name": name, "price": price}
        mhk_data_access.save_to_file(products)
        return True
    return False