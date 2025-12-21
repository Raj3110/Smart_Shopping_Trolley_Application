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