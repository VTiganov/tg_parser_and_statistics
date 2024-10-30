import os
import pathlib

def check_if_env_exists() -> bool:
    """Checks if the .env file exists in the current directory."""
    return os.path.exists(".env")

def configure_env():
    """Creates a .env file with API_ID and API_HASH variables."""
    api_id = input("Enter your API_ID: ")
    api_hash = input("Enter your API_HASH: ")
    
    with open(".env", "w") as env_file:
        env_file.write(f"API_ID={api_id}\n")
        env_file.write(f"API_HASH={api_hash}\n")
    
    print(".env file created successfully with API_ID and API_HASH.")

def cat_env():
    """Displays the contents of the .env file."""
    if check_if_env_exists():
        with open(".env", "r") as env_file:
            contents = env_file.read()
            print(".env file contents:\n")
            print(contents)
    else:
        print("The .env file does not exist.")


def main():
    while True:
        print("\nChoose an option to execute:")
        print("1. Configure .env file")
        print("2. Display .env file contents")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            configure_env()
        elif choice == "2":
            cat_env()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")