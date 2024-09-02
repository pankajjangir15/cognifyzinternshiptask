def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

while True:
    try:
        num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
        else:
            fibonacci_sequence = generate_fibonacci(num_terms)
            print(f"Fibonacci sequence up to {num_terms} terms: {fibonacci_sequence}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    
    continue_prompt = input("Do you want to generate another Fibonacci sequence? (yes/no): ").strip().lower()
    if continue_prompt != 'yes':
        print("Exiting the program.")
        break
