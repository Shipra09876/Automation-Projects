import os
import pathlib
import datetime
import shutil
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ExtensionFiles={
    'Images':['.img','.gif','.jpeg','.jpg','.png','.svg'],
    'Documents':['.pptx','.docx','.doc','.pdf','.exe','.txt','.html','.bat'],
    'Spreadsheet':['.xlsx','.csv','.xls'],
    'Videos': ['.mp3','.mp4', '.mov'],
    'Archives': ['.zip', '.tar', '.rar'],
    'Others':[]
}

path=input("Enter folder path: ").strip()
filter_keyword = input("Filter by name (leave empty if not needed): ").strip().lower()

folder=os.listdir(path)
for file in folder:
    if file.startswith('.'):
        continue

    file_path=os.path.join(path,file)

    # skip if it's file 
    if not os.path.isfile(file_path):
        continue

    root,ext=os.path.splitext(file)

    # print(f"root : {root}")
    # print(f"ext : {ext}")

    if filter_keyword and filter_keyword not in file.lower():
        continue

    try:
        if os.path.exists(file_path):
            ctimestamp=os.path.getctime(file_path)
            cdatetime=datetime.datetime.fromtimestamp(ctimestamp)
    except Exception as e:
        logger.error(f"Failed to get creation time for {file}: {e}")
        cdate = 'UnknownDate'

    moved=False
    for folder_name,extension in ExtensionFiles.items():
        print(folder_name,extension)

        if ext.lower() in extension:
            dest_folder=os.path.join(path,folder_name)
            print(dest_folder)
            os.makedirs(dest_folder,exist_ok=True)

            shutil.move(file_path,os.path.join(dest_folder,file))
            
            logger.info(f"Moved '{file}' to folder '{folder_name}'")
            moved=True
            break

    if not moved:
        other_folder=os.path.join(path,"Others")
        os.makedirs(other_folder,exist_ok=True)
        shutil.move(file_path,os.path.join(other_folder,file))
        logger.info(f"moved {file} to 'others'")


def list_sorted(folder_path):
    all_files=[]
    for file in os.listdir(folder_path):
        file_path=os.path.join(folder_path,file)
        if os.path.isfile(file_path):
            stat=os.stat(file_path)
            created=datetime.datetime.fromtimestamp(stat.st_ctime)
            _,ext=os.path.splitext(file)
            all_files.append((file,created,ext))

    
    print(f"\nFiles in {os.path.basename(folder_path)} (sorted by Name):")
    for f in sorted(all_files, key=lambda x: x[0].lower()):
        print(f"{f[0]} - Created: {f[1]} - Type: {f[2]}")

    print(f"\nFiles in {os.path.basename(folder_path)} (sorted by Date):")
    for f in sorted(all_files, key=lambda x: x[1]):
        print(f"{f[0]} - Created: {f[1]} - Type: {f[2]}")

    print(f"\nFiles in {os.path.basename(folder_path)} (sorted by Type):")
    for f in sorted(all_files, key=lambda x: x[2]):
        print(f"{f[0]} - Created: {f[1]} - Type: {f[2]}")


    for folder_name in ExtensionFiles.keys():
        category_folder=os.path.join(path,folder_name)
        if os.path.exists(category_folder):
            list_sorted(category_folder)
    
    # Check for 'Others'
    others_folder = os.path.join(path, "Others")
    if os.path.exists(others_folder):
        list_sorted(others_folder)

# =================================================================


    
        


