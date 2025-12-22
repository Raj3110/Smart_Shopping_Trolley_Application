from storage import load_products , save_products

def list_products():
    products = load_products()
    if not products:
        print("No products available.")
        return []

    print("\nProducts:")
    for i, p in enumerate(products, 1):
        print(f"{i}. {p['name']} | €{p['price']} | Code: {p['code']}")
    return products

def add_product():
    products = load_products()

    name = input("Product name: ")
    price = float(input("Price: "))
    code = input("Scanner code (5 digits): ")

    for p in products:
        if p["code"] == code:
            print("❌ Scanner code already exists.")
            return

    products.append({
        "name": name,
        "price": price,
        "code": code
    })

    save_products(products)
    print("✅ Product added successfully.")


def update_product():
    products = list_products()
    if not products:
        return

    try:
        idx = int(input("Select product number: ")) - 1
        p = products[idx]

        name = input("New name (Enter to skip): ")
        price = input("New price (Enter to skip): ")
        code = input("New code (Enter to skip): ")

        if name:
            p["name"] = name
        if price:
            p["price"] = float(price)
        if code:
            p["code"] = code

        save_products(products)
    except:
        print("Invalid selection.")