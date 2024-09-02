import os
import shutil

def organize_files(directory):
    # Define the file type categories and their corresponding extensions
    file_types = {
        'Documents': ['.pdf', '.docx', '.txt'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Music': ['.mp3', '.wav'],
        'Archives': ['.zip', '.rar', '.tar.gz']
    }

    # Create folders for each file type category if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files into their corresponding folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    moved = True
                    break
            if not moved:
                # Move files with unknown extensions to 'Others' folder
                others_folder = os.path.join(directory, 'Others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, os.path.join(others_folder, filename))

while True:
    directory = input("Enter the path to the directory you want to organize: ")
    if os.path.exists(directory) and os.path.isdir(directory):
        organize_files(directory)
        print(f"Files in {directory} have been organized.")
    else:
        print("Invalid directory. Please enter a valid path.")
    
    continue_prompt = input("Do you want to organize another directory? (yes/no): ").strip().lower()
    if continue_prompt != 'yes':
        print("Exiting the program.")
        break
