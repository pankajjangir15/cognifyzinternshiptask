import re

def validate_email():
    email = input("Enter the email address: ")

    # Define the regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Use re.match() to check if the email matches the pattern
    if re.match(pattern, email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")

while True:
    validate_email()
    continue_prompt = input("Do you want to validate another email? (yes/no): ").strip().lower()
    if continue_prompt != 'yes':
        print("Exiting the program.")
        break
