from PIL import Image
import os

# Specify the directory containing your images
base_directory = '/Users/sumaiyauddin/Documents/Semester03/CCNY-DSE-Capstone-Project-Segmenting-Coral-Branch-tips/data/external/Coral_images/APAL'

# Define the desired width and height for resizing
desired_width = 1080
desired_height = 1080

if os.path.exists(base_directory):
    # Iterate through all files in the directory
    for filename in os.listdir(base_directory):
        # Check if the file is an image (you can adjust the file extensions as needed)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')):
            # Open the image
            image_path = os.path.join(base_directory, filename)
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
    print(f"Directory '{base_directory}' does not exist.")
