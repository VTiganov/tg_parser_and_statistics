import parser
import configure_env

def console() -> int:
    """Displays menu options and prompts the user to select an option."""
    while True:
        print("\nChoose an option to execute:")
        print("1. Start parsing")
        print("2. Analyze particular chat")
        print("3. Print overall statistics")
        print("4. See or rewrite .env file")
        print("0. Exit\n")

        try:
            chosen_option = int(input("Enter the number of your choice: "))
        except ValueError:
            print("\nInvalid input. Please enter a number between 0 and 4.\n")
            continue

        if chosen_option in {0, 1, 2, 3, 4}:
            return chosen_option
        else:
            print("\nInvalid input. Please enter a number between 0 and 4.\n")


def analyze_particular_chat():
    """Analyzes a specific chat. Function implementation needed."""
    print("\nAnalyzing specific chat feature is not yet implemented.\n")

def print_overall_statistics():
    """Prints overall statistics. Function implementation needed."""
    print("\nPrinting overall statistics feature is not yet implemented.\n")

def main():
    while True:
        if configure_env.check_if_env_exists():
            chosen_option = console()
            if chosen_option == 0:
                print("\nExiting program.\n")
                break
            elif chosen_option == 1:
                parser.main()
            elif chosen_option == 2:
                analyze_particular_chat()
            elif chosen_option == 3:
                print_overall_statistics()
            elif chosen_option == 4:
                configure_env.configure_env()
                print("\n.env file configured.\n")
        else:
            print("\nYou have to configure your .env file first!\n")
            configure_env.configure_env()


