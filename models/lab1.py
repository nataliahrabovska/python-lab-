from abc import ABC, abstractmethod


class AbstractLaptop(ABC):
    """A class representing a laptop with certain characteristics."""
    __instance = None

    def __init__(self, model="Unknown", screen_size=15.6, ram=8, storage=256, battery_life=5):
        self.battery_level = None
        self.model = model
        self.screen_size = screen_size
        self.ram = ram
        self.storage = storage
        self.battery_life = battery_life
        """
        Initialize the AbstractLaptop object.

        Args:
            model (str): The model of the laptop.
            screen_size (float): The screen size in inches.
            ram (int): The RAM capacity in gigabytes.
            storage (int): The storage capacity in gigabytes.
            battery_life (int): The battery life in hours.
        """

    @abstractmethod
    def replace_battery(self, capacity_in_hours):
        pass

    """
    Abstract method to replace the laptop's battery.

    Args:
        capacity_in_hours (int): The new battery capacity in hours.
    """

    def add_ram(self, value):
        self.ram += value

    """
    Increase the RAM capacity of the laptop.

    Args:
        value (int): The amount of RAM to add in gigabytes.
    """

    def add_storage(self, value):
        self.storage += value

    """
    Increase the storage capacity of the laptop.

    Args:
        value (int): The amount of storage to add in gigabytes.
    """

    def charge(self):
        self.battery_level = 100

    """Set the battery level of the laptop to 100."""

    def __str__(self):
        return f"Model: {self.model}, Screen Size: {self.screen_size}, RAM: {self.ram}, Storage: {self.storage}, " \
               f"Battery Life: {self.battery_life}"

    """
    Return a string representation of the laptop object.

    Returns:
        str: A formatted string representing the laptop.
    """

    @staticmethod
    def get_instance():
        if not AbstractLaptop.__instance:
            AbstractLaptop.__instance = AbstractLaptop()
        return AbstractLaptop.__instance

    """
   Get the singleton instance of the AbstractLaptop class.

   Returns:
       AbstractLaptop: The singleton instance.
    """
