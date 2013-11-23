'''
@author: Abdelrahman Moez - aka Hydra
@script: nested_listing.py
@description: This snippet returns all the files and all the directories
              in some given path (root) in two lists, the first for the
              files and the other for directories
@python version: 2.7
'''
# List all files in root dir, sub-dirs

import os

dir_to_list = r'C:\\Test' # directory path
all_files = []
all_dirs = []

# Start walking
for (root, dirs,files) in os.walk(dir_to_list):
    for dir in dirs:
        dir_ = os.path.join(root, dir) 
        all_dirs.append(dir_)
        for file in files:
            file_ = os.path.join(root, dir, file) 
            all_files.append(file_)
# Listing all the files & dirs	
for each in all_files:
    print  each
print '='*79
for each in all_dirs:
    print each
