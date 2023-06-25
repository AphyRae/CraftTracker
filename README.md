    # Craft Material Invoice Cost
    #### Video Demo:  https://youtu.be/8bilT6Nez8M
    #### Description: This is a program to help keep an inventory of crafting supplies to use with heat transfers and Cricut projects, and produce the costs of materials used. Included features:
    - Adding base materials (e.g. mug, shirt, hat)
    - Adding cut materials (e.g. vinyl, heat transfer)
    - Removing base and cut materials
    - Inventory of materials
    - Total project costs

    ## Dependencies
    The following python packcages are required:
    -sys
    -pandas
    -numpy
    -tabulate

    ## Supporting Code
    - 'base_materials.py': adds base materials, updating the inventory in a CSV file.
    - 'cut_materials.py': adds cut materials, updating the inventory in a CSV file.
    - 'remove_base_materials.py': removes materials from the CSV file and returns costs.
    - 'remove_cut_materials.py': removes materials from the CSV file and returns costs.

    ## Using the program
    The user will be presented with a menu of options:
    - To add materials, press 1
    - To remove materials, press 2
    - To see the current project costs, press 3
    - To see inventories, press 4
    - To exit the program, press 0

    ## Adding materials
    To add materials, after selecting 1 from the main menu the user will be asked to:
    - Press 1 to add base materials
    - Press 2 to add cut materials
    - Press 9 to return to the main menu
    - Press 0 to exit the program

    If the user selects option 1, they will be prompted for the following information:
    - Material: ....
    - Quantity: ....
    - Cost: ....

    If the material is not in the CSV file it will be added, otherwise the quantity and cost per unit will be updated.

    If the user selects option 2, they will be prompted for the following information:
    - Material: ....
    - Color or Pattern: ....
    - Size Length (inches): ....
    - Size Width (inches): ....
    - Costs: ....

    If the material is not in the CSV file it will added, otherwise the amount in file and cost per sqaure inch will be updated.

    ## Removing Materials
    To remove materials, after selecting 2 from the main menu the user will be asked to:
    - Press 1 to remove base materials
    - Press 2 to remove cut materials
    - Press 9 to return to the main menu
    - Press 0 to exit the program

    If the user selects option 1, they will be prompted for the following information:
    - Material: ....
    - Quantity: ....

    The program will then update the CSV file appropiately, and will return the total costs for the items removed.

    If the user selects option 2, they will be prompted for the following information:
    - Material: ....
    - Color or Pattern: ....
    - Length: ....
    - Width: ....

    The program will then update the CSV file appropiately, and will return the total costs for the items removed.

    ## Viewing the total project cost
    The user is able to view the combined cost of all items removed during the current running of the program. To view the total project cost, select 3 from the main menu.

    ## Viewing Inventories
    The program will show the corresponding inventory in a table. To access, select 4 from the main menu. The user will then have the option of:
    - Pressing 1, to see the base material inventory
    - Pressing 2, to see the cut material inventory
    - Pressing 9, to return to the main menu
    - Pressing 0, to exit the program

    ## Roadmap
    - [x] Create gui
          - [x] Drop down lists for the user to select for addition and removal of items already in the file. To help reduce misspelling of items creating doubles.
