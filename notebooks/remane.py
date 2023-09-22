import os
import shutil

# Specify the directory containing your image folders
base_directory = '/Users/sumaiyauddin/Documents/Semester03/CCNY-DSE-Capstone-Project-Segmenting-Coral-Branch-tips/data/external/Coral_images/APAL_photos'

# Iterate through all folders in the base directory
for folder_name in os.listdir(base_directory):
    folder_path = os.path.join(base_directory, folder_name)

    # Check if the item in the directory is a folder
    if os.path.isdir(folder_path):
        # List all files in the folder
        files = os.listdir(folder_path)

        # Iterate through the files and rename them
        for filename in files:
            old_filepath = os.path.join(folder_path, filename)

            # Construct the new filename using the folder name
            new_filename = folder_name + os.path.splitext(filename)[-1]
            new_filepath = os.path.join(folder_path, new_filename)

            # Rename the file
            shutil.move(old_filepath, new_filepath)


