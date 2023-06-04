class SetManager:
    """A class representing a set manager for laptops."""

    def __init__(self, laptops):
        """
        Initialize the SetManager object.

        Args:
            laptops (list): A list of laptops.
        """
        self.components = {component for laptop in laptops for component in laptop.components}
        self.icomponents = iter(self.components)

    def __len__(self):
        """
        Get the length of the set manager.

        Returns:
            int: The number of unique components in the manager.
        """
        return len(self.components)

    def __getitem__(self, item):
        """
        Get a component from the set manager using indexing.

        Args:
            item (int): The index of the component to retrieve.

        Returns:
            object: The component object at the specified index.
        """
        return list(self.components)[item]

    def __iter__(self):
        """
        Make the set manager iterable.

        Returns:
            iter: An iterator object for the components.
        """
        return iter(self.components)

    def __next__(self):
        """
        Get the next component from the set manager.

        Returns:
            object: The next component object.
        """
        return next(self.icomponents)
