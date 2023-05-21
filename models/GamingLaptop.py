from models.lab1 import AbstractLaptop


class GamingLaptop(AbstractLaptop):
    """A class representing a gaming laptop, inheriting from AbstractLaptop."""

    def __init__(self, model="Unknown", screen_size=15.6, ram=8, storage=256, battery_life=5,
                 graphics_processor="NVIDIA", fan_count=2):
        super().__init__(model, screen_size, ram, storage, battery_life)
        self.graphics_processor = graphics_processor
        self.fan_count = fan_count

        """
           Initialize the GamingLaptop object.

           Args:
               model (str): The model of the gaming laptop.
               screen_size (float): The screen size in inches.
               ram (int): The RAM capacity in gigabytes.
               storage (int): The storage capacity in gigabytes.
               battery_life (int): The battery life in hours.
               graphics_processor (str): The graphics processor of the gaming laptop.
               fan_count (int): The number of fans in the gaming laptop.
        """

    def replace_battery(self, capacity_in_hours):
        self.battery_life = capacity_in_hours

    """
    Replace the battery of the gaming laptop.

    Args:
        capacity_in_hours (int): The new battery capacity in hours.
    """

    def __str__(self):
        return super().__str__() + f", Graphics Processor: {self.graphics_processor}, Fan Count: {self.fan_count}"

    """
    Return a string representation of the gaming laptop object.

    Returns:
        str: A formatted string representing the gaming laptop.
    """
