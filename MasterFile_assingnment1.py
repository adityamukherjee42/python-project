import json
import os

os.chdir("C:\\Users\\abhin\\OneDrive\\Documents\\Course Content\\Python programming")

def load_json_file_named(file_name):
    try: 
        loaded_data = []
        file_location = f"data/{file_name}"
        with open(file_location, 'r') as file: # or f"data/{file_name}" depending on your files
            loaded_data =  json.load(file)
    except OSError as e:
        print(f"Error. Does the file exist in this folder? {file_location}\n\n {e}")
    return loaded_data

file_path = "nhs_scotland_boards.json"
with open(file_path, 'r') as json_file:
    data = json.load(json_file)

print(data)

print(data[0])