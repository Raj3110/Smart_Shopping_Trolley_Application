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


