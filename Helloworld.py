# --- Python Name Input Script ---

def get_user_name():
    """
    Prompts the user to enter their name and returns the cleaned input.
    Continues to prompt until a non-empty name is entered.
    """
    while True:
        # Prompt the user for their name using input()
        # The input() function reads a line from input, converts it to a string, and returns that.
        user_name = input("Please enter your name: ").strip()

        # Check if the entered name is not empty after removing leading/trailing whitespace
        if user_name:
            return user_name
        else:
            print("Name cannot be empty. Please try again.")

def display_greeting(name):
    """
    Prints a personalized greeting to the console.
    """
    print(f"\nHello, {name}!") # Use an f-string for easy string formatting

# --- Main execution block ---
if __name__ == "__main__":
    # Call the function to get the user's name
    name = get_user_name()

    # Call the function to display the greeting
    display_greeting(name)

    print("\nScript finished.")
