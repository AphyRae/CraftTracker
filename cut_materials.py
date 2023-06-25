import numpy as np
import pandas as pd


def main():
    # Getting user inputs
    user_material = input("Material: ").strip().lower()
    user_color = input("Color or Pattern: ").strip().lower()
    try:
        user_length = float(input('Size Length (inches): '))
        user_width = float(input('Size Width (inches): '))
        user_cost = float(input('Cost: $'))

        # Getting the cost per square inch
        initial_average = round(user_cost / (user_length * user_width), 3)

        # Creating dictionary of inputs
        user_materials = {
            "material": [user_material],
            "color_or_pattern": [user_color],
            "length": [user_length],
            "width": [user_width],
            "total_cost": [user_cost],
            "average": [initial_average]
        }

        # Creating a dataframe of the user inputs
        user_cut_df = pd.DataFrame(user_materials)

        # Getting the csv file and creating a dataframe
        cut_materials = pd.read_csv('cut_materials.csv')
        cut_df = pd.DataFrame(cut_materials)

        # Checking if material is in csv, appending or updating as needed
        filtered_row = (cut_df[(cut_df['material'] == user_material) &
                               (cut_df['color_or_pattern'] == user_color)])

        if len(filtered_row) <= 0:
            user_cut_df.to_csv('cut_materials.csv', mode='a', index=False, header=False)
            print('\nAdded to file\n')

        else:
            add_cut_size(cut_df, user_material, user_color, user_length)
            add_cut_cost(cut_df, user_material, user_color, user_cost)

    except ValueError:
        print('Invalid entry')
        main()


def add_cut_size(cut_df, user_material, user_color, user_length):
    # Updating the length of row with matching conditions
    cut_df['length'] = np.where((cut_df['material'] == user_material) &
                                (cut_df['color_or_pattern'] == user_color),
                                cut_df['length'] + user_length, cut_df['length'])

    # Updating the csv
    cut_df.to_csv('cut_materials.csv', mode='w', index=False, header=True)


def add_cut_cost(cut_df, user_material, user_color, user_cost):
    # Updating total_cost
    cut_df['total_cost'] = np.where((cut_df['material'] == user_material) &
                                    (cut_df['color_or_pattern'] == user_color),
                                    (cut_df['total_cost'] + user_cost), cut_df['total_cost'])

    # Update average
    cut_df['average'] = np.where((cut_df['material'] == user_material) &
                                 (cut_df['color_or_pattern'] == user_color),
                                 (cut_df['total_cost'] / (cut_df['length'] * cut_df['width'])), cut_df['average'])

    # Updating the csv
    cut_df.to_csv('cut_materials.csv', mode='w', index=False, header=True)
    print('\nFile updated\n')


if __name__ == "__main__":
    main()
  
