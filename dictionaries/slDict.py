from .dictabs import DictAbstract
from .pairD import PairD


class SLDict(DictAbstract):
    # Team programming
    def __init__(self):
        # Initialize an empty list to store PairD objects
        self._data = []

    # Define print format so we can call print(Node)
    def __str__(self):
        return f"{self.key}: {self.value}"

    def __len__(self):
        # Return the number of items stored in the dictionary
        return len(self._data)

    def __contains__(self, key):
        # Return true if key is in the dictionary, False otherwise
        key == self._normalize_key(key)
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
        for index, pair in enumerate(self._data):
            if pair.key == norm_key:
                return index
        return None

    # Lisa
    def __setitem__(self, key, value):
        key = self._normalize_key(key)
        current = PairD

        # check if key matches existing key. If yes, update value.
        """if current.key == key:
                current.value = value
                return
            else:
                self._data.append(PairD(key,value))
"""

    # Lisa
    def pop(self, key):
        key = self._normalize_key(key)

        # if key does not exist __getitem will return error,
        # otherwise it returns value associated with key
        value = self.__getitem__(key)

        # if key exists, use remove method to get rid of
        # that node and decrement length
        self._remove(key)
        self._size -= 1
        return value

    # Gabriel
    def _remove(self, key):
        pass

    # Gabriel
    def _normalize_key(self, key):
        """Return a normalized version of the key."""
        key = key.strip().lower()
        return key  # Add this line

    # Peter
    def values(self):
        pass

    # Team
    def sort():
        pass

    # lisa
    def rl(self, key):
        pass

    # Gabriel
    def rr(self, key):
        pass

    # peter
    def pivot(self):
        pass
