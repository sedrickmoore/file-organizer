# File Organizer

### Description

This Python script organizes files in a specified folder into categorized subfolders based on file extensions. It is designed to help users keep their directories neat and structured.

### Features

Categorizes files into predefined folders such as Images/, Videos/, Documents/, Audio/, Archives/, Code/, Executables/, and Others/.

Automatically creates necessary subfolders if they don't exist.

Moves files to the appropriate folder based on their extensions.

Ensures all uncategorized files are placed in the Others/ folder.

Use a JSON file to create custom categories.

### Installation

Ensure you have Python installed (version 3.x recommended).

Clone this repository or download the script.

```
git clone https://github.com/sedrickmoore/file-organizer.git
cd file-organizer
```
### Usage

Run the script with Python:

`python3 file_organizer.py <full_folder_path> --config <full_path_to_json>`

Must use the path to the folder as a command line argument.

Config file (JSON) is optional.

### Future Enhancements

Add real-time file monitoring to organize files automatically.