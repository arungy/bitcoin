"""An class that can be used to represent a restaurant"""

import sys

class Restaurant:
    """An attempt to model the restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name.title()} serves {self.cuisine_type} food to your taste bud.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is Open.")
        
    def read_customer_served(self):
        print(f"{self.restaurant_name.title()} serving {self.number_served} customers at the moment.")
    
    def total_customer_served(self):
        print(f"{self.restaurant_name.title()} were served {self.number_served} customers in a day of business.")
        
    def set_number_served(self, number_served):
        if number_served > self.number_served:
            self.number_served = number_served
    
    def increment_number_served(self, number_served):
        self.number_served += number_served

def main():
    an_restaurant = Restaurant("tamrind", "andhra")
    ch_restaurant = Restaurant("hongkong noodels", "chinese")
    ta_restaurant = Restaurant("adayar anadh bhavan", "vegetarian")

    an_restaurant.describe_restaurant()
    an_restaurant.read_customer_served()
    
    an_restaurant.set_number_served(13)
    an_restaurant.read_customer_served()
    
    an_restaurant.increment_number_served(501)
    an_restaurant.total_customer_served()
    
    ch_restaurant.describe_restaurant()
    ta_restaurant.describe_restaurant()
    
if __name__ == '__main__':
    main()
    sys.exit(1)

