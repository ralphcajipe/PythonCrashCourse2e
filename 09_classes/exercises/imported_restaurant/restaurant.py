"""A class representing a restaurant."""


class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
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
