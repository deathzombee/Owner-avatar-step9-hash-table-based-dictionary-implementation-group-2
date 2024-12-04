import unittest
from dictionaries import HTDict


class TestHTDict(unittest.TestCase):
    def setUp(self):
        self.ht_dict = HTDict()

    def test_set_and_get_item(self):
        self.ht_dict["key1"] = "value1"
        self.assertEqual(self.ht_dict["key1"], "value1")
        self.assertEqual(self.ht_dict["  KEY1  "], "value1")

    def test_update_existing_key(self):
        self.ht_dict["key1"] = "value1"
        self.ht_dict["KEY1"] = "new_value"
        self.assertEqual(self.ht_dict["key1"], "new_value")

    def test_len(self):
        self.ht_dict["key4"] = "value4"
        self.ht_dict["key5"] = "value5"
        self.assertEqual(len(self.ht_dict), 2)

    def test_setitem_with_whitespace_key(self):
        self.ht_dict["  key_with_space  "] = "value"
        self.assertEqual(self.ht_dict["key_with_space"], "value")

    def test_contains_key(self):
        self.ht_dict["key2"] = "value2"
        self.assertTrue("key2" in self.ht_dict)
        self.assertFalse("key3" in self.ht_dict)

    def test_pop_item(self):
        self.ht_dict["key3"] = "value3"
        value = self.ht_dict.pop("key3")
        self.assertEqual(value, "value3")
        self.assertFalse("key3" in self.ht_dict)

    def test_pop_nonexistent_key(self):
        with self.assertRaises(KeyError):
            self.ht_dict.pop("nonexistent_key")

    def test_rehash(self):
        """Test that rehashing works correctly when the capacity is exceeded."""
        original_capacity = self.ht_dict._capacity
        items_to_add = int(original_capacity * 0.8)  # Ensure we exceed the likely rehash threshold

        # Add items until we exceed the original capacity
        for i in range(items_to_add):
            self.ht_dict[f"key{i}"] = f"value{i}"

        # Check that the capacity has increased
        self.assertGreater(self.ht_dict._capacity, original_capacity, 
                        "Capacity should have increased after rehashing")

        # Ensure all items are still accessible after rehashing
        for i in range(items_to_add):
            self.assertEqual(self.ht_dict[f"key{i}"], f"value{i}",
                            f"Item key{i} was not correctly preserved after rehashing")

        # Check that the load factor is now below the rehash threshold
        load_factor = len(self.ht_dict) / self.ht_dict._capacity
        self.assertLess(load_factor, 0.75, 
        f"Load factor ({load_factor}) should be below 0.75 after rehashing")
    def test_values(self):
        """Test retrieving all values from the dictionary."""
        self.ht_dict["key1"] = "value1"
        self.ht_dict["key2"] = "value2"
        values = list(self.ht_dict.values())
        self.assertIn("value1", values)
        self.assertIn("value2", values)
