import sys
class Info:
    def __init__(self):
        self.fullname = ""
        self.username = ""
        self.email = ""
        self.password = ""

    def ask_and_validate(self, topic, field_name ):

        attempts = 5
        while attempts > 0:
            user_input = input(f"Enter your {topic}: ")
            is_valid = False
            if field_name == "name" or field_name == "username":
                if user_input != "":is_valid = True

            elif field_name == "email":
                if "@" in user_input and ".com" in user_input: is_valid = True

            elif field_name == "password":
                if len(user_input) >= 6: is_valid = True

            if is_valid:
                return user_input
                
            attempts -= 1
            if attempts > 0:
                print(f"Invalid {topic}!.Try Again(Attempts left {attempts})")
            else:
                print(f"Too many attempts for {topic}.Try again later.Sorry.")
                sys.exit()
    def get_data(self):
        print("\n Gmail Registration ")  
        self.fullname = self.ask_and_validate("full name", "name")
        self.username = self.ask_and_validate("user name", "username")
        self.email = self.ask_and_validate("email address","email")
        self.password = self.ask_and_validate("password","password")

        attempts = 5
        while attempts > 0:
            confirm = input("Confirm your password: ")
            if confirm == self.password:
                print("\nRegistration Successful!")
                return True
            attempts -= 1
            if attempts > 0:
                print(f"Passwords do not match! (Attempts left: {attempts})")
            else:
                sys.exit("Password confirmation failed.")


        