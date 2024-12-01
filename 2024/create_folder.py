import os
import shutil
import argparse

def create_day_folder(day_number, template_file="template.py"):
    folder_name = "day-{:02d}".format(day_number)

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print("Created folder: {}".format(folder_name))
    else:
        print("Folder '{}' already exists.".format(folder_name))
        return
    
    files = ["solution.py", "input.txt", "example-input.txt"]

    for file in files:
        file_path = os.path.join(folder_name, file)
        if file == "solution.py" and os.path.exists(template_file):
            shutil.copy(template_file, file_path)
            print("Copied template to: {}".format(file_path))
        else:
            with open(file_path, 'w') as f:
                pass
            print("Created empty file: {}".format(file_path))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a folder with files for a specific day.")
    parser.add_argument(
        "day_number",
        type=int,
        help="The day number to create the folder."
    )
    parser.add_argument(
        "--template",
        type=str,
        default="template.py",
        help="Path to the template file for solution.py (default: template.py)."
    )

    args = parser.parse_args()
    create_day_folder(args.day_number, args.template)