import os

def rename_files(input_folder):
    # Get all files in the input folder
    files = os.listdir(input_folder)
    
    # Sort files to ensure consistent ordering
    files.sort()

    # Rename files sequentially
    for i, file in enumerate(files):
        if os.path.isfile(os.path.join(input_folder, file)):
            # Construct new name
            new_name = f"ODM_{i+1}"

            # Rename file
            os.rename(os.path.join(input_folder, file), os.path.join(input_folder, new_name))

            print(f"Renamed {file} to {new_name}")

# Example usage
input_folder = r'C:\\location\to\the\folder'

rename_files(input_folder)
