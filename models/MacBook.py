from models.lab1 import AbstractLaptop


class MacBook(AbstractLaptop):
    def __init__(self, model="Unknown", screen_size=15.6, ram=8, storage=256, battery_life=5, color="grey",
                 guarantee=12):
        super().__init__(model, screen_size, ram, storage, battery_life)
        self.color = color
        self.guarantee = guarantee

    def replace_battery(self, capacity_in_hours):
        print("Battery replacement is not possible for Ultrabooks.")

    def __str__(self):
        return super().__str__() + f", Color: {self.color} , Guarantee In Month: {self.guarantee} "
