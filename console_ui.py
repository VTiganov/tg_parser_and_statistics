import parser

def console() -> int:
    print("Choose option to execute:")
    print("1. Start parsing")
    print("2. Analyze particular chat")
    print("3. Print overall statistics")
    try:
        chosen_option = int(input("Enter number of option: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        return None

    if chosen_option not in {1, 2, 3}:
        print("Invalid input. Please enter a number between 1 and 3.")
        return None
    
    return chosen_option

def start_parsing():
    parser.main()

def analyze_particular_chat():
    pass

def print_overall_statistics():
    pass

def main():
    
    chosen_option = console()
    
    if chosen_option is None:
        return
    
    if chosen_option == 1:
        start_parsing()
    
    elif chosen_option == 2:
        analyze_particular_chat()
    
    elif chosen_option == 3:
        print_overall_statistics()

