# cart.py
# US7 – Add Item to Cart
# Allows customer to add a product to cart using scanner code

from product import list_products
from utils import audit

def add_to_cart(cart):
    products = list_products()
    if not products:
        return

    code = input("Enter scanner code: ")

    for p in products:
        if p["code"] == code:
            qty_input = input("Enter quantity (default 1): ")

            if qty_input.isdigit() and int(qty_input) > 0:
                quantity = int(qty_input)
            else:
                quantity = 1

            cart.append({
                "name": p["name"],
                "price": p["price"],
                "quantity": quantity
            })

            audit(f"Added to cart: {p['name']} x{quantity}")
            print("Item added.")
            return

    print("Invalid scanner code.")
