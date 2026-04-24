"""
SmartCafe Management System
Final Project - ICS Computer Science
Developer: Minal
"""
from cafemanager import CafeManager
from staff import Staff
from customer import Customer

print("=== SMARTCAFE SYSTEM STARTING ===")

# 1. File handling test
print("\n1. Testing File Handling:")
cafe = CafeManager()
cafe.display_menu()

# 2. Add new item test
print("\n2. Testing Add Item:")
cafe.add_item("Pizza", 450, "Fast Food")
cafe.display_menu()

# 3. Inheritance test
print("\n3. Testing Inheritance:")
s1 = Staff("Ali", "S001", "Manager")
c1 = Customer("Sara", "C001")

print("\nStaff Details:")
s1.display()
print("\nCustomer Details:")
c1.display()

print("\n=== ALL TESTS COMPLETE ===")
print("\n--- Testing Search ---")
cafe.search_item("Pizza")
cafe.search_item("Burger")
print("\n--- Testing Update Price ---")
cafe.update_price("Pizza", 500)
cafe.display_menu()
print("\n--- Fast Food Items ---")
for item in cafe.menu:
    if item.category == "Fast Food":
        print(f"{item.name} - Rs.{item.price}")
print("\n--- Total Menu Value ---")
total = 0
for item in cafe.menu:
    total += item.price
print(f"Total value of all items: Rs.{total}")
print("\n--- Menu Summary ---")
print(f"Total items in menu: {len(cafe.menu)}")