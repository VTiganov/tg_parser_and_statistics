import parser

def console() -> int:
    """Displays menu options and prompts the user to select an option."""
    while True:
        print("Choose option to execute:")
        print("1. Start parsing")
        print("2. Analyze particular chat")
        print("3. Print overall statistics")
        print("0. Exit")
        
        try:
            chosen_option = int(input("Enter number of option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 3.")
            continue

        if chosen_option in {0, 1, 2, 3}:
            return chosen_option
        else:
            print("Invalid input. Please enter a number between 0 and 3.")

def start_parsing():
    """Starts the parsing process using parser.main()."""
    filename = input("Enter the filename to save chats (e.g., chats.csv): ")
    if not filename.lower().endswith('.csv'):
        filename += '.csv'
    parser.export_chats(filename)

def analyze_particular_chat():
    """Analyzes a specific chat. Function implementation needed."""
    print("Function analyze_particular_chat is not yet implemented.")

def print_overall_statistics():
    """Prints overall statistics. Function implementation needed."""
    print("Function print_overall_statistics is not yet implemented.")

def main():
    while True:
        chosen_option = console()
        
        if chosen_option == 0:
            print("Exiting program.")
            break
        elif chosen_option == 1:
            start_parsing()
        elif chosen_option == 2:
            analyze_particular_chat()
        elif chosen_option == 3:
            print_overall_statistics()
