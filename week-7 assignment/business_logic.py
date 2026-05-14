import data_access

def get_all_products():
    return data_access.load_from_file()

def add_product(name, price):
    if not name or name.isdigit():
        return False, "Invalid Name! Product name must not be numbers or empty."
    try:
        price = float(price)
        if price <= 0:
            return False, "Price must be a positive number."
    except ValueError:
        return False, "Invalid price format."
    products = data_access.load_from_file()
    products.append({"name": name, "price": price})
    data_access.save_to_file(products)
    return True, "Product added successfully!"


def update_product(index, name, price):
    if not name or name.isdigit():
        return False, "Update failed: Invalid product name."
    products = data_access.load_from_file()

    if 0 <= index < len(products):
        products[index] = {"name": name, "price": price}
        data_access.save_to_file(products)
        return True, "Product updated successfully!" 
    return False, "Product not found."

def delete_product(index):
    products = data_access.load_from_file()
    if 0 <= index < len(products):
        deleted_item = products.pop(index)
        data_access.save_to_file(products)
        return True, "Product has been deleted."
    return False, "Delete failed: Product not found."

def get_product_by_index(index):
    products = data_access.load_from_file()
    if 0 <= index < len(products):
        return products[index]
    return None