import os
import sys
import re
from pathlib import Path

def match_case(old_str, new_str, matched_str):
    """Match the case pattern of the old string in the matched text."""
    if matched_str.isupper():
        return new_str.upper()
    if matched_str.islower():
        return new_str.lower()
    return new_str

def replace_in_file(file_path, old_str, new_str):
    """Replace string in file contents case insensitively with case matching."""
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Use regex for case insensitive replacement with case matching
        pattern = re.compile(re.escape(old_str), re.IGNORECASE)
        if pattern.search(content):
            # Custom replacement function to match case
            new_content = pattern.sub(lambda m: match_case(old_str, new_str, m.group(0)), content)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated content in: {file_path}")
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}")

def is_target_file(file_path):
    """Check if file has target extension."""
    target_extensions = {'.cs', '.cpp', '.h', '.lua', '.json'}
    return file_path.suffix.lower() in target_extensions

def rename_file(file_path, old_str, new_str):
    """Rename file if old string exists in filename (case insensitive with case matching)."""
    try:
        path_str = str(file_path)
        pattern = re.compile(re.escape(old_str), re.IGNORECASE)
        
        if pattern.search(path_str):
            # Apply case matching for filename
            new_path = Path(pattern.sub(lambda m: match_case(old_str, new_str, m.group(0)), path_str))
            if new_path != file_path:  # Only rename if there's a change
                file_path.rename(new_path)
                print(f"Renamed: {file_path} -> {new_path}")
                return new_path
        return file_path
    except Exception as e:
        print(f"Error renaming {file_path}: {str(e)}")
        return file_path

def process_directory(directory, old_str, new_str):
    """Recursively process directory for string replacement."""
    try:
        directory = Path(directory)
        
        # First, process all files in current and subdirectories
        for file_path in list(directory.rglob("*")):
            if file_path.is_file() and is_target_file(file_path):
                replace_in_file(file_path, old_str, new_str)

        # Then handle directory and file renaming from deepest level up
        for dir_path, dirs, files in os.walk(str(directory), topdown=False):
            # Rename files first
            for file_name in files:
                file_path = Path(dir_path) / file_name
                if is_target_file(file_path):
                    rename_file(file_path, old_str, new_str)
            
            # Then rename the directory itself
            dir_path_obj = Path(dir_path)
            if dir_path_obj != directory:  # Don't rename the root directory
                rename_file(dir_path_obj, old_str, new_str)
                
    except Exception as e:
        print(f"Error processing directory {directory}: {str(e)}")

def main():
    # Get the string to replace (with default value)
    old_str = input("Enter string to replace (default 'Starter'): ").strip()
    if not old_str:
        old_str = "Starter"
    
    # Get the replacement string
    new_str = input("Enter replacement string: ").strip()
    while not new_str:
        print("Replacement string cannot be empty!")
        new_str = input("Enter replacement string: ").strip()
    
    # Get current working directory
    current_dir = os.getcwd()
    
    # Confirm with user
    print(f"\nWill replace all occurrences of '{old_str}' with '{new_str}'")
    print(f"in directory: {current_dir}")
    print("This will affect both file contents and names recursively (case insensitive).")
    print("Only processing files with extensions: .cs, .cpp, .h, .lua, .json")
    print("Case will be matched (e.g., OLDSTRING -> NEWSTRING, oldstring -> newstring)")
    confirm = input("\nProceed? (y/n): ").lower()
    
    if confirm == 'y':
        print("\nProcessing files and directories...")
        process_directory(current_dir, old_str, new_str)
        print("\nReplacement complete!")
    else:
        print("\nOperation cancelled.")
    
    # Wait for input before closing
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()