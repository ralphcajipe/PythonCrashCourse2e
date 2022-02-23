class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"\n{self.restaurant_name} is a {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"\n{self.restaurant_name} is open! Come on in!")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


# make Instance
restaurant = Restaurant('ultimate shawarma', 'middle eastern')
restaurant.describe_restaurant()

# Print number of customers the restaurant has served
print(f"\nNumber served: {restaurant.number_served}")

# Change value
restaurant.number_served = 100
print(f"Number served: {restaurant.number_served}")

# Use set_number_served(self, number_served) Method
restaurant.set_number_served(250)
print(f"Number served: {restaurant.number_served}")

# Use increment_number_served(self, additional_served) Method
restaurant.increment_number_served(50)
print(f"Number served: {restaurant.number_served}")
