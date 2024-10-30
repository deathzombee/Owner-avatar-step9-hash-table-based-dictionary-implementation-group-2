from inventoryLLDict import SatSystemDll
from interface import Interface



# Gabriel Calderon
def main():
    inventory = SatSystemDll()
    inventory.load_data()
    menu = Interface()
    menu.menu_function(inventory)


if __name__ == "__main__":
    main()
