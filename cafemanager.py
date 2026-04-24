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