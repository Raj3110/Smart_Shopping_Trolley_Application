# US13 – Calculate Cart Subtotal
# Calculates total price of all items in the cart

def checkout(cart, contact):
    if not cart:
        print("Cart empty.")
        return

    subtotal = sum(item["price"] * item["quantity"] for item in cart)