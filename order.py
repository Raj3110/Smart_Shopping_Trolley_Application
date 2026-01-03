import random
import csv
import os
from collections import defaultdict
from datetime import date
from storage import load_orders, save_orders
from utils import audit, timestamp
from security import validate_card_number, validate_cvv, validate_expiry




# ===============================
# HELPER FUNCTIONS
# ===============================

def _generate_order_id():
    return f"ORD{random.randint(10000, 99999)}"


def calculate_tax(amount):
    """GST calculation (2.5% CGST + 2.5% SGST)"""
    cgst = amount * 0.025
    sgst = amount * 0.025
    return cgst, sgst, cgst + sgst





# ===============================
# CHECKOUT
# ===============================

def checkout(cart, contact):
    if not cart:
        print("Cart empty.")
        return

    subtotal = sum(item["price"] * item["quantity"] for item in cart)
    discount_total = 0.0

    for item in cart:
        if item["quantity"] >= 5:
            discount_total += item["price"] * item["quantity"] * 0.10

    if subtotal >= 100:
        discount_total += 10

    past_orders = load_orders()
    if sum(1 for o in past_orders if o["customer"] == contact) >= 3:
        discount_total += subtotal * 0.05

    taxable = subtotal - discount_total
    cgst, sgst, tax_total = calculate_tax(taxable)
    final_total = taxable + tax_total

    # Payment (simplified success assumed here)
    method = input("\nPayment (card/cash): ").lower()
    if method == "card":
        while True:
            card = input("Card number (16 digits): ")
            if not validate_card_number(card):
                print("Invalid card.")
                continue
            expiry = input("Expiry (MM/YY): ")
            if not validate_expiry(expiry):
                print("Invalid expiry.")
                continue
            cvv = input("CVV: ")
            if not validate_cvv(cvv):
                print("Invalid CVV.")
                continue
            break

    order = {
        "order_id": _generate_order_id(),
        "customer": contact,
        "items": cart.copy(),
        "subtotal": subtotal,
        "discount": discount_total,
        "tax": {"cgst": cgst, "sgst": sgst, "total": tax_total},
        "total": final_total,
        "payment": method,
        "time": timestamp()
    }

    orders = load_orders()
    orders.append(order)
    save_orders(orders)

    audit(f"Order {order['order_id']} placed by {contact}")
    cart.clear()

def print_receipt(order):
    print("\n" + "=" * 50)
    print("               SMART MART")
    print("         Smart Shopping Trolley System")
    print("=" * 50)
    print(f"Receipt No   : {order['order_id']}")
    print(f"Date & Time  : {order['time']}")
    print(f"Customer     : {order['customer']}")
    print(f"Payment Mode : {order['payment'].upper()}")
    print("Transaction  : SUCCESS")
    print("-" * 50)
    print("{:<18} {:<5} {:<10} {:<10}".format(
        "Item", "Qty", "Price", "Total"
    ))
    print("-" * 50)

    for item in order["items"]:
        line_total = item["price"] * item["quantity"]
        print("{:<18} {:<5} {:<10.2f} {:<10.2f}".format(
            item["name"],
            item["quantity"],
            item["price"],
            line_total
        ))

    print("-" * 50)
    print(f"{'Subtotal':<35} ₹{order['subtotal']:.2f}")
    print(f"{'Discount':<35} -₹{order['discount']:.2f}")
    print(f"{'CGST (2.5%)':<35} ₹{order['tax']['cgst']:.2f}")
    print(f"{'SGST (2.5%)':<35} ₹{order['tax']['sgst']:.2f}")
    print("-" * 50)
    print(f"{'TOTAL PAYABLE':<35} ₹{order['total']:.2f}")
    print("=" * 50)
    print("Thank you for shopping with Smart Mart!")
    print("Visit again")
    print("=" * 50)


