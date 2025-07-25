import os
import shutil
from colorama import Fore, Style, init

# Initialize colorama for gentle console colors
init(autoreset=True)

# Define the path of the folder to be organized
folder_path = input("Please enter the full path of the folder you'd like to organize:\n> ").strip()

# A palette
PASTEL_PURPLE = Fore.LIGHTMAGENTA_EX
PASTEL_GREEN = Fore.LIGHTGREEN_EX
PASTEL_CYAN = Fore.LIGHTCYAN_EX
PASTEL_RED = Fore.LIGHTRED_EX
PASTEL_GRAY = Fore.LIGHTBLACK_EX

# Mapping of file extensions to their corresponding categories
extension_mapping = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Others": []
}

# Determines the category based on file extension
def determine_category(extension):
    for category, extensions in extension_mapping.items():
        if extension.lower() in extensions:
            return category
    return "Others"

# The core function that organizes the folder contents
def organize_folder(path):
    if not os.path.exists(path):
        print(PASTEL_RED + "The provided path does not exist. Please verify and try again.")
        return

    contents = os.listdir(path)
    if not contents:
        print(PASTEL_GRAY + "The folder is already in perfect order. No action needed.")
        return

    for item in contents:
        full_item_path = os.path.join(path, item)

        # Proceed only if the item is a file
        if os.path.isfile(full_item_path):
            _, extension = os.path.splitext(item)
            category = determine_category(extension)
            destination_folder = os.path.join(path, category)

            # Create the category folder if it does not yet exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
                print(PASTEL_GREEN + f"Created folder: {category}")

            # Move the file to its designated category folder
            shutil.move(full_item_path, os.path.join(destination_folder, item))
            print(PASTEL_CYAN + f"Moved: {item} → {category}/")

    print(PASTEL_PURPLE + "\nThe task is complete. Your folder is now gracefully arranged.")

# Let the operation commence
organize_folder(folder_path)


