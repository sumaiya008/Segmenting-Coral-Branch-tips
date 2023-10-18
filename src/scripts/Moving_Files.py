import os
import shutil

# Define the paths to your source and destination folders
source_folder = '/Users/sumaiyauddin/Documents/Semester03/CCNY-DSE-Capstone-Project-Segmenting-Coral-Branch-tips/data/external/Coral_images'
destination_image_folder = '/Users/sumaiyauddin/Documents/Semester03/CCNY-DSE-Capstone-Project-Segmenting-Coral-Branch-tips/data/external/image'
destination_annotation_folder = '/Users/sumaiyauddin/Documents/Semester03/CCNY-DSE-Capstone-Project-Segmenting-Coral-Branch-tips/data/external/annotation'

# Create the destination folders if they don't exist
os.makedirs(destination_image_folder, exist_ok=True)
os.makedirs(destination_annotation_folder, exist_ok=True)

# Iterate through the source folder
for root, dirs, files in os.walk(source_folder):
    for filename in files:
        if filename.endswith('.JPG'):
            # Rename the image file from .JPG to .jpg
            new_filename = filename.replace('.JPG', '.jpg')
            image_path = os.path.join(root, filename)
            new_image_path = os.path.join(root, new_filename)

            # Check if the corresponding XML file exists
            xml_path = os.path.join(root, new_filename.replace('.jpg', '.xml'))
            if os.path.exists(xml_path):
                # Move the image and XML file to their respective destination folders
                shutil.move(image_path, os.path.join(destination_image_folder, new_filename))
                shutil.move(xml_path, os.path.join(destination_annotation_folder, new_filename.replace('.jpg', '.xml')))
            else:
                print(f"XML not found for image: {new_filename}")

print("Processing complete.")
