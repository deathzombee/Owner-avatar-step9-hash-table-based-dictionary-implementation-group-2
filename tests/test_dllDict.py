import unittest
from dllDict import DllDict


class TestDllDict(unittest.TestCase):
    def setUp(self):
        """Set up an instance of DllDict before each test."""
        self.dll_dict = DllDict()

    def test_set_and_get_item(self):
        """Test setting and getting an item."""
        self.dll_dict["key1"] = "value1"
        self.assertEqual(self.dll_dict["key1"], "value1")
        # Also test with different casing and whitespace
        self.assertEqual(self.dll_dict["  KEY1  "], "value1")

    def test_update_existing_key(self):
        """Test updating the value of an existing key."""
        self.dll_dict["key1"] = "value1"
        self.dll_dict["KEY1"] = "new_value"
        self.assertEqual(self.dll_dict["key1"], "new_value")

    def test_len(self):
        """Test the length of the dictionary."""
        self.dll_dict["key4"] = "value4"
        self.dll_dict["key5"] = "value5"
        self.assertEqual(len(self.dll_dict), 2)

    def test_setitem_with_whitespace_key(self):
        """Test setting a key with whitespace around it."""
        self.dll_dict["  key_with_space  "] = "value"
        self.assertEqual(self.dll_dict["key_with_space"], "value")
