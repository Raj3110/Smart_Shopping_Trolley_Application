from utils import generate_otp, audit


ADMIN_USER = "admin"
ADMIN_PASS = "admin@123"

def customer_login():
    contact = input("Enter contact number: ")
    otp = generate_otp()
    print(f"OTP (demo): {otp}")

    entered = input("Enter OTP: ")
    if entered == str(otp):
        audit(f"Customer login success: {contact}")
        print(f"\n Welcome to Smart Mart, {contact}! Happy shopping 🛒\n")
        return contact
    else:
        print("Invalid OTP.")
        return None
    
def admin_login():
    user = input("Username: ")
    pwd = input("Password: ")

    if user == ADMIN_USER and pwd == ADMIN_PASS:
        audit("Admin login success")
        return True
    else:
        print("Invalid admin credentials.")
        return False
