class Laptop:
    instance = None

    def __init__(self, model="Unknown", screen_size=15.6, ram=8, storage=256, battery_life=5):
        self.__battery_level = None
        self.__model = model
        self.__screen_size = screen_size
        self.__ram = ram
        self.__storage = storage
        self.__battery_life = battery_life

    def add_ram(self, value):
        self.__ram += value

    def add_storage(self, value):
        self.__storage += value

    def charge(self):
        self.__battery_level = 100

    def __str__(self):
        return f"Model: {self.__model}, Screen Size: {self.__screen_size}, RAM: {self.__ram}, Storage: {self.__storage}, " \
               f"Battery Life: {self.__battery_life}"

    @staticmethod
    def get_instance():
        if not Laptop.instance:
            Laptop.instance = Laptop()
        return Laptop.instance


laptops = [Laptop() for i in range(4)]
laptops[1] = Laptop("HP", 12.0, 16, 64, 3)
laptops[2], laptops[3] = Laptop.get_instance(), Laptop.get_instance()

for laptop in laptops:
    print(laptop)
