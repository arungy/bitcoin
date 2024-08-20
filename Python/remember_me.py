import sys
import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as fp:
            username = json.load(fp)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for  a new username."""

    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as fp:
        json.dump(username, fp)

    return username

def main():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

if __name__ == '__main__':
    main()
    sys.exit(1)
