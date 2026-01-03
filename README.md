# Smart_Shopping_Trolley_Application
An intelligent shopping trolley app upgrades the regular cart into a smart assistant with real-time item scanning, self-checkout billing. It displays live totals, enables fast payments, saves time, and enhances convenience while providing data insights to retailers all without using IoT devices.

# how to run 

## run main.py and follow the below teaching mode commands

Smart Shopping Trolley
1. Customer Login
2. Admin Login
3. Exit

Choice: 1
Enter contact number: 12345678
OTP (demo): 9773
Enter OTP: 9773

 Welcome to Smart Mart, 12345678! Happy shopping 


1. Add to cart
2. View cart
3. Checkout
4. Logout

Choice: 1

Products:
1. Apple | €12.0 | Code: 10001
2. Banana | €10.0 | Code: 10002
3. Orange | €15.0 | Code: 10003
4. Grapes | €18.0 | Code: 10004
5. Pineapple | €40.0 | Code: 10005
6. Mango | €30.0 | Code: 10006
7. Watermelon | €45.0 | Code: 10007
.
.
.
98. Lunch Box | €180.0 | Code: 10098
99. Water Bottle | €120.0 | Code: 10099
100. Thermos Flask | €350.0 | Code: 10100
101. laptop | €5000.0 | Code: 99999
Enter scanner code: 99999
Enter quantity (default 1): 1
Item added.

1. Add to cart
2. View cart
3. Checkout
4. Logout

Choice: 2

 YOUR CART
---------------------------------------------
No    Item            Qty   Price    Total
---------------------------------------------
1     laptop          1     5000.00  5000.00
---------------------------------------------

Options:
1. Modify quantity
2. Remove item
3. Proceed to checkout
4. Back to menu
Choice: 1
Item number: 1
New quantity: 2
Quantity updated.

 YOUR CART
---------------------------------------------
No    Item            Qty   Price    Total
---------------------------------------------
1     laptop          2     5000.00  10000.00
---------------------------------------------

Options:
1. Modify quantity
2. Remove item
3. Proceed to checkout
4. Back to menu
Choice: 3

Payment (card/cash): card
Card number (16 digits): 12345678
Invalid card.
Card number (16 digits): 1234567887654321
Expiry (MM/YY): 10/15
Invalid expiry.
Card number (16 digits): 1234567887654321
Expiry (MM/YY): 10/26
CVV: 123

Receipt options:
1. Print on screen
2. Save as text
3. Save as PDF
4. Skip
Choice: 1

==================================================
               SMART MART
         Smart Shopping Trolley System
==================================================
Receipt No   : ORD66494
Date & Time  : 2026-01-03 12:19:02.899377
Customer     : 12345678
Payment Mode : CARD
Transaction  : SUCCESS
--------------------------------------------------
Item               Qty   Price      Total
--------------------------------------------------
laptop             2     5000.00    10000.00
--------------------------------------------------
Subtotal                            ₹10000.00
Discount                            -₹10.00
CGST (2.5%)                         ₹249.75
SGST (2.5%)                         ₹249.75
--------------------------------------------------
TOTAL PAYABLE                       ₹10489.50
==================================================
Thank you for shopping with Smart Mart!
Visit again
==================================================

1. Add to cart
2. View cart
3. Checkout
4. Logout

Choice: 2

 Your cart is empty.

1. Add to cart
2. View cart
3. Checkout
4. Logout

Choice: 3
Cart empty.

1. Add to cart
2. View cart
3. Checkout
4. Logout

Choice: 4

Smart Shopping Trolley
1. Customer Login
2. Admin Login
3. Exit

Choice: 2
Username: admin
Password: admin@123

Admin Menu
1. Add product
2. Update product
3. View orders
4. Sales & Analytics Report
5. Export Analytics to CSV
6. Logout

Choice:

Admin Menu
1. Add product
2. Update product
3. View orders
4. Sales & Analytics Report
5. Export Analytics to CSV
6. Logout

Choice: 3

ORDER ID   CONTACT         PAYMENT  TOTAL      DATE
----------------------------------------------------------------------
ORD66494   12345678        card     10489.5 (−10.0) 2026-01-03 12:19:02.899377

Admin Menu
1. Add product
2. Update product
3. View orders
4. Sales & Analytics Report
5. Export Analytics to CSV
6. Logout

Choice: 4

 REPEATED CUSTOMERS
CONTACT         ORDERS     TOTAL SPENT  AVG ORDER
-------------------------------------------------------

 TODAY'S SALES SUMMARY
Total orders today : 1
Total revenue today: ₹10489.5
Card payments      : ₹10489.5
Cash payments      : ₹0.0

 OVERALL SALES STATISTICS
Total orders       : 1
Total revenue      : ₹10489.5
Average order value: ₹10489.50
Top customer       : 12345678 (1 orders)

Admin Menu
1. Add product
2. Update product
3. View orders
4. Sales & Analytics Report
5. Export Analytics to CSV
6. Logout

Choice: 5
 Analytics exported successfully to sales_analytics.csv

Admin Menu
1. Add product
2. Update product
3. View orders
4. Sales & Analytics Report
5. Export Analytics to CSV
6. Logout

Choice: 6

Smart Shopping Trolley
1. Customer Login
2. Admin Login
3. Exit

Choice: 3

# pytest check

PS C:\Users\smart_trolley> pytest
========================================= test session starts ==========================================
platform win32 -- Python 3.12.5, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\smart_trolley
plugins: anyio-4.0.0
collected 57 items                                                                                      

