# Main function to return help command
def get_commands_list() :    
    f = open('txt_files/help.txt', 'r');
    print(f.read());
    f.close;