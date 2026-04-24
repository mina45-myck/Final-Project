from menuitem import MenuItem

class CafeManager:
    def __init__(self):
        self.menu = []
        self.load_menu()

    def load_menu(self, filename="data/menu.txt"):
        try:
            with open(filename, "r") as f:
                for line in f:
                    name, price, category = line.strip().split(",")
                    self.menu.append(MenuItem(name, float(price), category))
            print("Menu loaded successfully!")
        except FileNotFoundError:
            print("No menu file found.")
    def save_menu(self, filename="data/menu.txt"):
          with open(filename, "w") as f:
            for item in self.menu:
                f.write(item.to_file_string() + "\n")
    print("Menu saved to file!")
    def display_menu(self):
        if not self.menu:
            print("Menu is empty.")
            return
        print("\n--- CAFE MENU ---")
        for i, item in enumerate(self.menu, 1):
            print(f"{i}. {item.display()}")
        print("-----------------\n")
    def add_item(self, name, price, category):
           try:
            new_item = MenuItem(name, price, category)
            self.menu.append(new_item)
            self.save_menu()
            print(f"Added: {name} successfully!")
           except ValueError:
            print("Error: Price must be a number.")
    def remove_item(self, item_name):
        for item in self.menu:
            if item.name.lower() == item_name.lower():
                self.menu.remove(item)
                self.save_menu()
                print(f"Removed: {item_name} successfully!")
                return
        print(f"Error: {item_name} not found in menu.")       
       
    def search_item(self, name):
          for item in self.menu:
            if item.name.lower() == name.lower():
                print(f"Found: {item.name} - Rs.{item.price} - {item.category}")
                return item
            print(f"Item '{name}' not found in menu")
            
          return None
    def update_price(self, name, new_price):
        item = self.search_item(name)
        if item:
            old_price = item.price
            item.price = new_price
            self.save_menu()
            print(f"Price updated: {name} Rs.{old_price} -> Rs.{new_price}")
            return True
        print(f"Cannot update. Item '{name}' not found")
        return False