import numpy as np
import pandas as pd


def main():
    try:
        # Get user inputs
        user_material = input('Material: ')
        user_color = input('Color or Pattern: ')
        user_length = float(input('Length: '))
        user_width = float(input('Width: '))
        square_inches = user_length * user_width

        # Creating a dataframe from the csv
        cuts = pd.read_csv('cut_materials.csv')
        cuts_df = pd.DataFrame(cuts)

        # Calling functions
        subtract_length(cuts_df, user_material, user_color, user_length)
        cut_costs = return_cost(cuts_df, user_material, user_color, square_inches)
        update_cost(cuts_df, user_material, user_color, user_length)
        remove_entry(cuts_df)
        return cut_costs

    except ValueError:
        print('Invalid entry')
        main()


def subtract_length(cuts_df, user_material, user_color, user_length):
    # Updating the length of row with matching conditions
    cuts_df['length'] = np.where((cuts_df['material'] == user_material) &
                                 (cuts_df['color_or_pattern'] == user_color), cuts_df['length'] -
                                 user_length, cuts_df['length'])

    # If trying to remove too much material, change value to 'True'
    cuts_df.loc[cuts_df['length'] <= -1] = 'True'
    # Checking for value 'True' and if found warn user and exit
    filtered_row = cuts_df[cuts_df['material'] == 'True']
    if len(filtered_row) <= 0:
        pass
    else:
        print('\nTrying to remove more than available')
        main()

    # Printing confirmation
    if user_length >= 2:
        print(f"\n{user_length} inches of {user_color} {user_material} has been removed.")
    elif user_length == 1:
        print(f"\n{user_length} inch of {user_color} {user_material} has been removed.")


def return_cost(cuts_df, user_material, user_color, square_inches):
    # Getting the cost and saving it to the 'temp' column
    cost = np.where((cuts_df['material'] == user_material) & (cuts_df['color_or_pattern'] == user_color),
                    cuts_df['average'] * square_inches, cuts_df['blank'])

    # Removing all empty rows from 'tem
    cost = cost[pd.notnull(cost)]

    # Returning the user's cost per cut material
    cost = str(cost).strip('[]')
    cost = float(cost)
    cut_costs = round(cost, 2)
    return cut_costs


def update_cost(cuts_df, user_material, user_color, user_length):
    # Updating 'total_cost' to adjust for user removals
    cuts_df['total_cost'] = np.where((cuts_df['material'] == user_material) & (cuts_df['color_or_pattern']
                                                                               == user_color), cuts_df['total_cost'] -
                                     (cuts_df['average'] * (user_length * cuts_df['width'])), cuts_df['total_cost'])
    print('\nFile updated\n')


def remove_entry(cuts_df):
    # Search quantity column, if 0 remove row
    cuts_df = cuts_df[cuts_df.length > 1]
    # Updating the csv
    cuts_df.to_csv('cut_materials.csv', mode='w', index=False, header=True)

    # Clearing values from cut_material_price.csv
    total = pd.read_csv('cut_material_price.csv')
    total_df = pd.DataFrame(total)
    total_df['cost_per'] = 0
    total_df.to_csv('cut_material_price.csv', mode='w', index=False, header=True)


if __name__ == "__main__":
    main()
  
