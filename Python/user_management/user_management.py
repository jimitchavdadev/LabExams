import hashlib
import os

# File to store user data
USER_DATA_FILE = 'users.txt'

def load_users():
    """Load users from the file into a dictionary."""
    users = {}
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            for line in file:
                username, hashed_password = line.strip().split(',')
                users[username] = hashed_password
    return users

def save_user(username, hashed_password):
    """Save a new user to the file."""
    with open(USER_DATA_FILE, 'a') as file:
        file.write(f"{username},{hashed_password}\n")

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register(username, password):
    """Register a new user."""
    users = load_users()
    if username in users:
        print("Username already exists. Please choose a different username.")
        return False

    hashed_password = hash_password(password)
    save_user(username, hashed_password)
    print("User  registered successfully!")
    return True

def login(username, password):
    """Log in a user."""
    users = load_users()
    if username not in users:
        print("Username not found.")
        return False

    hashed_password = users[username]
    if hashed_password == hash_password(password):
        print("Login successful!")
        return True
    else:
        print("Incorrect password.")
        return False

def main():
    while True:
        print("\n--- User Management System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()