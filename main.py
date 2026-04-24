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