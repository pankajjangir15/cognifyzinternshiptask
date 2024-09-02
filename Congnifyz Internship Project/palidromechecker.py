def is_palindrome(s):
    # Remove any spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

while True:
    input_str = input("Enter a string: ")
    if is_palindrome(input_str):
        print(f'"{input_str}" is a palindrome.')
    else:
        print(f'"{input_str}" is not a palindrome.')
    
    continue_prompt = input("Do you want to check another string? (yes/no): ").strip().lower()
    if continue_prompt != 'yes':
        print("Exiting the program.")
        break
