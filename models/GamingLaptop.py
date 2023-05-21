from models.lab1 import AbstractLaptop


class GamingLaptop(AbstractLaptop):
    def __init__(self, model="Unknown", screen_size=15.6, ram=8, storage=256, battery_life=5,
                 graphics_processor="NVIDIA", fan_count=2):
        super().__init__(model, screen_size, ram, storage, battery_life)
        self.graphics_processor = graphics_processor
        self.fan_count = fan_count

    def replace_battery(self, capacity_in_hours):
        self.battery_life = capacity_in_hours

    def __str__(self):
        return super().__str__() + f", Graphics Processor: {self.graphics_processor}, Fan Count: {self.fan_count}"
