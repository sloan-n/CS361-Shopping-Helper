import os

# main function to use view function
def view_list(command_input):
    # if request to view by category
    if command_input[1] == '-c':
        view_with_flag(command_input, 'category');
    # if request to view by store
    elif command_input[1] == '-s':
        view_with_flag(command_input, 'store');
    elif command_input[1] == 'all':
        view_all_lists(command_input);
    # else view by shopping list name
    else:
        view_by_name(command_input);

# Return list name when flag is present
def list_name_with_flags(command_input):
    command_input.pop(0);
    command_input.pop(0);
    return '_'.join(command_input);

# Return list name when there is no flag
def list_name_no_flags(command_input):
    command_input.pop(0);
    return '_'.join(command_input);

# Returns the list path
def list_path(list_name):
    return 'shopping-lists/' + list_name + '.txt';

# Opens the list by flag
def view_with_flag(command_input, flag_type):
    list_name = list_name_with_flags(command_input);
    flag_name = input("What " + flag_type + "?\n");
    print("Opening file to view " + list_name + " by " + flag_name + "...\n");
    if valid_filter(flag_type, flag_name):
        open_filtered_list(list_name, flag_name);
    else:
        print(flag_name + " is not an available " + flag_type + ".\n");


# View all shopping lists
def view_all_lists(command_input):
    print("Viewing all shopping lists: \n");
    all = os.listdir('shopping-lists/');
    for list in all:
        print(list.split('.txt')[0]);
    print("\n");

# View a specific list by name
def view_by_name(command_input):
    list_name = list_name_no_flags(command_input);
    print("Opening file to view " + list_name + "...\n");
    open_list(list_name);

# Open list function
def open_list(list_name):
    path = list_path(list_name);
    # Checks if list already exists
    if os.path.exists(path):
        f = open(path, "r");
        print("Viewing " + list_name + "\n");
        print(f.read());
        if os.stat(path).st_size == 0:
            print("Your list is currently empty!\n");
        f.close();
    else:
        print("Sorry, " + list_name + " does not exist.\n");

# Open list based on filtered value
def open_filtered_list(list_name, filter):
    path = list_path(list_name);
    # Checks if list already exists
    if os.path.exists(path):
        f = open(path, "r");
        print("Viewing " + list_name + ": " + filter +"\n");
        count = 0;
        list = f.readlines();
        # Iterate through each line in the list to check if filtered word exists
        for line in list:
            if filter in line:
                print(line);
                count += 1
        # Prints number of items for the filtered search.
        print("There are " + str(count) + " items for " + filter + ".\n");
        f.close();
    else:
        print("Sorry, " + list_name + " does not exist.\n");

# Returns a boolean if the filter string is a category or store
def valid_filter(flag_type, flag_name):
    if flag_type == 'category':
        f = open('txt_files/categories.txt', 'r');
    elif flag_type == 'store':
        f = open('txt_files/stores.txt', 'r');
    content = f.read();
    if flag_name in content:
        return True;
    else:
        return False;



