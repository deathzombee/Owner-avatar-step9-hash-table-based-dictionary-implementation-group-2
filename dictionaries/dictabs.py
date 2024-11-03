from abc import abstractmethod
from abc import ABC


# An abstract class representing the blueprint for
# a dictionary
class DictAbstract(ABC):

    # Return the number of items stored in the dictionary
    @abstractmethod
    def __len__(self):
        pass

    # Implementing the python magic method __contains__
    # This will help to use in true or false sentences
    # e.g., if key is in dict
    @abstractmethod
    def __contains__(self, key):
        pass

    # Implementing the python magic method __getitem__
    # This function will help in using this sytax dict[key]
    @abstractmethod
    def __getitem__(self, key):
        pass

    # Implements self[key] = value.  If key is already stored in
    # the dictionary then its value is modified.  If key is not in the map,
    # it is added.
    @abstractmethod
    def __setitem__(self, key, value):
        pass

    # Remove a node from the tree with the indicated key
    # Return the value after removing the node
    # Raise a KeyError if the key is not in the map."
    @abstractmethod
    def pop(self, key):
        pass
