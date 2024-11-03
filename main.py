import os
import getpass
import re

class ClientEnvironment:
    def __init__(self):
        # Getting
        #  the current client_name and home directory path
        self.client_name = getpass.getuser()
        self.home_dir_path = os.path.expanduser("~")
        self.client_dir = os.path.join(self.home_dir_path, self.client_name)
        self.file_path = os.path.join(self.client_dir, ".profile.txt")

    def create_client_directory(self):
        """
        Ensuring that the client's directory exists in the home directory.
        If not, creating it and change the working directory to it.
        """
        print(f"Setting up [{self.client_name}] environment...\n")
        os.chdir(self.home_dir_path)
        
        if not os.path.exists(self.client_dir):
            print(f"Creating directory for client: {self.client_name}")
            os.mkdir(self.client_dir)
        else:
            print(f"client directory already exists: {self.client_dir}")
        
        os.chdir(self.client_dir)

    def is_valid_name(self, name):
        """
        Validating the name to contain only letters and spaces.
        """
        return bool(re.match(r"^[A-Za-z ]+$", name))

    def is_valid_phone(self, phone):
        """
        Validating the phone number to contain 7-15 digits only.
        """
        return bool(re.match(r"^[0-9]{7,15}$", phone))

    def is_valid_email(self, email):
        """
        Validating the email to ensure it has a typical email structure.
        """
        return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))

    def validate_inputs(self):
        """
        Prompt and validate client input for name, phone, and email using regex.
        """
        while True:
            name = input("Please enter your name: ")
            if not self.is_valid_name(name):
                print("Invalid name. Please use only letters and spaces.")
                continue
            
            phone = input("Please enter your phone number: ")
            if not self.is_valid_phone(phone):
                print("Invalid phone number. Must contain 7-15 digits.")
                continue
            
            email = input("Please enter your email address: ")
            if not self.is_valid_email(email):
                print("Invalid email address format.")
                continue

            print("\n--- client Details ---")
            print(f"Name: {name}")
            print(f"Phone: {phone}")
            print(f"Email: {email}")
            return {"name": name, "phone": phone, "email": email}

    def save_client_details(self, client_details):
        """
        Save the validated client details to the profile file.
        """
        print("Saving client details...")
        with open(self.file_path, 'w') as file:
            file.write(f"Name: {client_details['name']}\n")
            file.write(f"Phone: {client_details['phone']}\n")
            file.write(f"Email: {client_details['email']}\n")

    def read_profile_file(self):
        """
        Read and display the content of profile.txt, if it exists.
        """
        if os.path.exists(self.file_path):
            print(f"\n--- Profile Information ---")
            with open(self.file_path, 'r') as file:
                print(file.read())

    def check_and_update_profile(self):
        """
        Checking if profile.txt exists and is up to date.
        If it doesn't exist or if the information is outdated, prompting for updates.
        """
        if os.path.exists(self.file_path):
            self.read_profile_file()
            while True:
                client_res = input("Is the information above up to date? (Yes/y or No/n): ")
                if client_res.lower() in ['yes'.lower(), 'y'.lower()]:
                    print("ACCESS GRANTED.\n")
                    break
                elif client_res.lower() in ['no'.lower(), 'n'.lower()]:
                    print("Updating your details...")
                    client_details = self.validate_inputs()
                    self.save_client_details(client_details)
                    print("ACCESS GRANTED.\n")
                    break
                else:
                    print("Please enter a valid response.")
        else:
            print("Profile file not found. Creating a new profile...")
            client_details = self.validate_inputs()
            self.save_client_details(client_details)
            print("ACCESS GRANTED.")

    def execute(self):
        """
        Running the complete flow for setting up the client environment, directory, file,
        validation, and updating or creating client details.
        """
        print(f"Welcome => {self.client_name} <=\n")
        self.create_client_directory()
        self.check_and_update_profile()

# Create an instance of ClientEnvironment and execute the setup
if __name__ == "__main__":
    client_env = ClientEnvironment()
    client_env.execute()
