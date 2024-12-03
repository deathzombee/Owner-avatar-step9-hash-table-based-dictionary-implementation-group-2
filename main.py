import sys
import unittest
from inventories import SatSystemHT
from interface import Interface


# Gabriel Calderon
def main():
    # Check if the user passed '--test' as a command-line argument
    if "--test" in sys.argv:
        # Run all tests in the test suite
        loader = unittest.TestLoader()
        tests = loader.discover(start_dir="tests", pattern="test_sl*.py")
        test_runner = unittest.TextTestRunner(verbosity=2)
        test_runner.run(tests)
    else:
        # Continue with the main program if no '--test' argument is passed
        inventory = SatSystemHT()
        inventory.load_data()
        menu = Interface()
        menu.menu_function(inventory)


if __name__ == "__main__":
    main()
