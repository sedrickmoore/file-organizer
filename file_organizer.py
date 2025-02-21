import os
import shutil
import argparse
import json

def organize_files(source_folder):
    # Organizes files in the specified folder into categorized subfolders.
    print(f"Checking folder: {source_folder}")

    if not os.path.exists(source_folder):
        print(f"Error: The folder '{source_folder}' does not exist.")
        return

    # Define categories and their corresponding file extensions
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff", ".webp"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".mpeg"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".csv", ".pptx", ".ppt", ".odt"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".iso"],
        "Code": [".py", ".js", ".java", ".cpp", ".c", ".cs", ".html", ".css", ".php", ".sh", ".rb", ".go", ".swift"],
        "Executables": [".exe", ".bat", ".msi", ".sh", ".apk", ".app", ".dmg"],
        "Others": []
    }

    # Create subfolders if they don't exist
    for category in categories:
        category_path = os.path.join(source_folder, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            print(f"Created folder: {category_path}")

    # Organize files
    found_files = False  # Check if any files were processed
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1].lower()
            moved = False
            found_files = True

            for category, extensions in categories.items():
                if file_extension in extensions:
                    print(f"Moving {file_name} to {category}")
                    shutil.move(file_path, os.path.join(source_folder, category, file_name))
                    moved = True
                    break

            # If file didn't match any category, move to "Others"
            if not moved:
                print(f"Moving {file_name} to Others")
                shutil.move(file_path, os.path.join(source_folder, "Others", file_name))

    if not found_files:
        print("No files found to organize.")

    for subfolder in os.listdir(source_folder):
        if subfolder in categories:
            subfolder_path = os.path.join(source_folder, subfolder)
            try:
                os.rmdir(subfolder_path)
                print(f"Deleted empty folder: {subfolder}")
            except OSError:
                print(f"'{subfolder}' is not empty or does not exist.")

    print("Files organized successfully!")


def main():
    parser = argparse.ArgumentParser(description="Organize files in a specified folder.")
    parser.add_argument("folder_path", help="Full path to the folder you organize")
    args = parser.parse_args()

    organize_files(args.folder_path)

if __name__ == "__main__":
    main()
