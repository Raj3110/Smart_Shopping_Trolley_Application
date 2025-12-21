# product.py
# US4 – View Product Catalog
# Displays all available products to the user

from storage import load_products

def list_products():
    products = load_products()
    if not products:
        print("No products available.")
        return []

    print("\nProducts:")
    for i, p in enumerate(products, 1):
        print(f"{i}. {p['name']} | €{p['price']} | Code: {p['code']}")
    return products
