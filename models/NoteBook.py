from models.laptop import AbstractLaptop


class NoteBook(AbstractLaptop):
    """A class representing a notebook, inheriting from AbstractLaptop."""

    def __init__(self, model="Unknown", screen_size=15.6, ram=8, storage=256, battery_life=5, matrix_type="Ips",
                 ghz=3):
        """
        Initialize the NoteBook object.

        Args:
            model (str): The model of the notebook.
            screen_size (float): The screen size in inches.
            ram (int): The RAM capacity in gigabytes.
            storage (int): The storage capacity in gigabytes.
            battery_life (int): The battery life in hours.
            matrix_type (str): The type of display matrix.
            ghz (float): The processor speed in gigahertz.
        """
        super().__init__(model, screen_size, ram, storage, battery_life)
        self.matrixType = matrix_type
        self.ghz = ghz

    def replace_battery(self, capacity_in_hours):
        """
        Replace the battery of the notebook.

        Args:
            capacity_in_hours (int): The new battery capacity in hours.
        """
        self.battery_life = capacity_in_hours

    def __str__(self):
        """
        Return a string representation of the notebook object.

        Returns:
            str: A formatted string representing the notebook.
        """
        return super().__str__() + f", Matrix Type: {self.matrixType}, GHZ: {self.ghz}"
