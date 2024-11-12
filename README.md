[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/H2wPSilZ)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16850168)

### `SLDict`

`SLDict` is a custom dictionary implementation based on a sorted list (quick sort with middle pivot). It organizes data by keys (e.g., satellite names) and provides operations for setting, retrieving, searching, sorting, and deleting items. It is designed to sort items lexicographically by their keys.

### `SatSystemSLDict`

`SatSystemSLDict` is the main inventory system class that uses `SLDict` to store satellite information. It includes methods to load data from a CSV file, search satellites by various attributes, add or delete satellites, and write the inventory back to a CSV file.

## Running the Program

### Running the Main Program

To run the main program and use the inventory interface:

```bash
python main.py
```

This will load satellite data, shuffle and sort the entries, and launch an interactive menu for managing the inventory.

### Running Tests from Main

To run the tests directly from `main.py`, you can use the `--test` flag:

```bash
python main.py --test
```

This will execute all tests in verbose mode, showing each test case and its result.

### Running Tests Separately

If you want to run the test suite independently, use the following command:

```bash
python -m unittest -v tests/test_slDict.py  tests/test_slInv.py
```

## Directory Structure

- `dictionaries/`: Contains `SLDict`, the sorted-list dictionary implementation.
- `inventories/`: Contains `SatSystemSLDict`, the main inventory system class.
- `objects/`: Defines the `Satellite` class with attributes like `name`, `orbit_type`, `date`, etc.
- `tests/`: Contains unit tests for `SLDict` and `SatSystemSLDict`.
- `main.py`: Entry point for running the inventory system or executing tests.

## Notes

- `SLDict` sorts data lexicographically by satellite names (keys).
- The `mix` method in `SLDict` shuffles the entries, which is helpful for testing sorting functionality.
- The `write_back` method in `SatSystemSLDict` saves any modifications to `AllSatellites.csv`.
