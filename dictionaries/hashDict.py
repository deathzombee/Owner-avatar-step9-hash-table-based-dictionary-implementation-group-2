from .dictabs import DictAbstract
from .pairD import PairD
from random import shuffle


class HTDict(DictAbstract):
    # Team programming
    def __init__(self):
        # Initialize an empty list to store PairD objects
        self._data = []
        self._size = 0

    # Define print format so we can call print(Node)
    def __str__(self):
        return "{" + ", ".join([str(pair) for pair in self._data]) + "}"

    def __len__(self):
        # Return the number of items stored in the dictionary
        return len(self._data)

    def __contains__(self, key):
        # Return true if key is in the dictionary, False otherwise
        key = self._normalize_key(key)
        return self._find(key) is not None

    # peter vang
    # need to test
    def __getitem__(self, key):
        key = self._normalize_key(key)
        # find will return index thus set to idx
        idx = self._find(key)
        if idx is None:
            raise KeyError("Item does not exist")
        # return the satellite of index of our found key
        return self._data[idx].value

    # Lisa
    def _find(self, key):
        norm_key = self._normalize_key(key)
        # pair is pairD aka a data class, recall enumerate returns index of each tuple
        for index, pair in enumerate(self._data):
            if pair.key == norm_key:
                return index
        return None

    # Lisa
    def __setitem__(self, key, value):
        key = self._normalize_key(key)
        # if no match, find will return None
        index = self._find(key)
        # check if key matches existing key. If yes, update value.
        if index is not None:
            self._data[index].value = value
            return
        else:
            self._data.append(PairD(key, value))
            self._size += 1
            # print(self._data)  # test if works

    # Lisa
    def pop(self, key):
        key = self._normalize_key(key)

        # if key does not exist _find will return none,
        # otherwise it returns index associated with key
        index = self._find(key)

        # if key exists, get rid of
        # that pairD and decrement length
        if index is not None:
            value = self._data[index].value
            del self._data[index]
            self._size -= 1
            return value
        raise KeyError("Key not found")

    # Gabriel
    def _remove(self, key):
        key = self._normalize_key(key)
        index = self._find(key)
        if index is not None:
            del self._data[index]
            self._size -= 1
        else:
            raise KeyError(f"Key {key} not found")

    # Gabriel
    def _normalize_key(self, key):
        """Return a normalized version of the key."""
        key = key.strip().lower()
        return key  # Add this line

    # Peter
    def values(self):
        """Return an iterable of all values in the BSTDict."""
        return (pair.value for pair in self._data)

    def mix(self):
        # Shuffle the data
        shuffle(self._data)

    # Team

    def sort(self):
        """
        Entry point for sorting _data using quicksort.

        Explanation:
        - Sets up the pivot and partitions _data into left and right.
        - Recursively sorts each partition by calling rl.
        - Combines the sorted left, pivot, and sorted right into _data.
        """
        if len(self._data) <= 1:
            return self._data

        # Use rl to sort _data directly
        self._data = self.rl(self._data)
        return self._data

    # lisa
    # using this resource https://www.geeksforgeeks.org
    # /python-program-for-quicksort/
    def rl(self, data):
        if len(data) <= 1:
            return data
        # Use the pivot function for consistency
        pivot = self.pivot(data)

        # Split data based on pivot's value attribute
        left = [sat for sat in data if sat.key < pivot.key]
        right = [sat for sat in data if sat.key > pivot.key]

        # Recursively sort left and right, with pivot in the center
        return self.rl(left) + [pivot] + self.rl(right)

    # note should probably choose the middle value as the pivot
    # peter
    def pivot(self, data):
        # set the middle index of array to pivot
        middle = len(data) // 2
        return data[middle]
