import csv
from .inventoryabs import Inventory
from dictionaries import HTDict
from objects import Satellite


class SatSystemHT(Inventory):
    def __init__(self):
        self.satdict = HTDict()

    def __str__(self):
        return "not implemented yet"

    def load_data(self):
        """Load item data from a file and populate the item list."""
        with open("AllSatellites.csv", newline="") as csv_file:
            csv_reader = csv.reader(
                csv_file
            )  # looks neater when calling our line reader
            next(csv_reader)  # skip the first row, as its not satellite data
            for row in csv_reader:
                sat = Satellite()
                sat.name = row[0]
                sat.orbit_type = row[1]
                sat.orbit_height = row[2]
                sat.cycle = row[3]
                sat.date = row[4]
                sat.oos_date = row[5]
                sat.org = row[6]
                self.satdict[sat.name] = sat

    # Gabriel Calderon
    def get_satellites(self):
        """Return the list of satellites."""
        return list(self.satdict.values())

    # Gabriel Calderon
    def search(
        self, attribute, value
    ):  # non interactive search that returns all matches
        """Search for an item by attribute."""
        attributes = [
            "name",
            "orbit_type",
            "orbit_height",
            "cycle",
            "date",
            "oos_date",
            "org",
        ]
        if attribute not in attributes:
            raise ValueError(
                f"Invalid attribute '{attribute}'. Valid attributes are: {', '.join(attributes)}"
            )
        matches = []
        for satellite in self.satdict.values():
            attr_value = getattr(satellite, attribute)
            if str(attr_value).lower() == str(value).lower():
                matches.append(satellite)
        return matches

    # Lisa M.

    def birthday_search(self, date):
        result = []  # Create a list to hold the chosen satellites

        # Get the low and high values of the decade
        low = (date // 10) * 10
        high = low + 10

        # Iterate through all satellites
        for satellite in self.satdict.values():
            try:
                if satellite.date:  # Ensure date is not None or empty
                    launched = int(satellite.date)
                    if low <= launched < high:
                        result.append(satellite)  # Append the Satellite object
            except ValueError:
                # Skip satellites with invalid year
                continue
        return result
    # Lisa M.
    def delete(self, attribute, value):
        """Delete satellites based on a specified attribute and value."""
        attributes = [
            "name",
            "orbit_type",
            "orbit_height",
            "cycle",
            "date",
            "oos_date",
            "org",
        ]
        if attribute not in attributes:
            print(
                f"Invalid attribute '{attribute}'. Valid attributes are: {', '.join(attributes)}"
            )
            return

        matches = self.search(attribute, value)
        if not matches:
            print(f"No satellites found with {attribute} = {value}")
            return

            # Display matching satellites with index numbers
        print(f"Results for {attribute} = {value}:")
        for i, satellite in enumerate(matches, start=1):
            print(f"{i}. {satellite}")

        prompt1 = (
            input("Do you want to delete ALL of these records? (yes/no): ")
            .strip()
            .lower()
        )

        if prompt1 in ("yes", "y"):

            # execute if user input is affirmative
            csv_size = len(
                self.satdict
            )  # set length of entire satellite list to variable
            # self.satdict[satellite.name] = [sat for sat in self.satdict.name] if sat not in matches]
            for satellite in matches:
                key = satellite.name
                self.satdict.pop(key)
            deleted_count = csv_size - len(self.satdict)
            print(
                f"you have successfully deleted {deleted_count} records."
            )  # print("The following indices were deleted from csv_list: " + indices_deleting) #use to check what indices were deleted

        elif prompt1 in ("no", "n"):  # execute if user input is negative
            prompt2 = input(
                "Do you want to delete a specific Satellite entry?"
            )
            if prompt2 == ("yes") or prompt1 == ("y"):
                # Let the user select which satellite to delete
                while True:
                    try:
                        selection = int(
                            input(
                                "Enter the number of the satellite you want to delete (or 0 to cancel): "
                            )
                        )
                        if selection == 0:
                            print("Deletion canceled.")
                            break
                        elif 1 <= selection <= len(matches):
                            satellite_to_delete = matches[selection - 1]
                            keytoremove = satellite_to_delete.name
                            self.satdict.pop(keytoremove)
                            print("Satellite successfully deleted.")
                            break
                        else:
                            print("Invalid selection. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
            else:
                print("No satellites were deleted.")
        elif prompt1 in ("q", "quit"):  # execute if user wants to quit
            print("You have exited delete mode.")
        else:
            print("Invalid input. exiting for data safety.")

    # Lisa M.
    def write_back(self):
        """write the current list of satellites back to the CSV file"""
        with open(
            "AllSatellites.csv", "w", newline=""
        ) as file:  # opens Satellite csv in write mode and refers to it as 'file', will close file automatically once done
            writer = csv.writer(
                file
            )  # create writer object to write to the file
            writer.writerow(
                [
                    "name",
                    "orbit_type",
                    "orbit_height",
                    "cycle",
                    "date",
                    "oos_date",
                    "org",
                ]
            )
            # Write each satellite's data
            for satellite in self.satdict.values():
                writer.writerow(
                    [
                        satellite.name,
                        satellite.orbit_type,
                        satellite.orbit_height,
                        satellite.cycle,
                        satellite.date,
                        satellite.oos_date,
                        satellite.org,
                    ]
                )

    # Peter V.
    def add_satellite(self):
        satelitte_not_add = True  # bool for while loop

        # while loop to add satellite information if fails user have to re-enter satellite information
        while satelitte_not_add:
            try:
                print("Enter the satellite name")
                name = input()

                print("Enter the sattelite orbit type")
                orbit_type = input()

                print("Enter the satellite orbit height")
                orbit_height = input()

                print("Enter the satellite cycle")
                cycle = input()

                print("Enter the satellite launched date")
                date = input()

                print("Enter the satellite out of service date ")
                oos_date = input()

                print("Enter the satellite organization")
                org = input()
                new_satellite = Satellite(
                    name=name,
                    orbit_type=orbit_type,
                    orbit_height=orbit_height,
                    cycle=cycle,
                    date=date,
                    oos_date=oos_date,
                    org=org,
                )
                # once all input is filled in correctly exit while loop
                satelitte_not_add = False
            except ValueError as ve:
                print(f"Validation error:{ve}. Please try again.")
            except Exception as e:
                print(f"An exception occured: {e}")
            except:
                print("error")
        else:
            # if everything was valid we can add to the list
            self.satdict[new_satellite.name] = (
                new_satellite  # *figure out how insert works
            )
            print("Satellite successfully added!")

    # Peter V. search function rework. Help from Gabriel
    def search_function(self, search):  # Peter V. search function

        display_result = []  # empty list to display reseult
        x = 0  # x value for incrementing
        for satellite in self.satdict.values():
            # exits when size is 20 for the 20 results
            if x >= 20:
                break
            # if name matches add to display_results and wont add if duplicate
            if search.lower() == satellite.name.lower():
                display_result.append(satellite)
                x += 1
            # if condition to search for orbit type
            elif search.lower() == satellite.orbit_type.lower():
                display_result.append(satellite)
                x += 1
            # if condition to search for orbit height
            elif self._attribute_matches(search, satellite.orbit_height):
                display_result.append(satellite)
                x += 1
            # if condition to search cycle
            elif self._attribute_matches(search, satellite.cycle):
                display_result.append(satellite)
                x += 1
            # if condition to search launched date
            elif self._attribute_matches(search, satellite.date):
                display_result.append(satellite)
                x += 1
            # if condition to search out of service date
            elif self._attribute_matches(search, satellite.oos_date):
                display_result.append(satellite)
                x += 1
            # if condition to search organization
            elif search.lower() == satellite.org.lower():
                display_result.append(satellite)
                x += 1
        if display_result:
            for result in display_result:
                print(result)
        else:
            print("No matching results found")

    # Peter V. method to help get int value attributes help from Gabriel

    def _attribute_matches(self, search, attribute_value):
        """Helper method to compare search term with satellite attribute."""
        if search.isdigit():
            try:
                return int(search) == int(attribute_value)
            except ValueError:
                return False
        else:
            return search.lower() == str(attribute_value).lower()


# Gabriel Calderon
# just a method to make
# a new reversed dictionary
# because we used a doubly linked list
def reversed_dict(self):
    """Return a new DllDict with the elements in reversed order."""
    new_dict = DllDict()
    # Use reverse_iter to traverse the original dictionary in reverse
    for node in self.reverse_iter():
        new_dict[node.key] = node  # Insert into the new dictionary
    return new_dict
