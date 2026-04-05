import sys
class Login:
    def checking(self, regis_email, regis_password,):
        print("\n Gmail Login ")
        max_attempts = 5
        for attempt in range(1,max_attempts + 1):
            login_email = input("Enter your email: ")
            login_password = input("Enter your password: ")
            if login_email == regis_email and login_password == regis_password:
                print("Login successful.")
                return True
            else:
                left_attempts = max_attempts - attempt
                if left_attempts > 0:
                    print(f"Login failed. {left_attempts} attempts left!")
                else:
                    sys.exit("Too many attemts.Try again later.")

                

            
        