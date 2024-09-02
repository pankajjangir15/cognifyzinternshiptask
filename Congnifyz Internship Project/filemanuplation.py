def count_word_occurrences(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                word = word.strip('.,!?;:"()[]{}')  # Remove punctuation
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count

def display_word_counts(word_count):
    for word in sorted(word_count):
        print(f"{word}: {word_count[word]}")

while True:
    file_path = input("Enter the path to the text file: ")
    try:
        word_count = count_word_occurrences(file_path)
        display_word_counts(word_count)
    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")
    
    continue_prompt = input("Do you want to analyze another file? (yes/no): ").strip().lower()
    if continue_prompt != 'yes':
        print("Exiting the program.")
        break
