import os
import shutil


# Example usage:
source_folder = input('Enter Source folder: ')  # Replace with your source folder path
destination_folder = input('Enter Destination Folder: ')  # Replace with your destination folder path
index_to_copy = int(input("Enter Index Number: "))  # Replace with the index you want to copy

def copy_lines_by_index(source_folder, destination_folder, index_to_copy):
    try:
        # Create the destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Iterate through each file in the source folder
        for filename in os.listdir(source_folder):
            source_file_path = os.path.join(source_folder, filename)

            # Check if the file is a text file
            if filename.endswith(".txt"):
                # Read the content of the source file into a list of lines
                with open(source_file_path, 'r', encoding='latin-1') as source_file:
                    lines = source_file.readlines()

                # Check if the index is valid
                if 0 <= index_to_copy < len(lines):
                    # Create a new file in the destination folder
                    destination_file_path = os.path.join(destination_folder, filename)

                    # Write the copied line to the destination file
                    with open(destination_file_path, 'w', encoding='latin-1') as destination_file:
                        destination_file.write(lines[index_to_copy])
                    print(f"Line at index {index_to_copy} from {filename} copied successfully.")
                else:
                    print(f"Invalid index for {filename}. Skipping.")
            else:
                print(f"Skipping non-txt file: {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")


copy_lines_by_index(source_folder, destination_folder, index_to_copy)
