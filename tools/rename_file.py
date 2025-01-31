import os
import argparse
import re

def rename_files_in_folder(folder_path, base_name):
    """
    Renames files in the specified folder that do not match the base pattern.
    It continues numbering from the last correctly named file.

    Args:
        folder_path (str): The path to the folder containing the files to be renamed.
        base_name (str): The base name for the files.

    Returns:
        None
    """
    try:
        # List all files in the folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        # Define the regex pattern to match correctly named files
        pattern = re.compile(rf"^{re.escape(base_name)}(\d+)\..+$")
        
        # Identify the highest existing index in correctly named files
        max_index = 0
        for file in files:
            match = pattern.match(file)
            if match:
                max_index = max(max_index, int(match.group(1)))
        
        # Iterate through the files and rename only those that don't match the pattern
        for file in files:
            if not pattern.match(file):
                file_extension = os.path.splitext(file)[1]
                max_index += 1  # Increment the index
                new_name = f"{base_name}{str(max_index)}{file_extension}"
                
                old_path = os.path.join(folder_path, file)
                new_path = os.path.join(folder_path, new_name)
                
                os.rename(old_path, new_path)
                print(f"Renamed '{file}' -> '{new_name}'")

        print("Renaming completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Rename files that do not match the base pattern while continuing numbering.",
        epilog="Example: python rename_files.py /path/to/folder base_name_"
    )
    parser.add_argument("folder_path", type=str, help="The path to the folder containing the files to be renamed.")
    parser.add_argument("base_name", type=str, help="The base name for the renamed files.")

    args = parser.parse_args()

    rename_files_in_folder(args.folder_path, args.base_name)
