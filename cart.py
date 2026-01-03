from product import list_products
from utils import audit
from order import checkout

def add_to_cart(cart):
    """
    Add a product to the cart using scanner code.
    Supports quantity to make the prototype more realistic.
    """
    products = list_products()
    if not products:
        return

    code = input("Enter scanner code: ")

    for p in products:
        if p["code"] == code:
            qty_input = input("Enter quantity (default 1): ")

            # Quantity validation with safe fallback
            if qty_input.isdigit() and int(qty_input) > 0:
                quantity = int(qty_input)
            else:
                quantity = 1

            # Check if item already exists in cart
            for item in cart:
                if item["name"] == p["name"]:
                    item["quantity"] += quantity
                    audit(f"Updated quantity: {p['name']} x{quantity}")
                    print("Item quantity updated.")
                    return

            # Add new item to cart
            cart.append({
                "name": p["name"],
                "price": p["price"],
                "quantity": quantity
            })

            audit(f"Added to cart: {p['name']} x{quantity}")
            print("Item added.")
            return

    print("Invalid scanner code.")


def remove_from_cart(cart):
    """
    Remove an item or reduce quantity from the cart.
    """
    if not cart:
        print("Cart empty.")
        return

    print("\nCart Items:")
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item['name']} | Qty: {item['quantity']} | Price: {item['price']}")

    try:
        idx = int(input("Item number to remove: ")) - 1
        item = cart[idx]

        qty_input = input("Enter quantity to remove (Enter for full remove): ")

        # Full removal
        if not qty_input:
            removed = cart.pop(idx)
            audit(f"Removed from cart: {removed['name']}")
            print("Item removed from cart.")
            return

        # Partial quantity removal
        if qty_input.isdigit() and int(qty_input) > 0:
            qty = int(qty_input)
            if qty >= item["quantity"]:
                removed = cart.pop(idx)
                audit(f"Removed from cart: {removed['name']}")
                print("Item removed from cart.")
            else:
                item["quantity"] -= qty
                audit(f"Reduced quantity: {item['name']} by {qty}")
                print("Item quantity updated.")
        else:
            print("Invalid quantity.")

    except (ValueError, IndexError):
        print("Invalid selection.")

def view_cart(cart, contact):
    if not cart:
        print("\n Your cart is empty.")
        return

    while True:
        print("\n YOUR CART")
        print("-" * 45)
        print("{:<5} {:<15} {:<5} {:<8} {:<8}".format(
            "No", "Item", "Qty", "Price", "Total"
        ))
        print("-" * 45)

        for i, item in enumerate(cart, start=1):
            total = item["price"] * item["quantity"]
            print("{:<5} {:<15} {:<5} {:<8.2f} {:<8.2f}".format(
                i,
                item["name"],
                item["quantity"],
                item["price"],
                total
            ))

        print("-" * 45)

        print("\nOptions:")
        print("1. Modify quantity")
        print("2. Remove item")
        print("3. Proceed to checkout")
        print("4. Back to menu")

        choice = input("Choice: ")

        # -------------------------
        # Modify quantity
        # -------------------------
        if choice == "1":
            try:
                idx = int(input("Item number: ")) - 1
                if idx < 0 or idx >= len(cart):
                    print("Invalid item number.")
                    continue

                new_qty = int(input("New quantity: "))
                if new_qty <= 0:
                    print("Quantity must be positive.")
                    continue

                cart[idx]["quantity"] = new_qty
                audit(f"Quantity updated for {cart[idx]['name']}")
                print("Quantity updated.")

            except ValueError:
                print("Invalid input.")

        # -------------------------
        # Remove item
        # -------------------------
        elif choice == "2":
            try:
                idx = int(input("Item number to remove: ")) - 1
                if idx < 0 or idx >= len(cart):
                    print("Invalid item number.")
                    continue

                removed = cart.pop(idx)
                audit(f"Removed item from cart: {removed['name']}")
                print(" Item removed.")

                if not cart:
                    print(" Cart is now empty.")
                    return

            except ValueError:
                print("Invalid input.")

        # -------------------------
        # Checkout
        # -------------------------
        elif choice == "3":
            checkout(cart, contact)
            return

        # -------------------------
        # Back
        # -------------------------
        elif choice == "4":
            return

        else:
            print("Invalid choice.")