# main.py
# US3 – Logout User
# Allows user to safely exit menu and log activity

from utils import audit

def customer_menu(contact):
    cart = []
    while True:
        print("""
1. Add to cart
2. View cart
3. Checkout
4. Logout
""")
        c = input("Choice: ")
        if c == "4":
            audit(f"Customer logout: {contact}")
            break
