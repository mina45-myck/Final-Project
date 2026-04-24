class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = float(price)
        self.category = category

    def display(self):
        return f"{self.name} - Rs.{self.price} [{self.category}]"

    def to_file_string(self):
        return f"{self.name},{self.price},{self.category}"