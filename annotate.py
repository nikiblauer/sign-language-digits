import os
import pandas as pd
from glob import glob

def create_annotation_csv(root_dir, output_csv='annotations.csv'):
    """
    Creates an annotation CSV file with image names and their corresponding labels.

    Parameters:
    - root_dir: str - Path to the root folder containing subfolders labeled 0-9.
    - output_csv: str - Name of the output CSV file.
    """
    data = []

    # Iterate through each subfolder (label folders)
    for label_folder in sorted(os.listdir(root_dir)):
        folder_path = os.path.join(root_dir, label_folder)
        
        # Ensure it's a folder and the folder name is a valid label
        if os.path.isdir(folder_path) and label_folder.isdigit():
            image_paths = glob(os.path.join(folder_path, '*'))  # Get all files in the folder

            for image_path in image_paths:
                image_name = os.path.basename(image_path)
                data.append({'image_name': image_name, 'label': int(label_folder)})

    # Save to CSV
    df = pd.DataFrame(data)
    df.to_csv(output_csv, index=False)
    print(f"Annotation CSV saved as '{output_csv}' with {len(df)} entries.")

# Example usage:
root_directory = './data'  # Replace with your actual folder path
create_annotation_csv(root_directory)

