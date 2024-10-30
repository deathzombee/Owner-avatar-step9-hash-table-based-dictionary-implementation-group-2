from fuzzy import FuzzySearch


class Interface:
    @staticmethod
    def print_header():
        print("***********************************************************")
        print("*   Welcome to the inventory system   *")
        print("***********************************************************")

    @staticmethod
    def print_menu():
        # disregard
        print("[0] - exit program")
        # Lisa
        print("[1] - Search Birthday Year")
        # Peter
        print("[2] - Add Record")
        # Lisa
        print("[3] - Delete Record")
        # Peter
        print("[4] - Search")
        # Gabriel
        print("[5] - Fuzzy Search")
        # Lisa
        print("[6] - Save")

    @staticmethod
    def menu_function(inventory):
        option = -1
        Interface.print_header()
        while option != 0:
            Interface.print_menu()
            option = int(input("Option: "))

            # Lisa birthday search option. Places user input into delete,
            if option == 1:

                date = input("Enter year: ")
                results = inventory.birthday_search(int(date))
                for sat in results:
                    print(f"{sat.name} was launched in {sat.date}")

            # peter vang
            elif option == 2:
                inventory.add_satellite()

            # Lisa delete option. Requires value to be an exact match and type to a value in the csv file to work.
            elif option == 3:

                list = ["name", "orbit_type", "orbit_height", "cycle", "date", "oos_date", "org"]
                attribute = int(input("Which attribute are you searching for? \n[0] Name \n[1]\
 Orbit Type \n[2] Orbit Height \n[3] Cycle, \n[4] Date, \n[5] Out of Service Date, \n[6] Organization: \n"))
                if attribute <= len(list)-1:
                    attribute = list[attribute]
                    print(attribute)
                value = input(f"Enter your {attribute} search: ")
                if attribute in ["orbit_height", "date", "oos_date"]:
                    value = int(value)
                elif attribute in ["cycle"]:
                    value = float(value)
                inventory.delete(attribute, value)

            # Peter Search option
            elif option == 4:
                search_value = input(
                    f"Search for satellite by entering satellite's name, or orbit type, or orbit height, \nor orbit cycle, or launched date, or out of service date, or organization name:"
                )
                inventory.search_function(search_value)
            # Gabriel Calderon
            elif option == 5:
                # fuzzy search
                # option to seach a specific attribute or all attributes
                ask_opt = input("Search all attributes? (y/n): ")
                match ask_opt:
                    case "y":
                        search_value = input("fuzzy search: ")
                        fuzzy = FuzzySearch(inventory.get_satellites())
                        result = fuzzy.search_all_attributes(search_value)
                        for sat, ratio in result:
                            # its currently printing the object memory location but we want the object attributes
                            print(sat)
                    case "n":
                        attributes = [
                            "name",
                            "orbit_type",
                            "orbit_height",
                            "cycle",
                            "date",
                            "oos_date",
                            "org",
                        ]
                        # display the attribute options
                        for i, atr in enumerate(attributes):
                            print(f"[{i}] {atr}")
                        attribute_index = int(input("Choose an attribute num: "))
                        selected_atr = attributes[attribute_index]
                        search_value = input(f"enter your search for {selected_atr}: ")
                        fuzzy = FuzzySearch(inventory.get_satellites())
                        result = fuzzy.search_by_attribute(search_value, selected_atr)
                        for sat, ratio in result:
                            print(sat)

            # Lisa save option
            elif option == 6:
                inventory.write_back()

            elif option != 0:
                print("Invalid option")
