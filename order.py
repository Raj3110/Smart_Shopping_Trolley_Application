from storage import load_orders, save_orders
from utils import audit, timestamp
from collections import defaultdict
from datetime import date



def checkout(cart, contact):
    if not cart:
        print("Cart empty.")
        return

    print("\n BILL DETAILS")
    print("-" * 45)

    subtotal = 0.0
    discount_total = 0.0

    # -------------------------------
    # Item-level calculation
    # -------------------------------
    for item in cart:
        item_total = item["price"] * item["quantity"]
        subtotal += item_total

        # Bulk discount rule (10% if qty >= 5)
        if item["quantity"] >= 5:
            item_discount = item_total * 0.10
            discount_total += item_discount
            print(
                f"{item['name']} x{item['quantity']} = ₹{item_total:.2f} "
                f"(Bulk discount: -₹{item_discount:.2f})"
            )
        else:
            print(f"{item['name']} x{item['quantity']} = ₹{item_total:.2f}")

    # -------------------------------
    # Cart-level discount
    # -------------------------------
    if subtotal >= 100:
        discount_total += 10
        print("Cart Offer Applied: -₹10.00")

    # -------------------------------
    # Coupon discount
    # -------------------------------
    coupon_discount = 0.0
    use_coupon = input("\nDo you have a coupon code? (y/n): ").lower()

    if use_coupon == "y":
        code = input("Enter coupon code: ").upper()

        if code == "SAVE10" and subtotal >= 50:
            coupon_discount = 10
            print("Coupon SAVE10 applied: -₹10.00")
        elif code == "STUDENT5":
            coupon_discount = subtotal * 0.05
            print(f"Coupon STUDENT5 applied: -₹{coupon_discount:.2f}")
        else:
            print("Invalid or ineligible coupon.")

        discount_total += coupon_discount