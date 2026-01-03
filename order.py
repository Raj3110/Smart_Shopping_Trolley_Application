import random
import csv
import os
from collections import defaultdict
from datetime import date
from storage import load_orders, save_orders
from utils import audit, timestamp
from security import validate_card_number, validate_cvv, validate_expiry
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False



RECEIPT_DIR = "receipts"


# ===============================
# HELPER FUNCTIONS
# ===============================

# generated prder ID prior development
def _generate_order_id():
    return f"ORD{random.randint(10000, 99999)}"


def calculate_tax(amount):
    """GST calculation (2.5% CGST + 2.5% SGST)"""
    cgst = amount * 0.025
    sgst = amount * 0.025
    return cgst, sgst, cgst + sgst


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


def save_receipt_txt(order):
    os.makedirs(RECEIPT_DIR, exist_ok=True)
    path = os.path.join(RECEIPT_DIR, f"{order['order_id']}.txt")

    with open(path, "w", encoding="utf-8") as f:
        f.write("SMART MART\n")
        f.write("Smart Shopping Trolley System\n")
        f.write("=" * 40 + "\n")
        f.write(f"Receipt No : {order['order_id']}\n")
        f.write(f"Date       : {order['time']}\n")
        f.write(f"Customer   : {order['customer']}\n")
        f.write(f"Payment    : {order['payment'].upper()}\n")
        f.write("-" * 40 + "\n")

        for item in order["items"]:
            total = item["price"] * item["quantity"]
            f.write(f"{item['name']} x{item['quantity']} = ₹{total:.2f}\n")

        f.write("-" * 40 + "\n")
        f.write(f"Subtotal   : ₹{order['subtotal']:.2f}\n")
        f.write(f"Discount   : -₹{order['discount']:.2f}\n")
        f.write(f"CGST (2.5%): ₹{order['tax']['cgst']:.2f}\n")
        f.write(f"SGST (2.5%): ₹{order['tax']['sgst']:.2f}\n")
        f.write("-" * 40 + "\n")
        f.write(f"TOTAL      : ₹{order['total']:.2f}\n")
        f.write("=" * 40 + "\n")

    print(f" Receipt saved as text: {path}")


def save_receipt_pdf(order):
    if not PDF_AVAILABLE:
        print(" PDF receipt not available (reportlab not installed).")
        return

    os.makedirs(RECEIPT_DIR, exist_ok=True)
    filename = os.path.join(RECEIPT_DIR, f"{order['order_id']}.pdf")

    c = canvas.Canvas(filename, pagesize=A4)
    text = c.beginText(40, 800)


    lines = [
        "SMART MART",
        "Smart Shopping Trolley System",
        "=" * 40,
        f"Receipt No : {order['order_id']}",
        f"Date       : {order['time']}",
        f"Customer   : {order['customer']}",
        f"Payment    : {order['payment'].upper()}",
        "-" * 40,
    ]

    for item in order["items"]:
        total = item["price"] * item["quantity"]
        lines.append(f"{item['name']} x{item['quantity']} = ₹{total:.2f}")

    lines.extend([
        "-" * 40,
        f"Subtotal   : ₹{order['subtotal']:.2f}",
        f"Discount   : -₹{order['discount']:.2f}",
        f"CGST (2.5%): ₹{order['tax']['cgst']:.2f}",
        f"SGST (2.5%): ₹{order['tax']['sgst']:.2f}",
        "-" * 40,
        f"TOTAL      : ₹{order['total']:.2f}",
        "=" * 40,
        "Thank you! Visit again."
    ])

    for line in lines:
        text.textLine(line)

    c.drawText(text)
    c.showPage()
    c.save()

    print(f" Receipt saved as PDF: {filename}")


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

    #loading orders also done
    orders = load_orders()
    orders.append(order)
    save_orders(orders)

    audit(f"Order {order['order_id']} placed by {contact}")
    cart.clear()

    # Receipt choice
    choice = input(
        "\nReceipt options:\n"
        "1. Print on screen\n"
        "2. Save as text\n"
        "3. Save as PDF\n"
        "4. Skip\n"
        "Choice: "
    )

    if choice == "1":
        print_receipt(order)
    elif choice == "2":
        save_receipt_txt(order)
    elif choice == "3":
        if PDF_AVAILABLE:
            save_receipt_pdf(order)
        else:
            print("PDF option unavailable on this system.")

# ===============================
# ADMIN / ANALYTICS FUNCTIONS
# ===============================

def view_orders():
    orders = load_orders()
    if not orders:
        print("No orders.")
        return

    print("\n{:<10} {:<15} {:<8} {:<10} {}".format(
        "ORDER ID", "CONTACT", "PAYMENT", "TOTAL", "DATE"
    ))
    print("-" * 70)

    updated = False

    for idx, o in enumerate(orders, start=1):
        if "order_id" not in o:
            o["order_id"] = f"LEGACY{idx:04d}"
            updated = True

        print("{:<10} {:<15} {:<8} {:<10} {}".format(
            o["order_id"],
            o["customer"],
            o["payment"],
            f"{o['total']} (−{o.get('discount', 0)})",
            o["time"]
        ))

    if updated:
        save_orders(orders)

def sales_analytics():
    orders = load_orders()
    if not orders:
        print("No orders available for analytics.")
        return

    customer_stats = defaultdict(lambda: {"orders": 0, "total": 0.0})
    today = str(date.today())

    today_revenue = 0.0
    today_orders = 0
    payment_split = {"card": 0.0, "cash": 0.0}
    total_revenue = 0.0

    for o in orders:
        contact = o["customer"]
        total = o["total"]

        customer_stats[contact]["orders"] += 1
        customer_stats[contact]["total"] += total
        total_revenue += total

        if o["time"].startswith(today):
            today_revenue += total
            today_orders += 1
            payment_split[o["payment"]] += total

    print("\n REPEATED CUSTOMERS")
    print("{:<15} {:<10} {:<12} {:<12}".format(
        "CONTACT", "ORDERS", "TOTAL SPENT", "AVG ORDER"
    ))
    print("-" * 55)

def export_analytics_csv(filename="sales_analytics.csv"):
    orders = load_orders()
    if not orders:
        print("No data to export.")
        return
    for o in orders:
        contact = o["customer"]
        total = o["total"]

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Order ID", "Customer", "Payment",
            "Subtotal", "Discount", "Total", "Date"
        ])

        for o in orders:
            writer.writerow([
                o.get("order_id", "NA"),
                o["customer"],
                o["payment"],
                o.get("subtotal", 0),
                o.get("discount", 0),
                o["total"],
                o["time"]
            ])

    print(f" Analytics exported successfully to {filename}")
