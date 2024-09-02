import re

def check_password_strength(password):
    # Define the criteria for a strong password
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password)
    uppercase_criteria = re.search(r'[A-Z]', password)
    digit_criteria = re.search(r'[0-9]', password)
    special_char_criteria = re.search(r'[@$!%*?&]', password)

    # Check if all criteria are met
    if all([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria]):
        return True
    else:
        return False

while True:
    password = input("Enter a password to check its strength: ")
    if check_password_strength(password):
        print("The password is strong.")
    else:
        print("The password is weak. It should be at least 8 characters long and include uppercase and lowercase letters, digits, and special characters.")
    
    continue_prompt = input("Do you want to check another password? (yes/no): ").strip().lower()
    if continue_prompt != 'yes':
        print("Exiting the program.")
        break