Smart_Shopping_Trolley_Application\tests\2123456\test\blackbox\test_cart_blackbox.py ........     [ 14%]
Smart_Shopping_Trolley_Application\tests\2123456\test\blackbox\test_checkout_blackbox.py .....    [ 22%]
Smart_Shopping_Trolley_Application\tests\2123456\test\blackbox\test_login_blackbox.py ....        [ 29%]
Smart_Shopping_Trolley_Application\tests\2123456\test\blackbox\test_product_blackbox.py ..        [ 33%] 
Smart_Shopping_Trolley_Application\tests\2123456\test\concolic\test_checkout_concolic.py ...      [ 38%]
Smart_Shopping_Trolley_Application\tests\2123456\test\symbolic\test_checkout_symbolic.py ....     [ 45%] 
Smart_Shopping_Trolley_Application\tests\2123456\test\whitebox\test_cart_whitebox.py ............ [ 66%]
.                                                                                                 [ 68%] 
Smart_Shopping_Trolley_Application\tests\2123456\test\whitebox\test_checkout_whitebox.py ......   [ 78%]
Smart_Shopping_Trolley_Application\tests\2123456\test\whitebox\test_order_additional_whitebox.py . [ 80%]
..                                                                                                [ 84%] 
Smart_Shopping_Trolley_Application\tests\2123456\test\whitebox\test_security_whitebox.py ......   [ 94%]
Smart_Shopping_Trolley_Application\tests\2123456\test\whitebox\test_storage_whitebox.py ...       [100%]

========================================== 57 passed in 0.42s ========================================== 

# coverage report
covered upto 81%


PS C:\Users\smart_trolley> coverage run -m pytest  
========================================= test session starts ==========================================
platform win32 -- Python 3.12.5, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\smart_trolley
plugins: anyio-4.0.0
collected 57 items                                                                                      

Smart_Shopping_Trolley_Application\tests\2123456\test\blackbox\test_cart_blackbox.py ........     [ 14%]
Smart_Shopping_Trolley_Application\tests\2123456\test\blackbox\test_checkout_blackbox.py .....    [ 22%]
Smart_Shopping_Trolley_Application\tests\2123456\test\blackbox\test_login_blackbox.py ....        [ 29%]
Smart_Shopping_Trolley_Application\tests\2123456\test\blackbox\test_product_blackbox.py ..        [ 33%]
Smart_Shopping_Trolley_Application\tests\2123456\test\concolic\test_checkout_concolic.py ...      [ 38%]
Smart_Shopping_Trolley_Application\tests\2123456\test\symbolic\test_checkout_symbolic.py ....     [ 45%]
Smart_Shopping_Trolley_Application\tests\2123456\test\whitebox\test_cart_whitebox.py ............ [ 66%]
.                                                                                                 [ 68%] 
Smart_Shopping_Trolley_Application\tests\2123456\test\whitebox\test_checkout_whitebox.py ......   [ 78%]
Smart_Shopping_Trolley_Application\tests\2123456\test\whitebox\test_order_additional_whitebox.py . [ 80%]
..                                                                                                [ 84%] 
Smart_Shopping_Trolley_Application\tests\2123456\test\whitebox\test_security_whitebox.py ......   [ 94%]
Smart_Shopping_Trolley_Application\tests\2123456\test\whitebox\test_storage_whitebox.py ...       [100%]

========================================== 57 passed in 0.79s ========================================== 
PS C:\Users\smart_trolley> coverage report
Name                                                                                               Stmts   Miss  Cover
----------------------------------------------------------------------------------------------------------------------
Smart_Shopping_Trolley_Application\__init__.py                                                         0      0   100%
Smart_Shopping_Trolley_Application\auth.py                                                            22      0   100%
Smart_Shopping_Trolley_Application\cart.py                                                           107     25    77%
Smart_Shopping_Trolley_Application\order.py                                                          206     91    56%
Smart_Shopping_Trolley_Application\product.py                                                         43      9    79%
Smart_Shopping_Trolley_Application\security.py                                                        15      0   100%
Smart_Shopping_Trolley_Application\storage.py                                                         38     15    61%
Smart_Shopping_Trolley_Application\tests\2123456\__init__.py                                           0      0   100%
Smart_Shopping_Trolley_Application\tests\2123456\test\blackbox\__init__.py                             0      0   100%
Smart_Shopping_Trolley_Application\tests\2123456\test\blackbox\test_cart_blackbox.py                  52      1    98%
Smart_Shopping_Trolley_Application\tests\2123456\test\blackbox\test_checkout_blackbox.py              39      1    97%
Smart_Shopping_Trolley_Application\tests\2123456\test\blackbox\test_login_blackbox.py                 24      1    96%
Smart_Shopping_Trolley_Application\tests\2123456\test\whitebox\test_order_additional_whitebox.py      31      1    97%     
Smart_Shopping_Trolley_Application\tests\2123456\test\whitebox\test_security_whitebox.py              17      1    94%     
Smart_Shopping_Trolley_Application\tests\2123456\test\whitebox\test_storage_whitebox.py               18      1    94%     
Smart_Shopping_Trolley_Application\tests\__init__.py                                                   0      0   100%     
Smart_Shopping_Trolley_Application\tests\conftest.py                                                   5      0   100%     
Smart_Shopping_Trolley_Application\utils.py                                                            9      1    89%     
----------------------------------------------------------------------------------------------------------------------     
TOTAL                                                                                                815    152    81%   