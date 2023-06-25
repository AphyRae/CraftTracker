import pandas as pd


def main():
    # Getting user inputs
    user_material = input("Material: ").strip().lower()
    try:
        user_quantity = int(input("Quantity: "))
        user_cost = float(input("Cost: $"))
        initial_average = user_cost / user_quantity

        # Creating a dictionary for the inputs
        user_base_materials = {
            "material": [user_material],
            "quantity": [user_quantity],
            "total_cost": [user_cost],
            "average": [initial_average]
        }

        # Creating a dataframe of the user inputs
        user_base_df = pd.DataFrame(user_base_materials)

        # Get the csv file and create a dataframe
        base_materials = pd.read_csv("base_materials.csv")
        base_df = pd.DataFrame(base_materials)

        # Checking if material is in csv, appending or updating as needed
        filtered_row = base_df[base_df['material'] == user_material]

        if len(filtered_row) <= 0:
            user_base_df.to_csv('base_materials.csv', mode='a', index=False, header=False)
            print('\nAdded to file\n')

        else:
            update_base_qty(base_df, user_material, user_quantity)
            update_base_cost(base_df, user_material, user_cost)

    except ValueError:
        print('Invalid entry')
        main()


def update_base_qty(base_df, user_material, user_quantity):
    # Get row to update
    filtered_row = (base_df['material'] == user_material)
    # Updating quantity
    base_df.loc[filtered_row, 'quantity'] = user_quantity + base_df.loc[filtered_row, 'quantity']
    # Saving to file
    base_df.to_csv('base_materials.csv', mode='w', index=False, header=True)


def update_base_cost(base_df, user_material, user_cost):
    # Get row to update
    filtered_row = (base_df['material'] == user_material)

    # Getting the new total item cost
    old_cost = base_df.loc[filtered_row, 'total_cost']
    new_cost = [old_cost, user_cost]
    new_cost = sum(new_cost)

    # Update the cost
    base_df.loc[filtered_row, 'total_cost'] = new_cost

    # Getting the average price per unit
    average = new_cost / base_df.loc[filtered_row, 'quantity']

    # Update the average
    base_df.loc[filtered_row, 'average'] = average

    # Save to file
    base_df.to_csv('base_materials.csv', mode='w', index=False, header=True)
    print('\nFile updated\n')


if __name__ == "__main__":
    main()
  
