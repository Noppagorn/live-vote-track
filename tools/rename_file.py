import os
import argparse

def rename_files_in_folder(folder_path, base_name):
    """
    Renames every file in the specified folder to the format: base_name + number (zero-padded).

    Args:
        folder_path (str): The path to the folder containing the files to be renamed.
        base_name (str): The base name for the files.

    Returns:
        None
    """
    try:
        # List all files in the folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        # Calculate the zero-padding width based on the number of files
        num_files = len(files)
        padding_width = len(str(num_files))

        # Iterate through the files and rename them
        for index, file in enumerate(files, start=1):
            # Extract the file extension
            file_extension = os.path.splitext(file)[1]

            # Create the new file name with zero-padding
            new_name = f"{base_name}{str(index).zfill(padding_width)}{file_extension}"

            # Construct the full paths for renaming
            old_path = os.path.join(folder_path, file)
            new_path = os.path.join(folder_path, new_name)

            # Rename the file
            os.rename(old_path, new_path)

        print(f"Successfully renamed {len(files)} files in '{folder_path}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Rename all files in a folder to a specified base name with sequential numbering.",
        epilog="Example: python rename_files.py /path/to/folder base_name_"
    )
    parser.add_argument("folder_path", type=str, help="The path to the folder containing the files to be renamed. For example: /home/user/documents.")
    parser.add_argument("base_name", type=str, help="The base name for the renamed files. For example: file_ or image_.")

    args = parser.parse_args()

    rename_files_in_folder(args.folder_path, args.base_name)
