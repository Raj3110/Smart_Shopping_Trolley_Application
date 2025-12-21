# auth.py
# US1 – Customer Login
# This function allows a customer to log in using OTP verification

from utils import generate_otp, audit

def customer_login():
    contact = input("Enter contact number: ")
    otp = generate_otp()
    print(f"OTP (demo): {otp}")

    entered = input("Enter OTP: ")
    if entered == str(otp):
        audit(f"Customer login success: {contact}")
        print(f"\n🎉 Welcome to Smart Mart, {contact}! Happy shopping 🛒\n")
        return contact
    else:
        print("Invalid OTP.")
        return None
