from models.GamingLaptop import GamingLaptop
from models.MacBook import MacBook
from models.NoteBook import NoteBook
from models.Ultrabook import Ultrabook


class AbstractLaptopManager:
    """A class for managing a collection of laptops."""

    def __init__(self):
        """Initialize the AbstractLaptopManager object."""
        self.laptops = []

    def add_laptop(self, laptop):
        """
        Add a laptop to the manager.

        Args:
            laptop (AbstractLaptop): The laptop object to be added.
        """
        self.laptops.append(laptop)

    def find_all_with_weight_greater_than(self, weight):
        """
        Find all Ultrabooks with weight greater than the specified value.

        Args:
            weight (float): The weight threshold.

        Returns:
            list: A list of Ultrabook objects with weight greater than the specified value.
        """
        return list(filter(lambda laptop: isinstance(laptop, Ultrabook) and laptop.weight > weight, self.laptops))

    def find_with_fans(self):
        """
        Find all gaming laptops with fans.

        Returns:
            list: A list of GamingLaptop objects with fans.
        """
        return list(filter(lambda laptop: isinstance(laptop, GamingLaptop) and laptop.fan_count > 0, self.laptops))

    def print_laptops(self):
        """Print the details of all laptops in the manager."""
        for laptop in self.laptops:
            print(laptop)
            print()


laptop_manager = AbstractLaptopManager()

gaming_laptop = GamingLaptop("HP Gaming", 17.3, 16, 512, 6, "AMD", 3)
ultrabook = Ultrabook("Lenovo", 13.3, 8, 512, 10, 1.1, 0.8)
macbook = MacBook("Air", 13.6, 8, 256, 4, "grey", 12)
notebook = NoteBook("HP", 12.0, 16, 64, 3, "Ips", 3)

laptop_manager.add_laptop(gaming_laptop)
laptop_manager.add_laptop(ultrabook)
laptop_manager.add_laptop(macbook)
laptop_manager.add_laptop(notebook)

print("All Laptops:")
laptop_manager.print_laptops()

print("Ultrabooks with weight greater than 1.2 kg:")
ultrabooks = laptop_manager.find_all_with_weight_greater_than(1.2)
for ultrabook in ultrabooks:
    print(ultrabook)

print("Gaming laptops with fans:")
gaming_laptops = laptop_manager.find_with_fans()
for gaming_laptop in gaming_laptops:
    print(gaming_laptop)
