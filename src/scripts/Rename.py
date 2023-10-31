import os

# Specify the directory containing your coral images
base_directory = '/Users/sumaiyauddin/Documents/Semester03/CCNY-DSE-Capstone-Project-Segmenting-Coral-Branch-tips/data/external/Coral_images/Test/APAL'

if os.path.exists(base_directory):
    # Create a counter to keep track of the image number
    counter = 1

    # Iterate through all files in the directory
    for filename in os.listdir(base_directory):
        # Check if the file is a .jpg file
        if filename.endswith(('.jpg','.jpeg','.png')):
            # Construct the new filename
            new_filename = f'APAL{counter:02}.jpg'
            old_filepath = os.path.join(base_directory, filename)
            new_filepath = os.path.join(base_directory, new_filename)

            # Print statements for debugging
            print(f"Renaming: {old_filepath} -> {new_filepath}")

            # Rename the file
            try:
                os.rename(old_filepath, new_filepath)
            except Exception as e:
                print(f"Error renaming {old_filepath}: {e}")

            # Increment the counter
            counter += 1
else:
    print(f"Directory '{base_directory}' does not exist.")



# Specify the directory containing your coral images
base_directory = '/Users/sumaiyauddin/Documents/Semester03/CCNY-DSE-Capstone-Project-Segmenting-Coral-Branch-tips/data/external/Coral_images/Test/Pseudodiploria'

if os.path.exists(base_directory):
    # Create a counter to keep track of the image number
    counter = 1

    # Iterate through all files in the directory
    for filename in os.listdir(base_directory):
        # Check if the file is a .JPG file (uppercase)
        if filename.endswith(('.jpg','.jpeg','.png')):
            # Construct the new filename
            new_filename = f'Pseudodiploria{counter:02}.jpg'
            old_filepath = os.path.join(base_directory, filename)
            new_filepath = os.path.join(base_directory, new_filename)

            # Print statements for debugging
            print(f"Renaming: {old_filepath} -> {new_filepath}")

            # Rename the file
            try:
                os.rename(old_filepath, new_filepath)
            except Exception as e:
                print(f"Error renaming {old_filepath}: {e}")

            # Increment the counter
            counter += 1
else:
    print(f"Directory '{base_directory}' does not exist.")
