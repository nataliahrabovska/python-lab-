from models.gaming_laptop import GamingLaptop
from models.macbook import MacBook
from models.notebook import NoteBook
from models.ultrabook import Ultrabook
from decorators.decorators import CallCountDecorator, ArgumentsCountDecorator


class AbstractLaptopManager:
    """A class representing a manager for abstract laptops."""

    def __init__(self):
        """Initialize the AbstractLaptopManager object."""
        self.laptops = []

    def add_laptop(self, laptop):
        """
        Add a laptop to the manager.

        Args:
            laptop (AbstractLaptop): The laptop object to add.
        """
        self.laptops.append(laptop)

    def main(self):
        """Run the main operations of the laptop manager."""
        # Adding laptops
        self.add_laptop(Ultrabook("Lenovo", 13.3, 8, 512, 10, 1.1, 0.8))
        self.add_laptop(Ultrabook("Xiaomi", 14.0, 16, 128, 7, 0.9, 2.0))
        self.add_laptop(GamingLaptop("HP Gaming", 17.3, 16, 512, 6, "AMD", 3))
        self.add_laptop(GamingLaptop("Victus", 15.6, 8, 512, 9, "RTX", 2))
        self.add_laptop(MacBook("Air", 13.6, 8, 256, 4, "grey", 12))
        self.add_laptop(MacBook("Air Pro", 13.3, 16, 128, 5, "silver", 24))
        self.add_laptop(NoteBook("HP", 12.0, 16, 64, 3, "Ips", 3))
        self.add_laptop(NoteBook("Asus", 16.0, 8, 128, 10, "oled", 4))

        # Print all laptops
        for laptop in self.laptops:
            print(laptop)

        # Enum object
        print()
        print("Enum object")
        print()
        for item in enumerate(self.laptops):
            print(item)

        # Battery replaced
        print()
        print("Battery replaced")
        print()
        self.laptops[3].replace_battery(9)
        print(self.laptops[3])

        # Search by battery life
        print()
        print("Search by battery life")
        print()
        for res in self.find_all_with_battery_life_greater_than(8):
            print(res)

        # Search by fans
        print()
        print("Search by fans")
        print()
        for res in self.find_all_with_fans():
            print(res)

        # Conditional
        print()
        print("Conditional")
        print()
        print(self.satisfies(lambda x: x.battery_life > 2))
        print(self.satisfies(lambda x: x.screen_size > 10))

    @ArgumentsCountDecorator()
    def find_all_with_battery_life_greater_than(self, battery_life):
        """
        Find all laptops with battery life greater than a given value.

        Args:
            battery_life (int): The minimum battery life value.

        Returns:
            list: A list of laptops with battery life greater than the specified value.
        """
        return [x for x in self.laptops if (lambda x: x.battery_life > battery_life)(x)]

    @ArgumentsCountDecorator()
    def find_all_with_fans(self):
        """
        Find all laptops with a GPU.

        Returns:
            list: A list of laptops with a GPU.
        """
        return [x for x in self.laptops if (lambda x: isinstance(x, GamingLaptop) and x.fan_count > 0)(x)]

    @CallCountDecorator()
    def start_all_laptops(self):
        """
        Start all laptops.

        Returns:
            list: A list of strings representing the results of starting each laptop.
        """
        return [x.start() for x in self.laptops]

    @CallCountDecorator()
    def make_enumerable(self):
        """
        Make the laptops enumerable.

        Returns:
            enumerate: An enumerate object for the laptops.
        """
        return enumerate(self.laptops)

    @ArgumentsCountDecorator()
    def make_zip(self):
        """
        Create a zip of laptops and their start results.

        Returns:
            zip: A zip object containing the laptops and their start results.
        """
        return zip(self.laptops, self.start_all_laptops())

    @ArgumentsCountDecorator()
    def satisfies(self, condition):
        """
        Check if a condition is satisfied for all laptops.

        Args:
            condition (function): The condition function to check.

        Returns:
            dict: A dictionary indicating if the condition is satisfied for all and any laptops.
        """
        satisfied = [condition(x) for x in self.laptops]
        return {'all': all(satisfied), 'any': any(satisfied)}

    def __len__(self):
        """
        Get the length of the laptop manager.

        Returns:
            int: The number of laptops in the manager.
        """
        return len(self.laptops)

    def __getitem__(self, item):
        """
        Get a laptop from the manager using indexing.

        Args:
            item (int): The index of the laptop to retrieve.

        Returns:
            AbstractLaptop: The laptop object at the specified index.
        """
        return self.laptops[item]

    def __iter__(self):
        """
        Make the laptop manager iterable.

        Returns:
            iter: An iterator object for the laptops.
        """
        return iter(self.laptops)
