from PIL import Image
import os

def resize_images_in_directory(directory, desired_width, desired_height):
    if os.path.exists(directory):
        # Iterate through all files in the directory
        for filename in os.listdir(directory):
            # Check if the file is an image (you can adjust the file extensions as needed)
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')):
                # Open the image
                image_path = os.path.join(directory, filename)
                image = Image.open(image_path)

                # Resize the image
                resized_image = image.resize((desired_width, desired_height), Image.ANTIALIAS)

                # Save the resized image, overwriting the original
                resized_image.save(image_path)

                # Close the image
                resized_image.close()

                # Print statements for debugging
                print(f"Resized: {image_path} to {desired_width}x{desired_height}")
    else:
        print(f"Directory '{directory}' does not exist.")

# Specify the directories and dimensions
directories = [
    '/Users/sumaiyauddin/Documents/Semester03/CCNY-DSE-Capstone-Project-Segmenting-Coral-Branch-tips/data/external/Coral_images/APAL',
    '/Users/sumaiyauddin/Documents/Semester03/CCNY-DSE-Capstone-Project-Segmenting-Coral-Branch-tips/data/external/Coral_images/Pseudodiploria'
]
desired_width = 512
desired_height = 512

# Resize images in each directory
for directory in directories:
    resize_images_in_directory(directory, desired_width, desired_height)
