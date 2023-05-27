from models.laptop import AbstractLaptop


class Ultrabook(AbstractLaptop):
    """A class representing an Ultrabook, inheriting from AbstractLaptop."""

    def __repr__(self):
        """Return a string representation of the Ultrabook object."""
        return f"Model: {self.model}, Screen Size: {self.screen_size}, RAM: {self.ram}, Storage: {self.storage}, " \
               f"Battery Life: {self.battery_life}, Weight: {self.weight} kg, Thickness: {self.thickness} cm"

    def __init__(self, model="Unknown", screen_size=15.6, ram=8, storage=256, battery_life=5,
                 weight=1.2, thickness=0.5):
        """
        Initialize the Ultrabook object.

        Args:
            model (str): The model of the Ultrabook.
            screen_size (float): The screen size in inches.
            ram (int): The RAM capacity in gigabytes.
            storage (int): The storage capacity in gigabytes.
            battery_life (int): The battery life in hours.
            weight (float): The weight of the Ultrabook in kilograms.
            thickness (float): The thickness of the Ultrabook in centimeters.
        """
        super().__init__(model, screen_size, ram, storage, battery_life)
        self.weight = weight
        self.thickness = thickness

    def replace_battery(self, capacity_in_hours):
        """
        Replace the battery of the Ultrabook (not possible).

        Args:
            capacity_in_hours (int): The new battery capacity in hours.
        """
        print("Battery replacement is not possible for Ultrabooks.")

    def __str__(self):
        """
        Return a string representation of the Ultrabook object.

        Returns:
            str: A formatted string representing the Ultrabook.
        """
        return super().__str__() + f", Weight: {self.weight} kg, Thickness: {self.thickness} cm"
