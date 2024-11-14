import unittest
from dictionaries import SLDict


class TestSLDict(unittest.TestCase):
    def setUp(self):
        """Set up an instance of SLDict before each test."""
        self.sl_dict = SLDict()

    def test_set_and_get(self):
        """Test setting and getting an item."""
        self.sl_dict["key1"] = "value1"
        self.assertEqual(self.sl_dict["key1"], "value1")
        # Also test with different casing and whitespace
        self.assertEqual(self.sl_dict["  KEY1  "], "value1")

    def test_update_existing_key(self):
        """Test updating the value of an existing key."""
        self.sl_dict["key1"] = "value1"
        self.sl_dict["KEY1"] = "new_value"
        self.assertEqual(self.sl_dict["key1"], "new_value")

    def test_len(self):
        """Test the length of the dictionary."""
        self.sl_dict["key4"] = "value4"
        self.sl_dict["key5"] = "value5"
        self.assertEqual(len(self.sl_dict), 2)

    def test_setitem_with_whitespace_key(self):
        """Test setting a key with whitespace around it."""
        self.sl_dict["  key_with_space  "] = "value"
        self.assertEqual(self.sl_dict["key_with_space"], "value")

    def test_contains(self):
        """Test the __contains__ method to check if a key is present."""
        self.sl_dict["key1"] = "value1"
        self.assertIn("key1", self.sl_dict)
        self.assertNotIn("missing_key", self.sl_dict)

    def test_pop(self):
        """Test removing an item with pop and checking if it's removed."""
        self.sl_dict["key1"] = "value1"
        popped_value = self.sl_dict.pop("key1")
        self.assertEqual(popped_value, "value1")
        self.assertNotIn("key1", self.sl_dict)

        # Test popping a non-existent key; should raise KeyError
        with self.assertRaises(KeyError):
            self.sl_dict.pop("nonexistent")

    def test_sort(self):
        """Test sorting functionality for SLDict by key."""
        # Add unordered key-value pairs
        self.sl_dict["c"] = 3
        self.sl_dict["a"] = 1
        self.sl_dict["b"] = 2
        self.sl_dict.sort()

        # Check if data is sorted by key (lexicographical order of 'a', 'b', 'c')
        sorted_keys = [pair.key for pair in self.sl_dict._data]
        self.assertEqual(sorted_keys, ["a", "b", "c"])

    def test_sort_with_mixed_data(self):
        """Test sorting after shuffling the data, based on key."""
        # Insert unsorted values
        self.sl_dict["d"] = 10
        self.sl_dict["b"] = 2
        self.sl_dict["a"] = 15
        self.sl_dict["c"] = 7
        self.sl_dict.mix()  # Shuffle the list

        # Sort and check if the data is sorted by key
        self.sl_dict.sort()
        sorted_keys = [pair.key for pair in self.sl_dict._data]
        self.assertEqual(
            sorted_keys, sorted(sorted_keys)
        )  # Check if sorted by key

    def test_rl_helper(self):
        """Test the rl helper method directly to ensure recursive sorting by key."""
        # Insert unordered key-value pairs
        self.sl_dict["c"] = 5
        self.sl_dict["a"] = 3
        self.sl_dict["b"] = 4

        # Call rl directly on the internal data for recursive sorting test
        self.sl_dict._data = self.sl_dict.rl(self.sl_dict._data)
        sorted_keys = [pair.key for pair in self.sl_dict._data]
        self.assertEqual(sorted_keys, ["a", "b", "c"])

    def test_normalize_key(self):
        """Test key normalization for consistent key handling."""
        normalized_key = self.sl_dict._normalize_key("  Key1  ")
        self.assertEqual(normalized_key, "key1")

    def test_mixed_sort_and_operations(self):
        """Test sort in conjunction with setitem and pop to ensure stability."""
        # Insert unordered data
        self.sl_dict["key3"] = 5
        self.sl_dict["key1"] = 3
        self.sl_dict["key4"] = 8
        self.sl_dict["key2"] = 1

        # Sort the dictionary and verify the order by key
        self.sl_dict.sort()
        sorted_keys = [pair.key for pair in self.sl_dict._data]
        self.assertEqual(sorted_keys, ["key1", "key2", "key3", "key4"])

        # Remove an item and check if sort remains stable
        self.sl_dict.pop("key3")
        self.sl_dict.sort()  # Re-sort after pop
        sorted_keys = [pair.key for pair in self.sl_dict._data]
        self.assertEqual(sorted_keys, ["key1", "key2", "key4"])


if __name__ == "__main__":
    unittest.main()
