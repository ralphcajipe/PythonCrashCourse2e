# Parent class
class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"\n{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"\n{self.restaurant_name} is open! Come on in!")


# child class
class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """Initialize an ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


# Make IceCreamStand instance
baskin_robbins = IceCreamStand('Baskin-Robbins')

# Populate flavors in list
baskin_robbins.flavors = ['cotton candy', 'vanilla', 'rocky road']

# Call Methods
baskin_robbins.describe_restaurant()
baskin_robbins.show_flavors()
