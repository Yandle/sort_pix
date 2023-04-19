import os
import shutil
import time
import argparse

def organize_files(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            modified_time = os.path.getmtime(file_path)
            modified_date = time.strftime('%Y-%m-%d', time.localtime(modified_time))
            new_folder_path = os.path.join(folder_path, modified_date)
            if not os.path.exists(new_folder_path):
                os.mkdir(new_folder_path)
            new_file_path = os.path.join(new_folder_path, file_name)
            shutil.move(file_path, new_file_path)
        elif os.path.isdir(file_path):
            organize_files(file_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Recursively re-organize files in a specified folder according to modification date into a series of contextually named sub-folders that are generated on the fly as needed.')
    parser.add_argument('folder_path', metavar='folder_path', type=str, help='the path to the folder to be organized')
    args = parser.parse_args()

    organize_files(args.folder_path)

