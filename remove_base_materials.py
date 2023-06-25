import pandas as pd


def main():
    try:
        # Getting user inputs
        user_material = input('Material: ')
        user_quantity = int(input('Quantity: '))

        # Get the csv file and create a dataframe
        base_materials = pd.read_csv("base_materials.csv")
        base_df = pd.DataFrame(base_materials)

        # Calling functions
        base_cost = return_cost(base_df, user_material, user_quantity)
        subtract_quantity(base_df, user_material, user_quantity)
        update_cost(base_df, user_material, user_quantity)
        remove_entry(base_df)
        return base_cost

    except ValueError:
        print('Invalid entry')
        main()


def subtract_quantity(base_df, user_material, user_quantity):
    # Get row to update
    filtered_row = (base_df['material'] == user_material)
    # Updating quantity
    base_df.loc[filtered_row, 'quantity'] = base_df.loc[filtered_row, 'quantity'] - user_quantity

    # If trying to remove too many, change value to 'True'
    base_df.loc[base_df['quantity'] <= -1, 'material'] = 'True'
    # Checking for value 'True' and if so warn user and exit
    filtered_row = base_df[base_df['material'] == 'True']
    if len(filtered_row) <= 0:
        pass
    else:
        print('Trying to remove more than available')
        main()

    # Updating csv and notifying user of the remaining quantity
    # base_df.to_csv('base_materials.csv', mode='w', index=False, header=True)
    if user_quantity > 1:
        print(f"\n{user_quantity} {user_material}'s removed.\n")
    elif user_quantity == 1:
        print(f"\n{user_quantity} {user_material} removed.\n")


def update_cost(base_df, user_material, user_quantity):
    # Get row to update
    filtered_row = (base_df['material'] == user_material)

    # Getting the new total item cost
    new_cost = base_df.loc[filtered_row, 'total_cost'] - (user_quantity * base_df.loc[filtered_row, 'average'])

    # Update the cost
    base_df.loc[filtered_row, 'total_cost'] = new_cost

    # Getting the average price per unit
    average = new_cost / base_df.loc[filtered_row, 'quantity']

    # Update the average
    base_df.loc[filtered_row, 'average'] = average

    # Save to file
    base_df.to_csv('base_materials.csv', mode='w', index=False, header=True)
    print('\nFile updated\n')


def remove_entry(base_df):
    # Search quantity column, if 0 remove row
    base_df = base_df[base_df.quantity != 0]
    # Updating the csv
    base_df.to_csv('base_materials.csv', mode='w', index=False, header=True)


def return_cost(base_df, user_material, user_quantity):
    # Filter for correct row
    filtered_row = (base_df['material'] == user_material)
    # Getting the cost per item
    total = base_df.loc[filtered_row, 'average']
    # Indexing to return cell value
    total.index = ['']

    # Single item cost
    cost_per_item = float(total)
    print(f'${cost_per_item:.2f} per item')

    # Total for multiple items
    total_for_all = float(total) * user_quantity
    total_for_all = round(total_for_all, 2)
    print(f'${total_for_all:.2f} for all base materials')

    # Returning the items costs
    base_costs = [cost_per_item, total_for_all]
    return base_costs


if __name__ == "__main__":
    main()
  
