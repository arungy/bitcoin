"""A class than can be used to represent privileges"""

class Privileges:
    """An simple attempt to model privileges"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.privileges_data = []

    def show_privileges(self):
        print(f"Admin {self.first_name.title()} {self.last_name.title()}")
        for p in self.privileges_data:
            print(f" {p}")
