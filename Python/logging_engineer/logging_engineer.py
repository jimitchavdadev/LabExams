import logging

# Configure logging to write to a file
logging.basicConfig(filename='user_manager.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class UserManager:
    def __init__(self):
        self.users = {}
        
    def register_user(self, username, password):
        logging.info(f"Trying to register: {username}")
        if username in self.users:
            logging.error("Username already exists")
            return "Username already exists"
        if not username or not password:
            logging.error("Registration failed, invalid username or password")
            return "Invalid input"

        self.users[username] = password
        logging.info(f"User  '{username}' registered successfully")
        return "Registration successful"
    
    def login_user(self, username, password):
        logging.info(f"Attempting to login user: {username}")
        if username not in self.users:
            logging.error("Username does not exist")
            return "Username does not exist"
        if self.users[username] != password:
            logging.warning(f"Invalid password for user: {username}") 
            return "Invalid credentials"
        
        logging.info(f"User  login: {username} successful")
        return "Login successful"
    
    def get_user(self, username):
        logging.info(f"Retrieving user data: {username}")
        if username not in self.users:
            logging.warning("Data retrieval unsuccessful")
            return "User  does not exist"
        
        user_data = {"username": username, "password": self.users[username]}  # Dummy data
        logging.info(f"Data retrieved for user '{username}': {user_data}")
        return user_data

# Example usage
if __name__ == "__main__":
    user_manager = UserManager()
    
    while True:
        print("\n1. Register User")
        print("2. Login User")
        print("3. Get User Data")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(user_manager.register_user(username, password))
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(user_manager.login_user(username, password))
        
        elif choice == '3':
            username = input("Enter username: ")
            print(user_manager.get_user(username))
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")