import os

# Choose the folder to organize (you can change this path)
folder_path = "C:/Users/user/Downloads"  # Replace this with your folder

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Print all files
print("Files in the folder:")
for file in files:
    print(file)

import shutil

# Define where to move each file type
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Executables": [".exe", ".msi"],
    "Archives": [".zip", ".rar"],
}

# Organize the files
for file in files:
    file_path = os.path.join(folder_path, file)
    
    # Skip folders
    if os.path.isdir(file_path):
        continue
    
    # Get the file extension
    _, ext = os.path.splitext(file)
    
    # Move file to the appropriate folder
    for folder_name, extensions in file_types.items():
        if ext.lower() in extensions:
            target_folder = os.path.join(folder_path, folder_name)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, file))
            print(f"Moved {file} to {folder_name}/")
            break
