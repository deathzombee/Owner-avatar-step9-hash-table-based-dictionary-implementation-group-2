from .dictabs import DictAbstract
import random


class HTDict(DictAbstract):
    # Team programming

    def __init__(self, capacity=1000):
        """
        Initialize two tables for cuckoo hashing with a total given capacity.
        Each table gets half the capacity.
        """
        self._capacity = capacity  # Total capacity
        self._size = 0
        self._table1 = [None] * (
            self._capacity // 2
        )  # Half capacity for table 1
        self._table2 = [None] * (
            self._capacity // 2
        )  # Half capacity for table 2
        self._rehash_seed = random.randint(
            0, 100000
        )  # Seed for hash randomization during rehash

    # Define print format so we can call print(Node)
    # Team programming
    def __str__(self):
        """
        Define print format for the dictionary.
        Combines non-empty key-value pairs from both tables.
        """
        items = [
            f"{key}: {value}"
            for table in (self._table1, self._table2)
            for pair in table
            if pair is not None
            for key, value in [pair]
        ]
        return "{" + ", ".join(items) + "}"

    # Return the number of items stored in the dictionary
    # Team programming
    def __len__(self):
        """
        Return the number of items stored in the dictionary.
        """
        return self._size

    # Return true if key is in the dictionary, False otherwise
    # Lisa
    def __contains__(self, key):
        """
        Return True if the key exists in the dictionary, False otherwise.
        """
        norm_key = self._normalize_key(key)  # Normalize the key
        try:
            self._find(norm_key)
            return True
        except KeyError:
            return False

    # Retrieve value associated with a key
    # Peter
    def __getitem__(self, key):
        """
        Retrieve the value associated with the given key.
        Raises KeyError if the key is not found.
        """
        norm_key = self._normalize_key(key)  # Normalize the key
        return self._find(norm_key)

    # Find value associated with a key
    # Lisa
    def _find(self, key):
        """
        Find the value associated with the given key.
        Returns the value if found, raises KeyError otherwise.
        """
        index1, index2 = self.hash1(key), self.hash2(key)

        if self._table1[index1] and self._table1[index1][0] == key:
            return self._table1[index1][1]

        if self._table2[index2] and self._table2[index2][0] == key:
            return self._table2[index2][1]

        raise KeyError(f"Key '{key}' not found")

    # Add or update key-value pair
    # Lisa
    def __setitem__(self, key, value):
        """
        Add or update a key-value pair in the dictionary.
        Handles collisions using cuckoo hashing with retries.
        """
        pair = (self._normalize_key(key), value)
        max_retries = 10

        for _ in range(max_retries):
            index1, index2 = self.hash1(pair[0]), self.hash2(pair[0])

            # Insert into table 1
            if not self._table1[index1] or self._table1[index1][0] == pair[0]:
                if not self._table1[index1]:
                    self._size += 1
                self._table1[index1] = pair
                return

            # Insert into table 2
            if not self._table2[index2] or self._table2[index2][0] == pair[0]:
                if not self._table2[index2]:
                    self._size += 1
                self._table2[index2] = pair
                return

            # Eviction logic
            pair, self._table1[index1] = self._table1[index1], pair

        # Trigger rehash if retries fail
        self._rehash()
        self.__setitem__(pair[0], pair[1])

    # Remove and return value associated with a key
    # Lisa
    def pop(self, key):
        """
        Remove and return the value associated with the given key.
        Raises KeyError if the key is not found.
        """
        norm_key = self._normalize_key(key)  # Normalize the key
        index1, index2 = self.hash1(norm_key), self.hash2(norm_key)

        if self._table1[index1] and self._table1[index1][0] == norm_key:
            value = self._table1[index1][1]
            self._table1[index1] = None
            self._size -= 1
            return value

        if self._table2[index2] and self._table2[index2][0] == norm_key:
            value = self._table2[index2][1]
            self._table2[index2] = None
            self._size -= 1
            return value

        raise KeyError(f"Key '{key}' not found")

    # Resize and rehash the tables
    # Gabriel
    def _rehash(self):
        """
        Resize and rehash the tables to avoid infinite loops due to collisions.
        """
        old_table1, old_table2 = self._table1, self._table2
        failed_keys = set()

        self._capacity *= 2
        self._table1 = [None] * (self._capacity // 2)
        self._table2 = [None] * (self._capacity // 2)
        self._size = 0

        # Rehash all existing keys
        for table in (old_table1, old_table2):
            for pair in table:
                if pair:
                    try:
                        self.__setitem__(pair[0], pair[1])
                    except RuntimeError:
                        print(
                            f"[WARNING] Persistent collision for key '{pair[0]}' during rehash."
                        )
                        failed_keys.add(pair)

    # Normalize a key
    # Gabriel
    def _normalize_key(self, key):
        """
        Normalize the key by stripping whitespace and converting to lowercase.
        """
        return key.strip().lower()

    # Return an iterable of all key-value pairs
    # Peter
    def items(self):
        """
        Return an iterable of all key-value pairs in the dictionary.
        """
        return (
            pair
            for table in (self._table1, self._table2)
            for pair in table
            if pair
        )

    # Return all values in the dictionary
    # Peter
    def values(self):
        """
        Directly iterate over the hash tables and yield all stored values.
        Skip None entries.
        """
        for pair in self.items():
            yield pair[1]

    # First hash function
    # Gabriel
    def hash1(self, key):
        """
        First hash function: FNV-1a inspired hash.
        """
        norm_key = self._normalize_key(key)  # Normalize the key
        prime = 1099511628211
        basis = 14695981039346656037
        h = basis
        for c in norm_key:
            h ^= ord(c)
            h *= prime
        return h % len(self._table1)

    # Second hash function
    # Gabriel
    def hash2(self, key):
        """
        Second hash function: MurmurHash-style mixing.
        """
        norm_key = self._normalize_key(key)  # Normalize the key
        h = 0
        for i, c in enumerate(norm_key):
            h ^= (ord(c) + i) * 0x5BD1E995
            h &= 0xFFFFFFFF  # Ensure 32-bit value
            h ^= h >> 24
        return h % len(self._table2)
