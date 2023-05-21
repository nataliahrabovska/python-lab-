from models.lab1 import AbstractLaptop


class NoteBook(AbstractLaptop):
    def __init__(self, model="Unknown", screen_size=15.6, ram=8, storage=256, battery_life=5, matrix_type="Ips",
                 ghz=3):
        super().__init__(model, screen_size, ram, storage, battery_life)
        self.matrixType = matrix_type
        self.ghz = ghz

    def replace_battery(self, capacity_in_hours):
        self.battery_life = capacity_in_hours

    def __str__(self):
        return super().__str__() + f", Matrix Type: {self.matrixType}, GHZ: {self.ghz}"
