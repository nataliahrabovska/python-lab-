from abc import ABC, abstractmethod


class AbstractLaptop(ABC):
    """створила клас Laptop, який представляє ноутбук з деякими характеристиками"""
    __instance = None

    def __init__(self, model="Unknown", screen_size=15.6, ram=8, storage=256, battery_life=5):
        self.battery_level = None
        self.model = model
        self.screen_size = screen_size
        self.ram = ram
        self.storage = storage
        self.battery_life = battery_life
        """атрибути:
        battery_level заряд батареї в відсотках
        model модель ноутбука
        screen_size розмір екрану
        ram оперативна пам'ять в гігабайтах
        storage кількість пам'яті в гігабайтвх
        battery_life тривалість роботи в годинах
        """

    @abstractmethod
    def replace_battery(self, capacity_in_hours):
        pass

    def add_ram(self, value):
        self.ram += value

    """метод який збільшує обсяг оперативної пам'ять"""

    def add_storage(self, value):
        self.storage += value

    """метод який збільшує обсяг сховища"""

    def charge(self):
        self.battery_level = 100

    """метод який встановлює поточний рівень заряду"""

    def __str__(self):
        return f"Model: {self.model}, Screen Size: {self.screen_size}, RAM: {self.ram}, Storage: {self.storage}, " \
               f"Battery Life: {self.battery_life}"

    """Повертає рядок, що представляє об'єкт класу Laptop у зрозумілому форматі."""

    @staticmethod
    def get_instance():
        if not AbstractLaptop.__instance:
            AbstractLaptop.__instance = AbstractLaptop()
        return AbstractLaptop.__instance

    """статичний метод який повертає екземпляр класу"""
