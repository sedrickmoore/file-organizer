# File Organizer

### Description

This Python script organizes files in a specified folder into categorized subfolders based on file extensions. It is designed to help users keep their directories neat and structured.

### Features

Categorizes files into predefined folders such as Images/, Videos/, Documents/, Audio/, Archives/, Code/, Executables/, and Others/.

Automatically creates necessary subfolders if they don't exist.

Moves files to the appropriate folder based on their extensions.

Ensures all uncategorized files are placed in the Others/ folder.

### Installation

Ensure you have Python installed (version 3.x recommended).

Clone this repository or download the script.

```
git clone https://github.com/sedrickmoore/file-organizer.git
cd file-organizer
```
### Usage

Run the script with Python:

`python3 file_organizer.py`

Enter the path of the folder you want to organize when prompted.

Alternatively, modify the script to specify the folder path directly in the organize_files() function.

### Future Enhancements

Implement CLI arguments for specifying the folder path without user input.

Add real-time file monitoring to organize files automatically.

Allow users to define custom file categories through a config file.