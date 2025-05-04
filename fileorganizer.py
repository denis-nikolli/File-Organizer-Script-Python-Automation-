import os

folder_path = "C:/Users/user/Downloads" 

files = os.listdir(folder_path)

print("Files in the folder:")
for file in files:
    print(file)

import shutil

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Executables": [".exe", ".msi"],
    "Archives": [".zip", ".rar"],
}


for file in files:
    file_path = os.path.join(folder_path, file)
    
    if os.path.isdir(file_path):
        continue
    
    _, ext = os.path.splitext(file)
    
    for folder_name, extensions in file_types.items():
        if ext.lower() in extensions:
            target_folder = os.path.join(folder_path, folder_name)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, file))
            print(f"Moved {file} to {folder_name}/")
            break
