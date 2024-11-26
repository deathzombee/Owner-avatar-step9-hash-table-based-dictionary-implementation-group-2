from .dictabs import DictAbstract
from .pairD import PairD
from random import shuffle


class HTDict(DictAbstract):
    # Team programming
    def __init__(self, capacity=1000):
        # Initialize an empty list to store PairD objects
        # Inititialize two tables for cuckoo hashing
        self._data = []
        self._size = 0
        self._capacity = capacity
        self._table1 = [None] * self.capacity
        self._table2 = [None] * self.capacity

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
        # Normalize key and get index from hash1 & hash2.
        norm_key = self._normalize_key(key)
        index1 = self.hash1(norm_key)
        index2 = self.hash2(norm_key)

        # Checking for key in both hash tables.
        if self._table1[index1] and self._table1[index1].key == norm_key:
            return self._table1[index1].value
        if self._table2[index2] and self._table2[index2].key == norm_key:
            return self._table2[index2].value

        raise KeyError(f"Key '{key}' not found")

    # Lisa CHANGE
    def __setitem__(self, key, value):
        norm_key = self._normalize_key(key)
        pair = PairD(norm_key, value)

        # Insert to table1
        index1 = self.hash1(norm_key)
        if self._table1(index1) is None:
            self._table1[index1] = pair
            self._size += 1
            return
        # Move existing pair to table2
        pair, self._tabl1[index1] = self._table1[index1], pair

        # Insert to table2
        index2 = self.hash2(pair.key)
        if self._table2[index2] is None:
            self._table2[index2] = pair
            self._size += 1
            return
        # Move existing pair
        pair, self._tabl2[index2] = self._table2[index2], pair

    # Lisa
    def pop(self, key):
        norm_key = self._normalize_key(key)
        index1 = self.hash1(norm_key)
        index2 = self.hash2(norm_key)

        # Remove from table 1
        if self._table1[index1] and self._table1[index1].key == key:
            value = self._table1[index1].value
            self._table1[index1] = None
            self._size -= 1
            return value

        # Remove from table 2
        if self._table2[index2] and self._table2[index2].key == key:
            value = self._table2[index2].value
            self._table2[index2] = None
            self._size -= 1
            return value

        raise KeyError("Key '{key}'not found")

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
        ascii_sum = sum(ord(char) for char in key)
        return ascii_sum

    # Peter
    def values(self):
        """Return an iterable of all values in the BSTDict."""
        return (pair.value for pair in self._data)

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

    # Gabriel
    def cuckoo(self, key):
        pass

    # Peter
    def hash1(self, key):
        key = key % 11
        return key

    # Lisa
    def hash2(self, key):
        norm_key = self._normalize_key(key)
        index = (norm_key // 11) % 11
        return index
