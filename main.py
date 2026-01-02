from storage import init_storage
from auth import customer_login, admin_login
from cart import add_to_cart, remove_from_cart, view_cart
from order import checkout, view_orders, sales_analytics, export_analytics_csv
from product import add_product, update_product
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
        if c == "1":
            add_to_cart(cart)
        elif c == "2":
            view_cart(cart, contact)
        elif c == "3":
            checkout(cart, contact)
        elif c == "4":
            audit(f"Customer logout: {contact}")
            break

def admin_menu():
    while True:
        print("""
Admin Menu
1. Add product
2. Update product
3. View orders
4. Sales & Analytics Report
5. Export Analytics to CSV
6. Logout
""")
        c = input("Choice: ")
        if c == "1":
            add_product()
        elif c == "2":
            update_product()
        elif c == "3":
            view_orders()
        elif c == "4":
            sales_analytics()
        elif c == "5":
            export_analytics_csv()
        elif c == "6":
            audit("Admin logout")
            break



def main():
    init_storage()
    while True:
        print("""
Smart Shopping Trolley
1. Customer Login
2. Admin Login
3. Exit
""")
        c = input("Choice: ")
        if c == "1":
            contact = customer_login()
            if contact:
                customer_menu(contact)
        elif c == "2":
            if admin_login():
                admin_menu()
        elif c == "3":
            break

if __name__ == "__main__":
    main()
