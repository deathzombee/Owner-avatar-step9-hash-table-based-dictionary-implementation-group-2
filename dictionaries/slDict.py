from .dictabs import DictAbstract
from .pairD import PairD


class SLDict(DictAbstract):
    # Team programming
    def __init__(self):
        # Initialize an empty list to store PairD objects
        self._data = []

    # Gabriel
    def _normalize_key(self, key):
        """Return a normalized version of the key."""
        key = key.strip().lower()
        return key  # Add this line

    def sort():
        pass

    def __len__(self):
        pass

    def __contains__(self, key):
        pass

    def __getitem__(self, key):
        pass

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

    # lisa
    def rl(self, key):
        pass

    # Gabriel
    def rr(self, key):
        pass

    # peter
    def pivot(self):
        pass
