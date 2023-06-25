import sys

import pandas as pd
from tabulate import tabulate

import base_materials
import cut_materials
import remove_base_materials
import remove_cut_materials

# Creating a list for the cost totals
total = []


def main():
    choice = int(input(
        'To add materials, press 1.\nTo remove materials, press 2.\nTo see the total project cost, press 3.\nTo see '
        'inventories press 4.\nTo exit, press 0.\n\nWhat would you like to do? \n'))

    if choice == 1:
        add_materials()

    elif choice == 2:
        remove_materials()

    elif choice == 3:
        project_total = sum(total)
        print(f'\n\nThe project total is ${project_total:.2f}\n\n')

        # Returning user to main menu
        main()

    elif choice == 4:
        see_inventory()

    elif choice == 0:
        sys.exit('Exiting program')

    else:
        print('Invalid input, please try again')
        main()


def add_materials(add_choice=None):  # add_choice=None for pytest
    if add_choice is None:
        add_choice = int(
            input('To add base materials, press 1.\nTo add cut materials, press 2.\nTo go back to the main '
                  'menu, press 9.\nTo exit, press 0.\n\nWhat would you like to do? \n'))

    if add_choice == 1:
        base_materials.main()
        add_materials()

    elif add_choice == 2:
        cut_materials.main()
        add_materials()

    elif add_choice == 9:
        main()

    elif add_choice == 0:
        sys.exit('Exiting program')

    else:
        print('Invalid input, please try again')
        add_materials()


def remove_materials(remove_choice=None):
    if remove_choice is None:
        remove_choice = int(
            input('\nTo remove base materials, press 1.\nTo remove cut materials, press 2.\nTo go back to '
                  'the main menu, press 9.\nTo exit, press 0.\n\nWhat would you like to do? \n'))

    if remove_choice == 1:
        base_costs = remove_base_materials.main()
        base_total = base_costs[1]

        # Appending the base_total to total
        total.append(base_total)

        # Returning user to menu
        remove_materials()

    elif remove_choice == 2:
        cut_costs = remove_cut_materials.main()

        # Appending the cut_costs to total
        total.append(cut_costs)

        # Returning user to menu
        remove_materials()

    elif remove_choice == 9:
        main()

    elif remove_choice == 0:
        sys.exit('Exiting the program')

    else:
        print('Invalid input, please try again')
        remove_materials()


def see_inventory(from_test=False, inventory_choice=None):
    if not from_test:
        inventory_choice = int(input('To see the base materials inventory press 1.\nTo see the cut materials inventory '
                                     'press 2.\nTo go back to the main menu press 9.\nTo exit, press 0.\n\nWhat would '
                                     'you like to do? \n'))

    if inventory_choice == 1:
        # Get the csv files and create dataframes
        base = pd.read_csv("base_materials.csv")
        base_df = pd.DataFrame(base)
        print(tabulate(base_df.round(2), showindex=False, headers="keys", tablefmt="fancy_grid"), '\n')

        see_inventory()

    elif inventory_choice == 2:
        # Getting the csv and creating a new dataframe to exclude 'temp' and 'blank' columns
        cut = pd.read_csv("cut_materials.csv")
        cut_df = pd.DataFrame(cut)
        df = pd.DataFrame(cut_df)
        df.drop(columns=['temp', 'blank'], axis=1, inplace=True)
        print(tabulate(df.round(2), showindex=False, headers="keys", tablefmt="fancy_grid"), '\n')

        see_inventory()

    elif inventory_choice == 9:
        main()

    elif inventory_choice == 0:
        sys.exit('Exiting program')

    else:
        print('Invalid input, please try again')
        see_inventory()


if __name__ == "__main__":
    main()
  
