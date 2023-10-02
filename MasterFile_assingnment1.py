import json
import os
import plotly.express as px
from itertools import chain
import pandas as pd

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



# Function to parsse through various nested dictionary dimensions
def extract_all_values(dict_temp, dimension):
    # Clear the list before appending new values
    value_list_def = list(value for key, value in dict_temp.items())
    key_list_def = list(key for key, value in dict_temp.items())
    result = key_list_def if dimension == "key" else value_list_def

    return result


budget_count = list(chain(*list(extract_all_values(i['budget_billions'], "values") for i in data)))
regions= list(i['name'] for i in data for _ in range(3))
year_mapping = list(chain(*list(extract_all_values(i['budget_billions'], "key") for i in data)))

data_sunburst = dict(
    budget_count = budget_count,
    regions = regions,
    years = year_mapping
)



fig = px.sunburst(data_sunburst,path= ['regions', 'years'], values = 'budget_count',color = 'budget_count', title = "SunBurst Chart of Accumulated Budgets over years for different NHS bases")

fig.show()






