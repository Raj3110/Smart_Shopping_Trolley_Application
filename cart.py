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

def add_to_cart(cart):
    products = list_products()
    if not products:
        return

    code = input("Enter scanner code: ")

    for p in products:
        if p["code"] == code:
            qty_input = input("Enter quantity (default 1): ")
            quantity = int(qty_input) if qty_input.isdigit() else 1

            for item in cart:
                if item["name"] == p["name"]:
                    item["quantity"] += quantity
                    audit(f"Updated quantity: {p['name']} x{quantity}")
                    print("Item quantity updated.")
                    return

            cart.append({
                "name": p["name"],
                "price": p["price"],
                "quantity": quantity
            })
            return

# US9 – Remove Item from Cart
# Allows customer to remove item or reduce quantity

def remove_from_cart(cart):
    if not cart:
        print("Cart empty.")
        return

    print("\nCart Items:")
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item['name']} | Qty: {item['quantity']}")

    try:
        idx = int(input("Item number to remove: ")) - 1
        item = cart[idx]

        qty_input = input("Enter quantity to remove (Enter for full remove): ")

        if not qty_input:
            cart.pop(idx)
            audit(f"Removed from cart: {item['name']}")
            return

        if qty_input.isdigit():
            qty = int(qty_input)
            if qty >= item["quantity"]:
                cart.pop(idx)
            else:
                item["quantity"] -= qty
    except:
        print("Invalid selection.")
