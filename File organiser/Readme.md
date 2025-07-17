## File organser
### This is a Python File Organizer script that automatically sorts files in a given directory based on their file extensions. It moves files into categorized folders such as Images, Documents, Videos, etc. Additionally, it supports in-place sorting within folders by name, type, and date (optional view/log only — no extra folders are created).

.

# 🚀 Features
- Organizes files into folders based on their file extension:

- Images, Documents, Spreadsheets, Videos, Archives, Others

- Skips directories, only processes files.

- Automatically creates destination folders if they don't exist.

- Logs all file moves using Python’s logging module.

- Supports in-place sorting info by:

- Filename

- File extension

- Creation date

# 📁 Supported File Types
ExtensionFiles = {
    'Images': ['.img', '.gif', '.jpeg', '.jpg', '.png', '.svg'],
    'Documents': ['.pptx', '.docx', '.doc', '.pdf', '.exe', '.txt', '.html', '.bat'],
    'Spreadsheet': ['.xlcs', '.csv'],
    'Videos': ['.mp4', '.mov'],
    'Archives': ['.zip', '.tar', '.rar'],
    'Others': []
}

# 📌 How to Use
- Clone or download the script:
    - git clone https://github.com/your-username/file-organizer.git
    - cd file-organizer

- python file_organizer.py
- When prompted, enter the full path to the folder you want to organize.

    - Example: Enter folder path: C:\Users\YourName\Downloads


# 📁 YourFolder/
    ├── 📁 Images/
    │   └── image1.jpg
    ├── 📁 Documents/
    │   └── resume.docx
    ├── 📁 Videos/
    │   └── movie.mp4
    ├── 📁 Spreadsheet/
    │   └── data.csv
    ├── 📁 Archives/
    │   └── backup.zip
    ├── 📁 Others/
    │   └── unknown.xyz
