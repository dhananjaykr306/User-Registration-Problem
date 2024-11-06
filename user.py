'''
    @Author: Dhananjay Kumar
    @Date: 04-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 04-11-2024
    @Title : Check user valid name
'''

import re

# Method to check if the first name is valid
def is_valid_First_name(first_name):
    try:
        # Check if input is a string
        if not isinstance(first_name, str):
            raise ValueError("Input must be a string.")

        # Define the pattern for a valid first name (starts with uppercase, followed by lowercase letters)
        first_name_pattern = r'^[A-Z][a-z]{2,}$'  
        return bool(re.match(first_name_pattern, first_name))  # Returns True if the name matches the pattern, otherwise False
    
    except Exception as e:
        print(f"Error: {e}")  # Print the exception message if something goes wrong
        return False  # Return False in case of any errors


# Main function
def main():
    try:
        name = input("Enter your first name: ")
        result = is_valid_First_name(name)  # Check if the entered name is valid
        if result:
            print(f"It is a valid first name: {name}")  # Print valid name
        else:
            print(f"It is not a valid first name: {name}")  # Print invalid name
    except Exception as e:
        print(f"Error: {e}")  # Handle any unexpected errors that occur in the main function

if __name__ == "__main__":
    main()
