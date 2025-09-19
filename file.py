import os
import shutil

def move_jpg_files(source_folder, dest_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' not found.")
        return

    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"Created destination folder: '{dest_folder}'")

    # Step 1: Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        # Step 2 & 3: Check for .jpg extension (case-insensitive)
        if filename.lower().endswith("m2.jpg"):
            source_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(dest_folder, filename)

            try:
                # Step 4: Move the file
                shutil.move(source_path, dest_path)
                print(f"Moved: {filename}")
            except Exception as e:
                print(f"Could not move {filename}: {e}")

# ✅ Run the function with your actual folder names
move_jpg_files("m2.jpg", "jpegs_folder")
