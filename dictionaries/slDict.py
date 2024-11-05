from .dictabs import DictAbstract
from .pairD import PairD


class SLDict(DictAbstract):
    # Team programming
    def __init__(self):
        # Initialize an empty list to store PairD objects
        self._data = []
        self._size = 0

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

    def __getitem__(self, key):
        pass

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
            print(self._data)  # test if works

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
