def reverse_string():
    input_string = input("Enter a string: ")
    reversed_string = input_string[::-1]
    return reversed_string

# Example usage

while True:
    print("Reversed string:", reverse_string())
    continue_prompt = input("Do you want to reverse another string? (yes/no): ").strip().lower()
    if continue_prompt != 'yes':
        print("Exiting the program.")
        break


