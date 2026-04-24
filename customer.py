from person import Person

class Customer(Person):
    def __init__(self, name, customer_id):
        super().__init__(name)  # Person class ka constructor call
        self.customer_id = customer_id
        self.order_history = []

    def display(self):  # Person ka display method override
        super().display()
        print(f"Customer ID: {self.customer_id}")

    def add_order(self, order):
        self.order_history.append(order)