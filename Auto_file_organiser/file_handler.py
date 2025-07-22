import os
import shutil
from watchdog.events import FileSystemEventHandler
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Define file types and their target folders
ExtensionFiles = {
    'Images': ['.img', '.gif', '.jpeg', '.jpg', '.png', '.svg'],
    'Documents': ['.pptx', '.docx', '.doc', '.pdf', '.exe', '.txt', '.html', '.bat', '.ppt'],
    'Spreadsheet': ['.xlsx', '.csv', '.xls'],
    'Videos': ['.mp3', '.mp4', '.mov'],
    'Archives': ['.zip', '.tar', '.rar'],
    'Others': []
}

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        file_name = os.path.basename(file_path)
        ext = os.path.splitext(file_name)[1].lower()

        moved = False
        for folder, extensions in ExtensionFiles.items():
            if ext in extensions:
                dest_folder = os.path.join(os.path.expanduser("C:/Users/2001k/Downloads/Organized"), folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, file_name))
                logging.info(f"Moved '{file_name}' to '{folder}' folder.")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(os.path.expanduser("C:/Users/2001k/Downloads/Organized"), "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file_name))
            logging.info(f"Moved '{file_name}' to 'Others' folder.")
