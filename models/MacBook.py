from models.laptop import AbstractLaptop


class MacBook(AbstractLaptop):
    """A class representing a MacBook, inheriting from AbstractLaptop."""

    def __repr__(self):
        """Return a string representation of the MacBook object."""
        return f"Model: {self.model}, Screen Size: {self.screen_size}, RAM: {self.ram}, Storage: {self.storage}, " \
               f"Battery Life: {self.battery_life}, Color: {self.color}, Guarantee In Month: {self.guarantee}"

    def __init__(self, model="Unknown", screen_size=15.6, ram=8, storage=256, battery_life=5, color="grey",
                 guarantee=12):
        """
        Initialize the MacBook object.

        Args:
            model (str): The model of the MacBook.
            screen_size (float): The screen size in inches.
            ram (int): The RAM capacity in gigabytes.
            storage (int): The storage capacity in gigabytes.
            battery_life (int): The battery life in hours.
            color (str): The color of the MacBook.
            guarantee (int): The guarantee period in months.
        """
        super().__init__(model, screen_size, ram, storage, battery_life)
        self.color = color
        self.guarantee = guarantee

    def replace_battery(self, capacity_in_hours):
        """
        Replace the battery of the MacBook (not possible).

        Args:
            capacity_in_hours (int): The new battery capacity in hours.
        """
        print("Battery replacement is not possible for MacBooks.")

    def __str__(self):
        """
        Return a string representation of the MacBook object.

        Returns:
            str: A formatted string representing the MacBook.
        """
        return super().__str__() + f", Color: {self.color}, Guarantee In Month: {self.guarantee}"
