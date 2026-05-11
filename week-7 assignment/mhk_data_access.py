import os

FILE_PATH = 'products.txt'

def save_to_file(products):
    with open(FILE_PATH, 'w') as f:
        for p in products:
            f.write(f"{p['name']},{p['price']}\n")
        
def load_from_file():
    products = []
    if not os.path.exists(FILE_PATH):
        return products
    
    try:
        with open(FILE_PATH, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    name, price = line.split(',')
                    products.append({'name': name, 'price': price})
    except Exception as e:
        print(f"Error loading file: {e}")
        
    return products
