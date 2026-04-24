from person import Person

class Staff(Person):
    def __init__(self, name, staff_id, role):
        super().__init__(name)  # Person class ka constructor call kiya
        self.staff_id = staff_id
        self.role = role

    def display(self):  # Person ka display method override kiya
        super().display()
        print(f"Staff ID: {self.staff_id}, Role: {self.role}")