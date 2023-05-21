from models.lab1 import AbstractLaptop


class Ultrabook(AbstractLaptop):
    def __init__(self, model="Unknown", screen_size=15.6, ram=8, storage=256, battery_life=5,
                 weight=1.2, thickness=0.5):
        super().__init__(model, screen_size, ram, storage, battery_life)
        self.weight = weight
        self.thickness = thickness

    def replace_battery(self, capacity_in_hours):
        print("Battery replacement is not possible for Ultrabooks.")

    def __str__(self):
        return super().__str__() + f", Weight: {self.weight} kg, Thickness: {self.thickness} cm"
