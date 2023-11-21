import os

def clean_working_directory():
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    files_to_delete = []

    # Iterate through files in the directory
    for file_name in os.listdir(current_directory):
        if file_name.endswith(".csv") or file_name.endswith(".jpg"):
            files_to_delete.append(file_name)

    # Delete the identified files
    for file_name in files_to_delete:
        os.remove(os.path.join(current_directory, file_name))
        print(f"Deleted: {file_name}")

if __name__ == "__main__":
    clean_working_directory()
