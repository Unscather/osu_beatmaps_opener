from pathlib import Path
import os
import zipfile

songs_directory_path = input('Input your osu! songs full directory path: ')

# Get folder path and osz files
folder_path = Path(songs_directory_path)
files = [file for file in folder_path.iterdir() if file.is_file() and file.suffix == '.osz']
osz_file_count = len(files)

# Convert files to ZIP
for file in files:
    new_file = file.with_suffix('.zip')
    file.rename(new_file)

# Get zip files
files = [file for file in folder_path.iterdir() if file.is_file() and file.suffix == '.zip']
zip_file_count = len(files)

# Extract contents to new folders
for file in files:
    new_folder_path = f'{folder_path}/{file.stem}'
    try:
        os.makedirs(new_folder_path)
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(new_folder_path)
        os.remove(file)
    except OSError as e:
        print(e)