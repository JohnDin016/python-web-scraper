import os
import shutil

def organize_files(directory):
    # Define a mapping for file extensions to folder names
    extension_mapping = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Music': ['.mp3', '.wav', '.aac']
    }

    # Check if the directory exists
    if not os.path.isdir(directory):
        print("The provided directory does not exist!")
        return

    # Process each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, extensions in extension_mapping.items():
                if file_ext in extensions:
                    target_folder = os.path.join(directory, folder)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"Moved {filename} to {folder} folder.")
                    moved = True
                    break
            if not moved:
                # If the file doesn't match any category, move to "Others"
                target_folder = os.path.join(directory, "Others")
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved {filename} to Others folder.")

if __name__ == "__main__":
    directory_to_organize = input("Enter the full path of the directory to organize: ")
    organize_files(directory_to_organize)
