import os

def find_files(suffix, path):
    if suffix == '':
        return []

    if len(os.listdir(path)) == 0:
        return []

    path_elements = os.listdir(path)
    path_files = [file for file in path_elements if '.'+ suffix in file]
    path_folders = [folder for folder in path_elements if '.' not in folder]

    for folder in path_folders:
        path_files.extend(find_files(suffix=suffix, path = path + '/' + folder))

    return path_files

# Testing
# Move this file to the testing folder
path = os.getcwd()
print(find_files('c',path))

print(find_files('',path))

print(find_files('.c','non-existent/folder'))
