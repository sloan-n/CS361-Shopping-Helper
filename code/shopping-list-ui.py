import help
import newlist
import view

# Main function to run program
def main() :
    # Welcome message
    print("Welcome to your Shopping Helper!\n");

    # Run program until user exits
    while True:
        # Get user input
        start = input("Enter a command or 'help' to view available commands: ");
        if not command(start):
            break;

# Function to execute command from user input
def command(input) :
    command_input = input.split();
    # Command on user input
    if input == 'help':
        help.get_commands_list();
    elif command_input[0] == 'new':
        newlist.create_new(command_input);
    elif command_input[0] == 'view':
        view.view_list(command_input);
    elif input == 'exit':
        print("Thanks for using your Shopping Helper! See you next time!\n");
        return False;
    else:
        print("That's an invalid command, please try again.\n");
    return True;


if __name__ == "__main__":
    main();