import unittest
from unittest.mock import patch, MagicMock
from inventories import SatSystemDll
from objects import Satellite
from dictionaries import DllDict
import io


class TestInventoryLLDict(unittest.TestCase):
    def setUp(self):
        # Initialize the inventory system
        self.inventory = SatSystemDll()
        # Manually populate the inventory with test data
        self.inventory.satdict = DllDict()
        self.sat1 = Satellite(
            name="Hubble",
            orbit_type="LEO",
            orbit_height="569",
            cycle="95.42",
            date="1990",
            oos_date="",
            org="NASA",
        )
        self.sat2 = Satellite(
            name="James Webb",
            orbit_type="L2",
            orbit_height="",
            cycle="",
            date="2021",
            oos_date="",
            org="NASA",
        )
        self.sat3 = Satellite(
            name="GPS IIF-3",
            orbit_type="MEO",
            orbit_height="20180",
            cycle="",
            date="2012",
            oos_date="",
            org="USAF",
        )
        # Add satellites to the inventory
        self.inventory.satdict[self.sat1.name] = self.sat1
        self.inventory.satdict[self.sat2.name] = self.sat2
        self.inventory.satdict[self.sat3.name] = self.sat3

    def test_get_satellites(self):
        satellites = self.inventory.get_satellites()
        self.assertEqual(len(satellites), 3)
        self.assertIn(self.sat1, satellites)
        self.assertIn(self.sat2, satellites)
        self.assertIn(self.sat3, satellites)

    def test_search_by_name(self):
        results = self.inventory.search("name", "Hubble")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], self.sat1)

    def test_search_by_orbit_type(self):
        results = self.inventory.search("orbit_type", "LEO")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], self.sat1)

    def test_search_no_results(self):
        results = self.inventory.search("name", "Nonexistent Satellite")
        self.assertEqual(len(results), 0)

    def test_birthday_search(self):
        results = self.inventory.birthday_search(1990)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], self.sat1)

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["yes"])  # Confirm deletion
    def test_delete_satellite(self, mock_input, mock_print):
        # Before deletion
        self.assertIn("hubble", self.inventory.satdict)
        # Delete 'Hubble' satellite
        self.inventory.delete("name", "Hubble")
        # After deletion
        self.assertNotIn("hubble", self.inventory.satdict)
        # Check that confirmation message was printed
        mock_print.assert_any_call("you have successfully deleted 1 records.")

    @patch("builtins.print")
    @patch(
        "builtins.input",
        side_effect=["TestSat", "GEO", "35786", "", "2023", "", "TestOrg"],
    )
    def test_add_satellite(self, mock_input, mock_print):
        self.inventory.add_satellite()
        # test if mock_input is called for eat attribute
        self.assertEqual(mock_input.call_count, 7)

        self.assertIn("testsat", self.inventory.satdict)
        new_sat = self.inventory.satdict["TestSat"]
        self.assertEqual(new_sat.name, "TestSat")
        self.assertEqual(new_sat.orbit_type, "GEO")
        self.assertEqual(new_sat.orbit_height, 35786)
        self.assertIsNone(new_sat.cycle)
        self.assertEqual(new_sat.date, 2023)
        self.assertIsNone(new_sat.oos_date)
        self.assertEqual(new_sat.org, "TestOrg")
        # Check that confirmation message was printed
        mock_print.assert_any_call("Satellite successfully added!")

    @patch("builtins.print")
    def test_search_function(self, mock_print):
        # Test the search_function method
        self.inventory.search_function("Hubble")
        # Check if the correct satellite was printed
        mock_print.assert_any_call(self.sat1)

    def test_search_invalid_attribute(self):
        with self.assertRaises(ValueError):
            self.inventory.search("invalid_attribute", "value")

    @patch("csv.writer")
    @patch("builtins.open")
    def test_write_back(self, mock_open, mock_csv_writer):
        # Mock the file and CSV writer
        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file
        mock_writer = MagicMock()
        mock_csv_writer.return_value = mock_writer

        # Call the method being tested
        self.inventory.write_back()

        # Ensure the file was opened correctly
        mock_open.assert_called_once_with("AllSatellites.csv", "w", newline="")

        # Ensure that writerow was called for headers and satellites
        expected_call_count = len(self.inventory.satdict) + 1  # +1 for header
        self.assertEqual(mock_writer.writerow.call_count, expected_call_count)

        # Verify that the header was written correctly
        header = [
            "name",
            "orbit_type",
            "orbit_height",
            "cycle",
            "date",
            "oos_date",
            "org",
        ]
        mock_writer.writerow.assert_any_call(header)

    @patch("builtins.open")
    def test_load_data(self, mock_open):
        # Mock the CSV reader

        mock_csv_data = io.StringIO(
            """name,orbit_type,orbit_height,cycle,date,oos_date,org
TestSat,GEO,35786,,2023,,TestOrg
"""
        )
        mock_open.return_value.__enter__.return_value = mock_csv_data
        self.inventory.load_data()
        # Check if the satellite was added
        self.assertIn("testsat", self.inventory.satdict)
        self.assertEqual(self.inventory.satdict["testsat"].org, "TestOrg")

    @patch("builtins.print")
    def test_delete_nonexistent_satellite(self, mock_print):
        with patch(
            "builtins.input",
            side_effect=["yes"],
        ):
            # Attempt to delete a satellite that doesn't exist
            self.inventory.delete("name", "Nonexistent Satellite")
            # Check that the correct message was printed
            mock_print.assert_any_call(
                "No satellites found with name = Nonexistent Satellite"
            )

    def test_write_back_no_satellites(self):
        # Clear the inventory by assigning a new empty DllDict
        self.inventory.satdict = DllDict()
        with patch("csv.writer") as mock_csv_writer, patch(
            "builtins.open", new_callable=MagicMock
        ):
            self.inventory.write_back()
            # Ensure that writerow was called only once for the header
            mock_writer = mock_csv_writer.return_value
            self.assertEqual(mock_writer.writerow.call_count, 1)
            # Check that the header was written
            header = [
                "name",
                "orbit_type",
                "orbit_height",
                "cycle",
                "date",
                "oos_date",
                "org",
            ]
            mock_writer.writerow.assert_any_call(header)

    def test_reverse_dict(self):
        """Test if the dictionary is reversed correctly."""
        # Create a list of the original order
        original_order = list(self.inventory.satdict.values())

        # Create a reversed list using reverse_iter()
        reversed_order = list(self.inventory.satdict.reverse_iter())

        # Check if the reversed list matches the original list in reverse order
        self.assertEqual(reversed_order, original_order[::-1])


if __name__ == "__main__":
    unittest.main()
