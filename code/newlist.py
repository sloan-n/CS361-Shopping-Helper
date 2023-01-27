import os

# Main function to create a new list
def create_new(command_input):
    # Remove 'new' from command input
    command_input.pop(0);
    # Join input to get list name
    list_name = '_'.join(command_input);
    # Creates list path to store .txt file
    list_path = ('shopping-lists/' + list_name + '.txt');

    # Checks if list already exists
    if not os.path.exists(list_path):
        # Creates list and returns success message
        open(list_path, 'w').close();
        print(list_name + ' has successfully been created!\n');
    else:
        # Returns error message if list exists
        print('Sorry, ' + list_name + ' already exists.\n');
        